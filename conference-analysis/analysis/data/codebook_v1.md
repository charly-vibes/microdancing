# Codebook v1 — Pass 1 Output

Built from: full digest of 385 titles (+ abstracts for corpus A) + transcript
openings of 10 stratified talks (4 A, 6 B). Free-coded bottom-up; no external
frameworks imposed. Themes emerge from the corpus itself.

## 1. Topic taxonomy (20 topics)

| Code | Topic | Corpus signal (from digest) |
|---|---|---|
| ORG | Org transformation & AI-native orgs | strong in A (org redesign mandates); present in B |
| REL | Agent reliability: evals, observability | heavy in B; A mentions but rarely centers |
| SEC | Agent security: permissions, sandboxing, supply chain | B-heavy; A light |
| COM | Agentic commerce & payments (x402, wallets, MCP) | B-only cluster |
| CODE | Coding agents in practice: review, brownfield, workflows | both; A = enterprise adoption angle, B = tooling angle |
| CTX | Context & harness engineering | B-dominant; A nearly absent as topic |
| LEARN | Memory & continual learning | B-only cluster (10+ talks) |
| GTM | Go-to-market / sales AI | B-only cluster (10 talks) |
| MM | Voice, video, generative UI/UX | B-only cluster |
| FDE | Forward-deployed engineering & vertical agents | B-only cluster (8 talks) |
| MODEL | Model research: post-training, RL, data curation | B-only cluster |
| EDGE | Local/edge/on-device models | B-only |
| SKILL | Skills & standardization (MCP, protocols) | B-dominant; A touches |
| CULT | Adoption culture & psychology | A-dominant (explicit theme); B has keynote moments |
| COST | Token/cost economics | both, more B |
| FUT | Future pronouncements ("X is dead", "the end of Y") | both — B: technical claims; A: org/work claims |
| REG | Regulated-industry deployment (health, finance, defense) | both; A = finance/defense, B = health |
| FV | Formal verification & determinism | A (Meijer) + B (Lean4, verifiable envs) |
| BENCH | Benchmarks & their critique | B-heavy |
| RUNTIME | Agent runtime/sandbox infra | B-only |

Corpus-unique clusters (pass-1 residue): COM, GTM, LEARN, MODEL, FDE, MM, EDGE,
RUNTIME — all B-side. A-unique: none fully (A themes are subsets of ORG, CULT,
FUT, REG).

## 2. Message frames (normative stance patterns observed in titles/openings)

| Code | Frame | Example |
|---|---|---|
| MF1 | DevOps-history analogy | A012 "vibe coding will reshape orgs like DevOps did, 100x" |
| MF2 | Standardization claim ("X is the new Y") | B240 "Skills are the new SDKs", B231 "verifiers are king" |
| MF3 | Threat/urgency ("you're not ready", "X is dying") | A002 "pivot nobody's ready for", B137 "Open Source Is Dead" |
| MF4 | War story / experience report | B293 (fleet broke), A021 (90-day platform swap) |
| MF5 | Product-pattern / how-to-build pitch | B002 (Vercel AI SDK), B043 (Adobe demo) |
| MF6 | Culture-first argument ("it's not tech, it's people") | A024, A022, A016 |
| MF7 | Manual/listicle format ("N things", "field guide") | B310, B282, B257 |

## 3. Evidence-style codes (per spec §2.2)

- WAR: first-hand experience at named employer
- CUST: customer/client data cited
- SURV: survey or aggregate data
- THEORY: framework/principles argument
- PITCH: product demonstration
- OPIN: opinion without grounding

Pass-1 correction to spec: war stories are NOT corpus-A-exclusive (B293 KRAFTON,
B205 ZS are war stories). Evidence-style comparison is still valid but must be
reported as distributions, not binary corpus traits.

## 4. Extraction schema (pass 2, per talk)

```json
{
  "id": "...", "conference": "A|B",
  "topics": [{"code": "REL", "salience": "primary|secondary|touched"}],
  "claims": [{"text": "...", "topic": "REL", "evidence": "WAR|CUST|SURV|THEORY|PITCH|OPIN",
              "numbers": [{"value": 0.94, "unit": "%", "context": "..."}],
              "normative": true|false}],
  "message": {"recommendations": ["..."], "framing": ["MF3"], "evidence_style": "WAR"},
  "tech": [{"name": "MCP", "category": "protocol"}],
  "genre_refined": "keynote|case-study|demo|workshop|panel|remarks|promo|remote-talk",
  "selling_intent": "talk|hybrid|pitch",
  "host_intro_skipped": true  // corpus A: first ~60-90s is host intro
}
```

## 5. Pass-1 grounding notes

- Corpus A transcripts embed host introductions (60–90s) before speaker content — extraction must skip them.
- B includes remote-recorded talks (B310: speaker not on site, no audience) — genre `remote-talk`.
- B titles are message-dense (normative claims in titles); A titles are neutral + speaker name. Title-sentiment is itself a corpus-contrasting feature to quantify.
- B workshops exist ("Full Workshop: ...") — separate genre.
- 14 B videos private; excluded from all rates.
- B043-style digest labels vs transcript index prefixes: consistent, IDs are the join key.

## 6. Known limitations of codebook v1

- Derived largely from titles (B) + abstracts (A); pass 2 may surface themes
  invisible in titles (esp. inside B demos).
- Themes not mutually exclusive; a talk averages ~2–3 topics with salience.
- Speaker-role data for B remains thin (221 unspecified) — role-crosstabs are
  A-only until pass 2 mines B descriptions/bios.
