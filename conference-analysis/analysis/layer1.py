#!/usr/bin/env python3
"""Layer 1 structuring: build talks.json from both playlist JSONs.
Deterministic + heuristic fields; ambiguous cases flagged needs_review."""
import json, re, os

KNOWN_VENDORS = [
    "openai", "anthropic", "google", "deepmind", "microsoft", "aws", "amazon",
    "meta", "nvidia", "vercel", "mongodb", "red hat", "github", "gitlab",
    "sourcegraph", "cursor", "jetbrains", "atlassian", "datadog", "elastic",
    "cloudflare", "ibm", "oracle", "salesforce", "cognition", "windsurf",
    "launchdarkly", "new relic", "hashicorp", "docker", "arize", "langchain",
    "prefect", "upstash", "neon", "supabase", "auth0", "okta", "snyk",
]

ROLE_PATTERNS = [
    (r"\bCEO|\bCOO|\bCTO|\bCPO|\bCIO|Chief \w+ Officer", "c-level", 0.9),
    (r"\bCo-?founder|\bfounder\b", "founder", 0.85),
    (r"\bVP\b|Vice President", "vp", 0.85),
    (r"\bDirector\b|Head of", "director", 0.8),
    (r"\bDr\.|\bPhD|Professor|Research Scientist|Researcher|Research Scholar", "researcher", 0.8),
    (r"\bStaff\b|\bPrincipal\b|\bDistinguished", "staff-principal", 0.7),
    (r"\bEngineer|\bDeveloper|\bArchitect", "engineer", 0.5),
    (r"\bManager\b", "manager", 0.5),
]

GENRE_PATTERNS = [
    (r"opening remark|closing remark", "remarks", 0.95, False),
    (r"\bfireside\b|\bpanel\b|fireside chat", "panel", 0.9, True),
    (r"\bkeynote\b", "keynote", 0.8, True),
    (r"demo\b|live.?build|live.?coding", "demo", 0.6, True),
    (r"6 things to know|things to know about", "promo", 0.7, False),
]

def parse_role(title, desc):
    text = title + " " + (desc[:400] if desc else "")
    for pat, role, conf in ROLE_PATTERNS:
        if re.search(pat, text, re.I):
            return role, conf, False
    return None, 0.0, True

def parse_genre(title):
    for pat, genre, conf, eligible in GENRE_PATTERNS:
        if re.search(pat, title, re.I):
            return genre, conf, eligible, False
    return "talk", 0.3, True, True  # default genre needs review only if vendor-pitch suspected

def parse_company(title, desc):
    text = (title + " " + (desc[:600] if desc else "")).lower()
    for v in KNOWN_VENDORS:
        if v in text:
            return "vendor", 0.7, v
    # enterprise end-user signals
    if re.search(r"\binc\b|\bcorp\b|enterprise|university", text):
        return "enterprise", 0.4, None
    return None, 0.0, None

def norm(v):
    return v if isinstance(v, (int, float)) else None

talks = []
for conf, meta_path in [("A", "playlist.json"), ("B", "playlist_aieng.json")]:
    data = json.load(open(meta_path))
    for v in data["videos"]:
        title, desc = v.get("title") or "", v.get("description") or ""
        role, role_conf, role_review = parse_role(title, desc)
        genre, genre_conf, eligible, genre_review = parse_genre(title)
        ctype, c_conf, matched_vendor = parse_company(title, desc)
        talks.append({
            "conference": conf,
            "index": v.get("index"),
            "id": v.get("id"),
            "title": title,
            "view_count": norm(v.get("view_count")),
            "like_count": norm(v.get("like_count")),
            "duration": norm(v.get("duration")),
            "upload_date": v.get("upload_date"),
            "transcript_uri": v.get("transcript_uri"),
            "layer1": {
                "speaker_role": role, "role_confidence": role_conf,
                "company_type": ctype, "company_confidence": c_conf,
                "matched_vendor": matched_vendor,
                "genre": genre, "genre_confidence": genre_conf,
                "message_eligible": eligible,
                "in_both_corpora": None,
                "needs_review": role_review or genre_review or c_conf == 0.4,
            },
        })

os.makedirs("analysis/data", exist_ok=True)
json.dump(talks, open("analysis/data/talks.json", "w"), ensure_ascii=False, indent=1)

from collections import Counter
roles = Counter(t["layer1"]["speaker_role"] or "unknown" for t in talks)
genres = Counter(t["layer1"]["genre"] for t in talks)
ctypes = Counter(t["layer1"]["company_type"] or "unknown" for t in talks)
review = sum(1 for t in talks if t["layer1"]["needs_review"])
elig = sum(1 for t in talks if t["layer1"]["message_eligible"])
print(f"talks={len(talks)} needs_review={review} message_eligible={elig}")
print("roles:", dict(roles)); print("genres:", dict(genres)); print("company:", dict(ctypes))
