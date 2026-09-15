# Skills Dossier Addendum — Research Labs

**Purpose:** extend the skills analysis to research institutions (universities,
CONICET-style public research, biotech/agtech R&D, corporate labs). Grounded in the
same corpus; research content is ~8% of corpus B plus A001 (formal verification) —
smaller but dense cluster. 284-passage mining surfaced 100 talks with
research-relevant passages; deepest: B247, B155, B074, B119, B161, B263.

---

## 1. What the corpus says about AI in research

Five distinct clusters:

1. **Autoresearch / agent scientists** — agents running the scientific method loop
   (observe → hypothesize → implement → measure): B247 (Radicait: "decomposing the
   2–10 year research process into steps where each is fundamental"), B263 (Weco's
   Aiden: 7 merged records in OpenAI's training competition, 2× any human), B161
   (Socher: "compresses enlightenment→moonlanding again", Popper loop as agent swarm
   across medicine/economics/astrophysics).
2. **Verifiable environments for domains without clean verifiers** — B155 (LatchBio:
   spatial biology as "verifiable substrate", 2–6TB per run; task prompt + deterministic
   Python grader), B158 (RL without verifiable rewards), B156 (taste spectrum:
   things that verify cleanly ↔ pure preference).
3. **Agent collaboration platforms for open science** — B074 (Einstein Arena:
   agent-only, human-expert-curated open problems from recent papers; "DS Gym" for
   data-scientist agents).
4. **Democratization of the research skill itself** — B119 (Hooker, Adaption Labs):
   *"people did a computer science PhD to learn the tools to get to the question, and
   now you can just get to the question"*; frontier-training knowledge travels by
   apprenticeship (<5,000 people), and agents widen that funnel.
5. **Where LLMs hit walls in research contexts** — B277 (Phaidra: "you cannot solve a
   combinatorial engineering problem with a next-token predictor", 500k sensors),
   B089 (the judgment wall: no trained taste for domain outputs), B343 (eval
   contamination: Hamilton persona rated high by judges that read its own myth),
   B247 (agents "saturate" on open-ended long-horizon tasks without structure).

## 2. Skills for RESEARCHERS (scientists, postdocs, PhD students — often code-adjacent, rarely software-engineered)

| # | Skill | Evidence anchor |
|---|---|---|
| 1 | **Framing research questions as agent tasks** — decomposing a 2–10 yr agenda into agent-sized, verifiable steps | B247 (explicit loop), B155 ("every step interpreted against the experimental design") |
| 2 | **Literature-scale agents with memory** — corpus review, cross-paper synthesis, personal research memory | B122 (memory boundary: matters only beyond context window), B336 (10,994 notes → memory), B118 (voice → structured KB) |
| 3 | **Building verifiable graders for their own domain** — turning protocols/metrics into deterministic checkers | B155 (deterministic Python grader per task), B158, B187 (clinical insight → machine-readable evals) |
| 4 | **Provenance & reproducibility discipline for agent outputs** — sources, replay, evidence chains | B206 (synthesized fact lost its 3 sources — clinical example), B190 (trace reconstruction = experiment replay), B281 (done = evidence + verifier + risk owner) |
| 5 | **Eval-gaming awareness** (contamination, benchmaxxing, judge drift) | B343, B145, B185, B157 |
| 6 | **Data structuring before agents** — unstructured lab records → structured corpus | B332, B087 (the "don't be data poor" fax problem, in every lab), B212 |
| 7 | **Taste/quality control of AI writing** — slop detection as a trainable skill | B156, B076, B013 |
| 8 | **Privacy/IP hygiene for sensitive data** | B226, B166, B087 |

**The Hooker thesis for marketing:** the PhD's tool-learning phase is compressing —
*"scientists just skipped the questions"* — which is exactly the pitch for
researcher-facing workshops: not "learn to code", but **"get to your question
faster"**.

## 3. Skills for RESEARCH SOFTWARE ENGINEERS / lab technical staff

| # | Skill | Evidence anchor |
|---|---|---|
| 1 | **Environment & harness building** (sandboxed, deterministic, domain-faithful) | B155, B153 ("real tasks aren't tidy — a database going down at scale is the curriculum"), B196 |
| 2 | **Long-horizon agent infrastructure** — memory, persistence, rollback, budgets | B122, B147, B216, B213 (log-is-the-agent rollback), B254 |
| 3 | **Physical-instrument & sensor integration** (where LLM intuition breaks) | B277, B236 ("the other physics of agent harnesses") |
| 4 | **Ontologies/semantic layers for domain data** | B209, B215, B235 |
| 5 | **Multi-agent orchestration for research pipelines** (and knowing when to kill it) | B205 (killed pipeline: right cause, wrong action), B172 (ALPHALAB), B283 (39 agents, no framework) |
| 6 | **Eval design for non-verifiable domains** | B158, B156, B272 (measurement theory, IRT), B191 (video judge drift) |

## 4. Skills for PIs / lab directors

Same as corporate leaders, adapted: **mandate design** (A022 — leaders shipping
personally), **phased adoption** (A010), **tolerance for noisy experimentation**
(A015/A019), **moat thinking** — data model + tacit knowledge as the lab's durable
asset (B212), **funding alignment**: "build for the memo, not the demo" (B163 —
AI-generated decks are confidently wrong; funders need evidence chains, which maps
directly onto grant reporting).

## 5. Proof points from the corpus (research-adjacent)

- Agent finished with 7 merged records in OpenAI's Parameter Golf — **2× the best
  human** competitor (B263)
- 200M+ clinical conversations deployed (B091) — regulated-domain scale exists
- ~82% outcome reduction from agent deployment measured pre/post (B176)
- zlib rewritten in Lean: 32,000 lines of machine-checked proof (B050) — verification
  at research-grade rigor
- Einstein Arena: agents collaborating "in the wild" on curated open scientific
  problems (B074)

## 6. Candidate workshop modules for research labs (raw material)

1. **"Get to your question faster"** (researcher track): literature agents, research
   memory systems, prompt→hypothesis→experiment decomposition. Non-coder friendly.
2. **"Your lab as a verifiable environment"** (RSE track): turning protocols into
   graders, provenance/replay infrastructure, eval design for fuzzy domains.
3. **"The judgment wall" clinic** (PI track): where agents saturate, how to review
   agent-generated science, eval-gaming detection, data-moat strategy.
4. **Format options (evidence-backed):** hackathon series (A015), role-specific
   2-week course (B302), anti-pattern-first curriculum (B135), ship-summit with
   pre-provisioned compute (A019 — labs have their own compute, an advantage).

## 7. Argentina mapping — HYPOTHESES ONLY (external input needed)

Corpus gives no LatAm data. Plausible anchors to verify: CONICET/CNEA/INTA/INTI,
university labs (UBA, UNLP, Balseiro), biotech & agtech (Bioceres-era ecosystem),
pharma (Gador, Bagó, Roemmers), energy (YPF-Tecnología), plus public-sector data
agencies. Open questions: budget source (grants vs corporate), Spanish-first vs
bilingual content, compute availability (affects format choice — ship-summit model
assumes provisioned environments), and whether the buyer is the lab director, the
grant office, or the ministry.

## 8. Honest limits

- Research is a minority cluster in an enterprise/engineering corpus; these skills
  are inferred from the closest analogues, not from research-lab case studies
  (except B074/B155/B247/B263, which are genuinely research-domain).
- No corpus evidence on grant dynamics, publication incentives, or academic adoption
  culture — the biggest actual barriers in research labs.
