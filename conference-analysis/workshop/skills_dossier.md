# Skills Dossier — What Coders and Non-Coders Actually Need (corpus-grounded)

**Purpose:** information base for designing sellable workshops. Everything attributed
to corpus speakers; no outside market data yet (Argentina positioning marked as TODO).
**Sources:** 371 talks coded (extraction_A/B.json), 284 enablement-related transcript
passages across 113 talks, 235 quantitative claims.

---

## 1. The central finding about skills

The corpus converges on one structural claim: **the coder/non-coder boundary is
moving, but not disappearing.**

- A015 (Newton, 700-person consultancy): made vibe coding a core skill for *every*
  employee incl. operations specialists — 8 hackathons → ~40% of company actively
  vibe coding; 6 hours of paired programming replaced a month of quoted contractor
  time. Open question they still wrestle with: *"how far along the engineering
  literacy spectrum can non-engineers realistically go?"*
- B302 (Automattic, 500-person Radical Speed Month): a *product designer* shipped 3
  products in 30 days after a role-specific enablement course. Their biggest
  learning: **"engineers will need to become enablers and teachers."**
- B056 (DoorDash): non-engineers annotate eval data and vibe-code their own tools
  — *given an API-first platform*.
- B266 (Anthropic): Claude Tag used heavily by non-engineers; onboarding new users
  matters enough to "teach Claude to make good assumptions."
- Counterweight: B120 — intelligence ≠ expertise; experts still see constraint
  violations capable models miss. B089 — the "judgment wall": engineers instantly
  judge generated code quality; nobody has that trained judgment in new domains yet.

## 2. Skills for CODERS (ranked by corpus weight)

| # | Skill | Evidence anchor | Talks |
|---|---|---|---|
| 1 | **Directing/orchestrating agents** (multi-agent supervision, context mgmt, specialization) | "manage agents like a director manages developers"; fleet field reports | A011, B293, B081, B287 |
| 2 | **Verification & evals discipline** | "evals, evals, evals" = #1 stack challenge in 2026 survey; "verifiers are king" | B220, B231, B195, B116, B268 |
| 3 | **Context/harness engineering** | harness = everything left when you remove the model; harness failures, not model failures | B007, B173, B218, B287 |
| 4 | **Spec-driven development & structured planning** | "what's coming back: architecture docs, clear requirements, structured planning" | B330, A017, B325 |
| 5 | **Review of AI-generated code** (avoiding verification debt, review debt) | gains evaporate ~3 months, residue stays; PR-count metrics miss bloat | B130, B280, B084, B104 |
| 6 | **Security & permissions awareness** | Replit-style incidents; supply-chain vetting; "generator ≠ validator" | B229, B105, B223, B166 |
| 7 | **Cost/token consciousness** | tokens as first-class architectural concern; routing economics | A008, B321, B140, B201 |
| 8 | **Teaching/enablement as part of the job** | "engineers will need to become enablers and teachers"; leader mandates | B302, A022, B126 |
| 9 | **Resurfacing classics**: pair programming, formal methods, requirements writing | "the unlikely answers to the challenges ahead" | A017, A006, A001 |
| 10 | **Anti-pattern recognition** | CCA exam taught backwards from anti-patterns; design-patterns-movement analogy | B135, B145 |

## 3. Skills for NON-CODERS (ranked)

| # | Skill | Evidence anchor | Talks |
|---|---|---|---|
| 1 | **Conversational building (vibe coding) for real work** | 40% of a 700-person firm; designers shipping products | A015, B302, B030 |
| 2 | **Role-specific tool fluency** | Automattic: every employee through a *2-week course designed for their role* | B302, A019 |
| 3 | **Judgment & taste over generation** | taste is learnable/tellable (30+ vibe-coded-app tells); discernment, not rubber-stamping | B076, B299, B013 |
| 4 | **Delegation & supervision of agents** (knowing what to ask, when to check) | "understanding is the new bottleneck"; librarian/trust patterns | B289, B288, B249 |
| 5 | **Context curation** (feeding the org's shared brain: docs, data models, lore repos) | "your moat is your data model"; lore repository as superpower | B212, A021, B027 |
| 6 | **Security hygiene for non-engineers** | skill supply-chain vetting; approval inversion patterns | B166, B035 |
| 7 | **Emotional regulation of adoption** ("hold multiple feelings simultaneously") | excitement+anxiety as adoption skill; "AI psychosis" normalized | A024, B292 |
| 8 | **Citizen-automation limits** (when to stop, when to call an engineer) | Newton's open question; escalation boundaries | A015, B042 |

## 4. Organizational skills (what the buyer's company needs around the workshops)

These are what differentiate a sold workshop from a repeated one:

1. **Leadership behavior > tool availability** — Cisco: unlimited tokens changed
   nothing until 100 leaders personally shipped (A022). **Workshop implication: sell
   a leader-track, not just a user-track.**
2. **Phased adoption models** — John Deere: Curiosity → Learning → Advocacy, moving
   innovators and majority *simultaneously* (A010); five-stages-to-AI-native maps (A023).
3. **Enablement formats that worked** (evidence-backed, reusable as workshop designs):
   - Hackathon series (8 → 40% active, CEO to new joiners) — A015
   - 2-week role-specific enablement course — B302
   - 3-day ship summits w/ pre-provisioned environments (198 workspaces <30s, 3,000
     pushes) — A019
   - Leader coding mandates w/ measurement (100 leaders, 1 quarter) — A022
   - Anti-pattern-first curriculum (CCA backwards) — B135
4. **Tolerating noisy experimentation** — stated twice independently (A015, A019) as
   the precondition buyers usually get wrong.
5. **Governance of skills/knowledge** — build→share→govern gradient; governance is
   the rarest step (B049, B166).

## 5. Adoption metrics the corpus offers (proof points for sales material)

- 93% weekly AI usage; 92% of devs with AI in 80%+ of contributions (John Deere, A010)
- 4.5x median deployment velocity for teams that *deliberately changed practice* vs
  <3x for tool-only teams (Amazon 50-team study, B053 — "the teams differed, not the tool")
- 40% active vibe-coding in 6 months (Newton, A015)
- 20x shipping pace via evals+simulation (Nubank/Snowglobe, B170)
- 90-day core platform replacement by 2 engineers, $500K saved (A021)
- 82% outcome reduction reported by FDE deployments (B176)

## 6. What the corpus does NOT answer (needs external input before content build)

1. **Argentina/LatAm market specifics**: pricing benchmarks, corporate training
   market, spanish/bilingual content norms, local compliance context. Corpus is
   US/UK-centric.
2. **Which verticals to target**: corpus suggests health/finance/gov are the
   regulated buyers with money, but LatAm composition differs.
3. **Live-tool versions**: corpus is model/tool-agnostic-ish; workshop needs a
   concrete stack decision (Claude Code / Cursor / etc.).
4. **Depth calibration**: corpus says non-engineer ceiling is an *open question*
   even for practitioners — workshops must position honestly (enablement, not
   engineer-replacement).

## 7. Candidate workshop modules (raw material, to be shaped later)

From the evidence: (a) leader track: mandate design + metrics; (b) coder track:
directing agents, evals, review debt, security; (c) non-coder track: vibe coding
for role, judgment/taste, context curation; (d) format options: hackathon series,
2-week role course, 3-day ship summit, anti-pattern clinic.
