#!/usr/bin/env python3
"""Layer 1 v2: org extraction + classification, roles from bios.
Org categories per spec §3: vendor | enterprise | consulting | academic |
investor-media | foundation | independent | unknown"""

import json, re
from collections import Counter

# --- org classification (knowledge-based; unknowns fall back to description) ---
ORG = {}
def _add(cat, *names):
    for n in names: ORG[n.lower()] = cat

_add("vendor", "aws", "amazon agi lab", "anthropic", "openai", "google deepmind",
     "google", "microsoft", "meta", "meta superintelligence labs", "nvidia",
     "adobe", "oracle", "ibm", "tiktok", "stripe", "figma", "linkedin", "box",
     "cloudflare", "akamai", "twilio", "snowflake", "docker", "neo4j", "neo4j labs",
     "hugging face", "snyk", "vercel", "posthog", "restate", "prefect",
     "together ai", "arize ai", "arize", "unblocked", "sonar", "prime intellect",
     "humanlayer", "notion", "tldraw", "composio", "promptql", "zo computer",
     "apify", "exa", "sourcegraph", "qodo", "braintrust", "hippocratic ai",
     "abridge", "browserbase", "the browser company", "langchain", "warp",
     "bright data", "oxylabs", "deno", "minimax", "applied compute",
     "launchdarkly", "dioxus labs", "cognition", "reweaver ai", "yutori",
     "taste labs", "edge & node", "clay", "ramp", "cursor", "commercetools",
     "ironclad", "navan", "audible", "uber", "nori", "audible & tanmay sah",
     "independent ai researcher", "independent")
_add("enterprise", "john deere", "best buy", "maersk", "doordash", "paypal",
     "indeed", "best buy co", "commercetools", "maven clinic", "hinge health",
     "lease end", "morgan stanley", "two sigma", "millennium", "block",
     "alixpartners", "quantumblack", "ogilvy", "tesco", "opengov", "automattic")
_add("consulting", "quantumblack", "alixpartners", "philo ventures")
_add("academic", "uc berkeley")
_add("investor-media", "ai engineer", "towards ai", "acrew capital", "philo ventures",
     "every/cora", "every", "cora", "philo ventures", "raindrop")
_add("foundation", "agentic ai foundation")
_add("independent", "independent", "results gen")

TALKS = json.load(open("analysis/data/talks.json"))

def extract_org_b(title):
    # "Title — Name, Org" / "— Name & Name, Org" / trailing comma segment
    m = re.search(r"[—\-–]\s*[^—\-–]+,\s*([^|\n]+?)\s*\.?\s*$", title)
    if not m: return None
    org = m.group(1).strip()
    # strip "& Person, Extra" noise and trailing descriptors
    org = re.sub(r"\s*&\s*[A-Z][^,]*$", "", org).strip(" &")
    return org or None

def extract_org_b_fallback(title):
    # titles without trailing ", Org": look for a known org anywhere in the title
    tl = title.lower()
    for k in ORG:
        if re.search(r"\b" + re.escape(k) + r"\b", tl):
            return ORG[k], k
    return None, None

def extract_org_a(desc):
    # corpus A: "PRESENTED BY\nName — Title, Org" — org is the last comma segment
    if not desc: return None
    m = re.search(r"PRESENTED BY\s*\n(.+?)(?:\n\n|\nCHAPTERS|\nLINKS)", desc, re.S)
    if not m: return None
    line = m.group(1).splitlines()[0]
    m2 = re.search(r"—\s*(.+)$", line)
    if not m2: return None
    segs = [s.strip() for s in m2.group(1).split(",")]
    return segs[-1] if segs else None

def classify(org):
    if not org: return None, None
    key = org.lower().strip()
    cat = ORG.get(key)
    if cat: return org, cat
    # fallback heuristics on the org name itself
    if re.search(r"\b(ai|labs?|ai labs?|intelligence)$", key): return org, "vendor"
    if re.search(r"\b(inc|corp|corporation|llc)$", key): return org, "enterprise"
    return org, "unknown"

# corpus A descriptions live in playlist.json (talks.json carries no descriptions)
pa = {v["id"]: v for v in json.load(open("playlist.json"))["videos"]}
for t in TALKS:
    if t["conference"] == "A":
        org_raw = extract_org_a(pa[t["id"]].get("description"))
    else:
        org_raw = extract_org_b(t["title"])
        if org_raw is None:
            cat_fb, k = extract_org_b_fallback(t["title"])
            if cat_fb:
                t["layer1"]["org"] = k
                t["layer1"]["company_type"] = cat_fb
                continue
    org, cat = classify(org_raw)
    t["layer1"]["org"] = org
    t["layer1"]["company_type"] = cat
    t["layer1"]["needs_review"] = (cat in (None, "unknown")) or t["layer1"]["needs_review"]

json.dump(TALKS, open("analysis/data/talks.json", "w"), ensure_ascii=False, indent=1)
ct = Counter((t["layer1"]["company_type"] or "missing") for t in TALKS)
rev = sum(1 for t in TALKS if t["layer1"]["company_type"] in (None, "unknown"))
print("company_type:", dict(ct))
print(f"needs_review (company): {rev}")
unk = [f'{t["conference"]}{t["index"] if t["index"] else "??"} {t["layer1"].get("org")} | {t["title"][:70]}' for t in TALKS if t["layer1"]["company_type"] in (None, "unknown")]
print("\n".join(unk[:60]))

# --- ORG2: knowledge-based classification of remaining unresolved orgs ---
ORG2_EXTRA = {}
def _add2(cat, *names):
    for n in names: ORG2_EXTRA[n.lower()] = cat

_add2("vendor", "red hat", "honeycomb.io", "cisco", "github", "temporal", "modal",
      "cline", "ollama", "openrouter", "turbopuffer", "krea.ai", "sakana.ai",
      "daily", "bugcrowd", "datologyai", "general reasoning", "emulated",
      "latchbio", "g2i", "boundary", "factory", "varick agents", "sierra",
      "decagon", "datacurve", "poolside", "character.ai", "youtube ads",
      "monday.com", "mastra", "heygen", "inngest", "osmantic", "keycard",
      "bee (acq. amazon)", "gas town", "datadog", "datachain", "dratarobot",
      "datarobot", "scalekit", "hud", "radicait", "good collective",
      "progress software", "langfuse", "conductor", "alithea bio", "zenml",
      "unsloth", "google deepmind vp of research", "weco", "cua", "corridor",
      "phaidra", "ratel", "paperclip", "machinecraft", "sky valley ambient computing",
      "relai", "standardagents", "visuallabs", "mutagent", "resonate hq",
      "mongodb", "orbis", "higharc", "starlightsearch", "prosodica", "nx",
      "omnara", "openprose", "intuit", "factset", "openai codex", "wisedocs",
      "avivtor", "aviator", "inth", "decawork", "anterior", "onlay", "ufonia",
      "urun", "lemonslice", "nereu", "reelful", "rexmore", "yutori",
      "adaption", "adaption labs", "neocognition", "engram", "trajectory",
      "superconductor", "theta software", "circle", "edge & node", "town",
      "long lake", "twelvelabs", "better auth", "kepler")
_add2("enterprise", "westpac nz", "john deere", "fidelity investments", "vanguard",
      "nrc health", "nubank", "china resources holdings", "netflix", "sondermind",
      "the new york times", "jp morgan chase", "gates foundation", "intuit",
      "tesla", "pinterest", "lyft", "ebay", "krafton", "lexisnexis", "etsy",
      "duolingo", "watershed technology inc.", "watershed technology", "snapchat",
      "form3", "sigma defense", "kepler")
_add2("consulting", "newtonimpact.com", "rise8", "zs associates", "position2 (position squared)",
      "evil martians", "callstack", "nearform", "isadora & co", "flyerssoft",
      "renaissance geek, inc.", "technology advisor and consultant", "mindmakers")
_add2("independent", "author of gas town agent swarm", "programmer & author",
      "@insecure-agents", "@matthew_berman", "@t3dotgg", "independent / state of data",
      "state of data")
_add2("investor-media", "it revolution", "y combinator", "thursdai", "untapped capital",
      "ai engineer")
_add2("foundation", "terminal-bench, harbor, laude institute", "gates foundation")
_add2("government", "u.s. naval surface forces i tf hopper (ai/ml)")

# fix A2/A6 map keys mismatch: exact extracted strings above
for t in TALKS:
    if t["layer1"]["company_type"] in (None, "unknown"):
        org = (t["layer1"].get("org") or "").lower().strip().rstrip(".")
        cat = ORG2_EXTRA.get(org)
        if cat:
            t["layer1"]["company_type"] = cat
            t["layer1"]["needs_review"] = False if org in ORG2_EXTRA else True
        # fallback: fuzzy title-known-org for None-org talks
        if not org and t["conference"] == "B":
            cat_fb, k = extract_org_b_fallback(t["title"])
            if cat_fb:
                t["layer1"]["org"] = k
                t["layer1"]["company_type"] = cat_fb

# private videos
for t in TALKS:
    if t["index"] is None:
        t["layer1"]["status"] = "private"
        t["layer1"]["needs_review"] = False

json.dump(TALKS, open("analysis/data/talks.json", "w"), ensure_ascii=False, indent=1)
ct = Counter((t["layer1"]["company_type"] or "missing") for t in TALKS)
left = [(t["conference"], t["index"], t["layer1"].get("org"), t["title"][:70])
        for t in TALKS if t["layer1"]["company_type"] in (None, "unknown")]
print("company_type:", dict(ct))
print(f"remaining unresolved: {len(left)}")
for c,i,o,ti in left: print(f"{c}{i or '??'}|{o}|{ti}")
