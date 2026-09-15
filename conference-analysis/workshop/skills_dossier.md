# Skills Dossier — What Coders and Non-Coders Actually Need (corpus-grounded)

**Purpose:** information base for designing sellable workshops. Everything attributed
to corpus speakers; no outside market data yet (Argentina positioning marked as TODO).
**Sources:** 371 talks coded (extraction_A/B.json), 284 enablement-related transcript
passages across 113 talks, 235 quantitative claims.

---

## 1. The central finding about skills

The corpus converges on one structural claim: **the coder/non-coder boundary is
moving, but not disappearing.**

- [A015](https://youtu.be/gGT4ysQOdIg) (Newton, 700-person consultancy): made vibe coding a core skill for *every*
  employee incl. operations specialists — 8 hackathons → ~40% of company actively
  vibe coding; 6 hours of paired programming replaced a month of quoted contractor
  time. Open question they still wrestle with: *"how far along the engineering
  literacy spectrum can non-engineers realistically go?"*
- [B302](https://youtu.be/UcYoMg-8-L8) (Automattic, 500-person Radical Speed Month): a *product designer* shipped 3
  products in 30 days after a role-specific enablement course. Their biggest
  learning: **"engineers will need to become enablers and teachers."**
- [B056](https://youtu.be/bMjlRrWjdT0) (DoorDash): non-engineers annotate eval data and vibe-code their own tools
  — *given an API-first platform*.
- [B266](https://youtu.be/uU5Gv2h8-9g) (Anthropic): Claude Tag used heavily by non-engineers; onboarding new users
  matters enough to "teach Claude to make good assumptions."
- Counterweight: [B120](https://youtu.be/I6aiEf3aEFQ) — intelligence ≠ expertise; experts still see constraint
  violations capable models miss. [B089](https://youtu.be/Yphdry8ttAQ) — the "judgment wall": engineers instantly
  judge generated code quality; nobody has that trained judgment in new domains yet.

## 2. Skills for CODERS (ranked by corpus weight)

| # | Skill | Evidence anchor | Talks |
|---|---|---|---|
| 1 | **Directing/orchestrating agents** (multi-agent supervision, context mgmt, specialization) | "manage agents like a director manages developers"; fleet field reports | [A011](https://youtu.be/sp5ee7DaL5A), [B293](https://youtu.be/4kYl2_mqmnQ), [B081](https://youtu.be/_ehJyfHg1Vk), [B287](https://youtu.be/9arM9b7JgOo) |
| 2 | **Verification & evals discipline** | "evals, evals, evals" = #1 stack challenge in 2026 survey; "verifiers are king" | [B220](https://youtu.be/RGe6EjucbzI), [B231](https://youtu.be/VrpEyglYgeU), [B195](https://youtu.be/q2JrUKBMf0w), [B116](https://youtu.be/jHMiYtjoJfA), [B268](https://youtu.be/0vphxNt4wyk) |
| 3 | **Context/harness engineering** | harness = everything left when you remove the model; harness failures, not model failures | [B007](https://youtu.be/gxVZ_1tuuq4), [B173](https://youtu.be/BInpv7lGp1o), [B218](https://youtu.be/8qWIPUia2O8), [B287](https://youtu.be/9arM9b7JgOo) |
| 4 | **Spec-driven development & structured planning** | "what's coming back: architecture docs, clear requirements, structured planning" | [B330](https://youtu.be/IddXPepIAS4), [A017](https://youtu.be/mrWGtCPrXBc), [B325](https://youtu.be/T0HhO4YtTfE) |
| 5 | **Review of AI-generated code** (avoiding verification debt, review debt) | gains evaporate ~3 months, residue stays; PR-count metrics miss bloat | [B130](https://youtu.be/03l29gJXpCE), [B280](https://youtu.be/TJPInBjhE4Q), [B084](https://youtu.be/s-aixZYJG4c), [B104](https://youtu.be/YgEv7IQzGdM) |
| 6 | **Security & permissions awareness** | Replit-style incidents; supply-chain vetting; "generator ≠ validator" | [B229](https://youtu.be/cgimkNGNjvU), [B105](https://youtu.be/MkRYPFIMCSA), [B223](https://youtu.be/1EZdpEhwmNc), [B166](https://youtu.be/iKQ78wyJEXU) |
| 7 | **Cost/token consciousness** | tokens as first-class architectural concern; routing economics | [A008](https://youtu.be/TMOcVC9SuK4), [B321](https://youtu.be/dRmWYHuIJxM), [B140](https://youtu.be/QHBjufYK8TA), [B201](https://youtu.be/-I5W5QVAT8E) |
| 8 | **Teaching/enablement as part of the job** | "engineers will need to become enablers and teachers"; leader mandates | [B302](https://youtu.be/UcYoMg-8-L8), [A022](https://youtu.be/KEkOdSZPqQk), [B126](https://youtu.be/aeTb5BdmTTc) |
| 9 | **Resurfacing classics**: pair programming, formal methods, requirements writing | "the unlikely answers to the challenges ahead" | [A017](https://youtu.be/mrWGtCPrXBc), [A006](https://youtu.be/AZn7JZiNetA), [A001](https://youtu.be/DiQsbzCpTyo) |
| 10 | **Anti-pattern recognition** | CCA exam taught backwards from anti-patterns; design-patterns-movement analogy | [B135](https://youtu.be/Z-c11pV_uvU), [B145](https://youtu.be/-npY6XjM8CQ) |

## 3. Skills for NON-CODERS (ranked)

| # | Skill | Evidence anchor | Talks |
|---|---|---|---|
| 1 | **Conversational building (vibe coding) for real work** | 40% of a 700-person firm; designers shipping products | [A015](https://youtu.be/gGT4ysQOdIg), [B302](https://youtu.be/UcYoMg-8-L8), [B030](https://youtu.be/Qr15lGAGKpo) |
| 2 | **Role-specific tool fluency** | Automattic: every employee through a *2-week course designed for their role* | [B302](https://youtu.be/UcYoMg-8-L8), [A019](https://youtu.be/nqaHTussq5o) |
| 3 | **Judgment & taste over generation** | taste is learnable/tellable (30+ vibe-coded-app tells); discernment, not rubber-stamping | [B076](https://youtu.be/7GMKdpLsxwU), [B299](https://youtu.be/CDqzWpwkSls), [B013](https://youtu.be/v42opQpCy60) |
| 4 | **Delegation & supervision of agents** (knowing what to ask, when to check) | "understanding is the new bottleneck"; librarian/trust patterns | [B289](https://youtu.be/WkBPX-oDMnA), [B288](https://youtu.be/YZQsWVeN3rE), [B249](https://youtu.be/L3RuP_q8Bwc) |
| 5 | **Context curation** (feeding the org's shared brain: docs, data models, lore repos) | "your moat is your data model"; lore repository as superpower | [B212](https://youtu.be/jt1Pbr_n6oU), [A021](https://youtu.be/n1_1FxpUYug), [B027](https://youtu.be/0uC6u0lJJl4) |
| 6 | **Security hygiene for non-engineers** | skill supply-chain vetting; approval inversion patterns | [B166](https://youtu.be/iKQ78wyJEXU), [B035](https://youtu.be/vGn6N4-bxBY) |
| 7 | **Emotional regulation of adoption** ("hold multiple feelings simultaneously") | excitement+anxiety as adoption skill; "AI psychosis" normalized | [A024](https://youtu.be/bXtH2FDbNlQ), [B292](https://youtu.be/xUnRQ9vLXxo) |
| 8 | **Citizen-automation limits** (when to stop, when to call an engineer) | Newton's open question; escalation boundaries | [A015](https://youtu.be/gGT4ysQOdIg), [B042](https://youtu.be/dQ-_i1tZiws) |

## 4. Organizational skills (what the buyer's company needs around the workshops)

These are what differentiate a sold workshop from a repeated one:

1. **Leadership behavior > tool availability** — Cisco: unlimited tokens changed
   nothing until 100 leaders personally shipped ([A022](https://youtu.be/KEkOdSZPqQk)). **Workshop implication: sell
   a leader-track, not just a user-track.**
2. **Phased adoption models** — John Deere: Curiosity → Learning → Advocacy, moving
   innovators and majority *simultaneously* ([A010](https://youtu.be/XRYFp-fGQcU)); five-stages-to-AI-native maps ([A023](https://youtu.be/C7McdiwHNKY)).
3. **Enablement formats that worked** (evidence-backed, reusable as workshop designs):
   - Hackathon series (8 → 40% active, CEO to new joiners) — [A015](https://youtu.be/gGT4ysQOdIg)
   - 2-week role-specific enablement course — [B302](https://youtu.be/UcYoMg-8-L8)
   - 3-day ship summits w/ pre-provisioned environments (198 workspaces <30s, 3,000
     pushes) — [A019](https://youtu.be/nqaHTussq5o)
   - Leader coding mandates w/ measurement (100 leaders, 1 quarter) — [A022](https://youtu.be/KEkOdSZPqQk)
   - Anti-pattern-first curriculum (CCA backwards) — [B135](https://youtu.be/Z-c11pV_uvU)
4. **Tolerating noisy experimentation** — stated twice independently ([A015](https://youtu.be/gGT4ysQOdIg), [A019](https://youtu.be/nqaHTussq5o)) as
   the precondition buyers usually get wrong.
5. **Governance of skills/knowledge** — build→share→govern gradient; governance is
   the rarest step ([B049](https://youtu.be/M05vON8i0aI), [B166](https://youtu.be/iKQ78wyJEXU)).

## 5. Adoption metrics the corpus offers (proof points for sales material)

- 93% weekly AI usage; 92% of devs with AI in 80%+ of contributions (John Deere, [A010](https://youtu.be/XRYFp-fGQcU))
- 4.5x median deployment velocity for teams that *deliberately changed practice* vs
  <3x for tool-only teams (Amazon 50-team study, [B053](https://youtu.be/pqlWNihgdjI) — "the teams differed, not the tool")
- 40% active vibe-coding in 6 months (Newton, [A015](https://youtu.be/gGT4ysQOdIg))
- 20x shipping pace via evals+simulation (Nubank/Snowglobe, [B170](https://youtu.be/KMR_RBoCa4M))
- 90-day core platform replacement by 2 engineers, $500K saved ([A021](https://youtu.be/n1_1FxpUYug))
- 82% outcome reduction reported by FDE deployments ([B176](https://youtu.be/RVxym6mmIns))

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
