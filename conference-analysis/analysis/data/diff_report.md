# Comparative Diff Report — Two AI Conference Playlists

**Generated:** after pass-2 extraction (all message-eligible talks coded)
**Method caveats (read first):**
- Corpus A (n=23 message-eligible of 27; 4 remarks excluded): coded from full abstracts + 4 transcript openings. Claims = what the abstract states the speaker says.
- Corpus B (n=343 message-eligible of 358; 14 private + 1 promo excluded): coded from titles + first ~380 chars of AI Engineer's narrative descriptions. Deep but lead-level.
- All claims are attributions, not facts. Corpus sizes differ 27 vs 358 — rates, never counts.
- Confounds (per spec §5): different audiences (enterprise leaders vs AI engineers), event scope, program curation. Conclusions scoped to *these two programs as curated*.

---

## 1. Content: what each conference talks about

| Topic | A rate | B rate | Delta |
|---|---:|---:|---|
| ORG (org transformation) | **78%** | 18% | +60pp — A's center of gravity |
| CULT (adoption culture/psychology) | **43%** | 3% | +40pp — A's second pillar |
| CODE (coding agents in practice) | 39% | 28% | shared, different sense (§3) |
| FUT (future pronouncements) | 30% | 11% | shared |
| REG (regulated industries) | 4% | 12% | B: health-vertical cluster |
| REL (evals/reliability) | 0% | **22%** | B-only as primary topic |
| CTX (context/harness) | 0% | **18%** | B-only |
| SEC (agent security) | 4% | 16% | B-dominant |
| MODEL (post-training/RL) | 0% | 13% | B-only |
| RUNTIME / MM / COST | 0% | 12% each | B-only |
| B-unique clusters | — | SKILL 6%, LEARN 7%, BENCH 5%, EDGE 3%, GTM 4%, COM 3%, FDE 3% | B-only |

**Bottom-up result:** zero A-unique themes; **eleven B-unique clusters**. A's content is a proper subset of B's — but A's subset is *concentrated* (78% org-transformation) while B is *distributed* across 20 topics.

**Shared topics, different sense:**
- **CODE**: A = enterprise war stories about adopting agents on brownfield estates; B = building review pipelines, benchmarks, agent factories.
- **ORG**: A = "how to convert your org" (mandates, culture, leadership); B = "what broke when we ran agents at scale" (org as failure surface).
- **FUT**: A = claims about *organizations* (roles, leadership, structure dying); B = claims about *technology* (base models dead, open source dead, pipelines dead).
- **"AI-native"**: A = a property of an organization; B (e.g. B136, B218) = a property of software architecture.
- **"Evals"**: A barely uses the word (1 talk); B treats it as the discipline of the field ("evals, evals, evals" survey; 22% of corpus). Same word, entirely different weight.

## 2. Message: how they say it

| Frame | A | B |
|---|---:|---:|
| MF4 war story / experience report | **52%** | **53%** |
| MF6 culture-first ("it's people, not tech") | **30%** | 4% |
| MF3 threat/urgency ("you're not ready", "X is dead") | 17% | 15% |
| MF7 manual/listicle | 17% | 5% |
| MF5 product-pattern pitch | 9% | **13%** |
| MF2 "X is the new Y" standardization | 9% | 11% |
| MF1 DevOps-analogy | 13% | ~0% |

**Finding:** war stories dominate *both* — the shared rhetorical DNA is the practitioner report. The conferences diverge on the second frame: A pivots to culture and DevOps-historicism, B pivots to product patterns and standardization claims.

**Evidence style** (dominant per talk):

| Style | A | B |
|---|---:|---:|
| WAR (personal experience) | **57%** | 14% |
| CUST (company/customer data) | 4% | **39%** |
| THEORY | 26% | 23% |
| PITCH | 4% | 18% |
| OPIN | 4% | 5% |
| SURV | 4% | 1% |

A's stories are *personal* ("I led this team"), B's are *corporate-documented* ("our 2M users", "$12M revenue, 50x ROI"). Same genre label, different evidentiary posture — and B's is verifiable-claim-dense (235 quantitative claims cataloged in `data_points.json`: 25 A / 210 B).

**Selling intent:** similar overall (A 26% hybrid/pitch vs B 27% hybrid) — but B's pitch share concentrates in vendor-origin talks, A's in consulting/tool hybrids.

## 3. Traction (within-conference only — NOT comparable across playlists)

Median views by primary topic, within each playlist:
- **A:** flat (50–86 views) — too small to differentiate.
- **B:** FDE (10.8k) > FUT (9.2k) > CTX/SKILL/CODE/ORG (6.4–7.2k) >> SEC (1.8k), MODEL (2.0k), REG (1.1k), BENCH (1.8k).
- Reading: B's *audience* rewards forward-deployed practice, future claims, and building topics; punishes security, research, and regulated-industry content. A's audience rewards everything roughly equally (or the sample is too small to say — likely both).

## 4. Duplicate-speaker control

A004 ≈ B328 and A004 ≈ B342 (Angie Jones, same mandate talk delivered to both conferences — A004 title vs B328/B342 near-identical abstracts). Excluding them does not change any rate by more than ~1pp (B328/B342 are 2/343 ≈ 0.6%). Steve Yegge also appears in both (A002 vs B230) with *different* talks — org-pivot story vs security story; not a duplication effect.

## 5. Answer to the research question (scoped, per confounds)

**Yes — these two programs differ sharply in content and measurably in message.**
1. **Content:** A programs for transformation (78% org, 43% culture); B programs for construction (a 20-topic technical spread; 11 clusters A never touches).
2. **Message:** both led by war stories, but A's backup move is cultural/personal ("it's about people, leadership, feelings") while B's is product and standardization ("this is the new primitive/SDK/protocol").
3. **Evidence:** A argues from personal tenure; B argues from company metrics.
4. **Shared blind spots:** formal verification is near-zero in both (4% A, 2% B); agent security is underweighted *relative to its talk-count* at B by its own audience (1.8k median views, lowest tier).

## 6. Limitations
- B coded at lead-abstract depth; deep themes inside talks may be missed (systematic check: 10 grounding openings were consistent with leads).
- A n=23; A percentages carry ±20pp uncertainty at these rates. Treat A figures as directional.
- AI Engineer house-style descriptions are written to hook; their frame distribution may partly reflect channel editorial voice, not speakers.
- Traction analysis confounded by channel reach and upload timing; within-conference only.
