# Skills Dossier Addendum — Research Labs

**Purpose:** extend the skills analysis to research institutions (universities,
CONICET-style public research, biotech/agtech R&D, corporate labs). Grounded in the
same corpus; research content is ~8% of corpus B plus [A001](https://youtu.be/DiQsbzCpTyo) (formal verification) —
smaller but dense cluster. 284-passage mining surfaced 100 talks with
research-relevant passages; deepest: [B247](https://youtu.be/XLEYtv3cMlw), [B155](https://youtu.be/3ZMUiFaQ3qg), [B074](https://youtu.be/mMNkdYnIVC4), [B119](https://youtu.be/XEd_SRVHBgU), [B161](https://youtu.be/pWXUkLP9uWM), [B263](https://youtu.be/iCj_ATyThvc).

---

## 1. What the corpus says about AI in research

Five distinct clusters:

1. **Autoresearch / agent scientists** — agents running the scientific method loop
   (observe → hypothesize → implement → measure): [B247](https://youtu.be/XLEYtv3cMlw) (Radicait: "decomposing the
   2–10 year research process into steps where each is fundamental"), [B263](https://youtu.be/iCj_ATyThvc) (Weco's
   Aiden: 7 merged records in OpenAI's training competition, 2× any human), [B161](https://youtu.be/pWXUkLP9uWM)
   (Socher: "compresses enlightenment→moonlanding again", Popper loop as agent swarm
   across medicine/economics/astrophysics).
2. **Verifiable environments for domains without clean verifiers** — [B155](https://youtu.be/3ZMUiFaQ3qg) (LatchBio:
   spatial biology as "verifiable substrate", 2–6TB per run; task prompt + deterministic
   Python grader), [B158](https://youtu.be/AQv3qRCG6Gw) (RL without verifiable rewards), [B156](https://youtu.be/lCBf9slCanI) (taste spectrum:
   things that verify cleanly ↔ pure preference).
3. **Agent collaboration platforms for open science** — [B074](https://youtu.be/mMNkdYnIVC4) (Einstein Arena:
   agent-only, human-expert-curated open problems from recent papers; "DS Gym" for
   data-scientist agents).
4. **Democratization of the research skill itself** — [B119](https://youtu.be/XEd_SRVHBgU) (Hooker, Adaption Labs):
   *"people did a computer science PhD to learn the tools to get to the question, and
   now you can just get to the question"*; frontier-training knowledge travels by
   apprenticeship (<5,000 people), and agents widen that funnel.
5. **Where LLMs hit walls in research contexts** — [B277](https://youtu.be/EUsPvBeIx70) (Phaidra: "you cannot solve a
   combinatorial engineering problem with a next-token predictor", 500k sensors),
   [B089](https://youtu.be/Yphdry8ttAQ) (the judgment wall: no trained taste for domain outputs), [B343](https://youtu.be/IJXjTLPzvAU) (eval
   contamination: Hamilton persona rated high by judges that read its own myth),
   [B247](https://youtu.be/XLEYtv3cMlw) (agents "saturate" on open-ended long-horizon tasks without structure).

## 2. Skills for RESEARCHERS (scientists, postdocs, PhD students — often code-adjacent, rarely software-engineered)

| # | Skill | Evidence anchor |
|---|---|---|
| 1 | **Framing research questions as agent tasks** — decomposing a 2–10 yr agenda into agent-sized, verifiable steps | [B247](https://youtu.be/XLEYtv3cMlw) (explicit loop), [B155](https://youtu.be/3ZMUiFaQ3qg) ("every step interpreted against the experimental design") |
| 2 | **Literature-scale agents with memory** — corpus review, cross-paper synthesis, personal research memory | [B122](https://youtu.be/R3-anFK1YM8) (memory boundary: matters only beyond context window), [B336](https://youtu.be/ZRM_TfEZcIo) (10,994 notes → memory), [B118](https://youtu.be/I3bpdgFJCUY) (voice → structured KB) |
| 3 | **Building verifiable graders for their own domain** — turning protocols/metrics into deterministic checkers | [B155](https://youtu.be/3ZMUiFaQ3qg) (deterministic Python grader per task), [B158](https://youtu.be/AQv3qRCG6Gw), [B187](https://youtu.be/O72p-rBb2bA) (clinical insight → machine-readable evals) |
| 4 | **Provenance & reproducibility discipline for agent outputs** — sources, replay, evidence chains | [B206](https://youtu.be/H7puB0RwJMM) (synthesized fact lost its 3 sources — clinical example), [B190](https://youtu.be/Ib5t2RLtxvM) (trace reconstruction = experiment replay), [B281](https://youtu.be/7P0elyLIxXo) (done = evidence + verifier + risk owner) |
| 5 | **Eval-gaming awareness** (contamination, benchmaxxing, judge drift) | [B343](https://youtu.be/IJXjTLPzvAU), [B145](https://youtu.be/-npY6XjM8CQ), [B185](https://youtu.be/ZyIoTOAbRfs), [B157](https://youtu.be/jWq-aZIU0kM) |
| 6 | **Data structuring before agents** — unstructured lab records → structured corpus | [B332](https://youtu.be/-x5GEVnkuRw), [B087](https://youtu.be/XAsb7MIAzm8) (the "don't be data poor" fax problem, in every lab), [B212](https://youtu.be/jt1Pbr_n6oU) |
| 7 | **Taste/quality control of AI writing** — slop detection as a trainable skill | [B156](https://youtu.be/lCBf9slCanI), [B076](https://youtu.be/7GMKdpLsxwU), [B013](https://youtu.be/v42opQpCy60) |
| 8 | **Privacy/IP hygiene for sensitive data** | [B226](https://youtu.be/IvE8n-ylFYY), [B166](https://youtu.be/iKQ78wyJEXU), [B087](https://youtu.be/XAsb7MIAzm8) |

**The Hooker thesis for marketing:** the PhD's tool-learning phase is compressing —
*"scientists just skipped the questions"* — which is exactly the pitch for
researcher-facing workshops: not "learn to code", but **"get to your question
faster"**.

## 3. Skills for RESEARCH SOFTWARE ENGINEERS / lab technical staff

| # | Skill | Evidence anchor |
|---|---|---|
| 1 | **Environment & harness building** (sandboxed, deterministic, domain-faithful) | [B155](https://youtu.be/3ZMUiFaQ3qg), [B153](https://youtu.be/zkX03APVj0M) ("real tasks aren't tidy — a database going down at scale is the curriculum"), [B196](https://youtu.be/jRCpXUjz4CI) |
| 2 | **Long-horizon agent infrastructure** — memory, persistence, rollback, budgets | [B122](https://youtu.be/R3-anFK1YM8), [B147](https://youtu.be/2aS7aKoXn64), [B216](https://youtu.be/9QebvrrY3KY), [B213](https://youtu.be/khVX_BUnEwU) (log-is-the-agent rollback), [B254](https://youtu.be/bZISsg7H7DA) |
| 3 | **Physical-instrument & sensor integration** (where LLM intuition breaks) | [B277](https://youtu.be/EUsPvBeIx70), [B236](https://youtu.be/bUJgirn4_yc) ("the other physics of agent harnesses") |
| 4 | **Ontologies/semantic layers for domain data** | [B209](https://youtu.be/Sir59K8ZDPU), [B215](https://youtu.be/VGN22pPpb-8), [B235](https://youtu.be/B8l81jhvHbI) |
| 5 | **Multi-agent orchestration for research pipelines** (and knowing when to kill it) | [B205](https://youtu.be/u6jJcIFDLE4) (killed pipeline: right cause, wrong action), [B172](https://youtu.be/kiqubc5b5Yo) (ALPHALAB), [B283](https://youtu.be/jtzh-GBXBWc) (39 agents, no framework) |
| 6 | **Eval design for non-verifiable domains** | [B158](https://youtu.be/AQv3qRCG6Gw), [B156](https://youtu.be/lCBf9slCanI), [B272](https://youtu.be/O3FEoMYvUf8) (measurement theory, IRT), [B191](https://youtu.be/b_PmGocP4rc) (video judge drift) |

## 4. Skills for PIs / lab directors

Same as corporate leaders, adapted: **mandate design** ([A022](https://youtu.be/KEkOdSZPqQk) — leaders shipping
personally), **phased adoption** ([A010](https://youtu.be/XRYFp-fGQcU)), **tolerance for noisy experimentation**
([A015](https://youtu.be/gGT4ysQOdIg)/[A019](https://youtu.be/nqaHTussq5o)), **moat thinking** — data model + tacit knowledge as the lab's durable
asset ([B212](https://youtu.be/jt1Pbr_n6oU)), **funding alignment**: "build for the memo, not the demo" ([B163](https://youtu.be/tJFjeMBKbIY) —
AI-generated decks are confidently wrong; funders need evidence chains, which maps
directly onto grant reporting).

## 5. Proof points from the corpus (research-adjacent)

- Agent finished with 7 merged records in OpenAI's Parameter Golf — **2× the best
  human** competitor ([B263](https://youtu.be/iCj_ATyThvc))
- 200M+ clinical conversations deployed ([B091](https://youtu.be/AN65uc645mE)) — regulated-domain scale exists
- ~82% outcome reduction from agent deployment measured pre/post ([B176](https://youtu.be/RVxym6mmIns))
- zlib rewritten in Lean: 32,000 lines of machine-checked proof ([B050](https://youtu.be/lRa9sPaMyy4)) — verification
  at research-grade rigor
- Einstein Arena: agents collaborating "in the wild" on curated open scientific
  problems ([B074](https://youtu.be/mMNkdYnIVC4))

## 6. Candidate workshop modules for research labs (raw material)

1. **"Get to your question faster"** (researcher track): literature agents, research
   memory systems, prompt→hypothesis→experiment decomposition. Non-coder friendly.
2. **"Your lab as a verifiable environment"** (RSE track): turning protocols into
   graders, provenance/replay infrastructure, eval design for fuzzy domains.
3. **"The judgment wall" clinic** (PI track): where agents saturate, how to review
   agent-generated science, eval-gaming detection, data-moat strategy.
4. **Format options (evidence-backed):** hackathon series ([A015](https://youtu.be/gGT4ysQOdIg)), role-specific
   2-week course ([B302](https://youtu.be/UcYoMg-8-L8)), anti-pattern-first curriculum ([B135](https://youtu.be/Z-c11pV_uvU)), ship-summit with
   pre-provisioned compute ([A019](https://youtu.be/nqaHTussq5o) — labs have their own compute, an advantage).

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
  (except [B074](https://youtu.be/mMNkdYnIVC4)/[B155](https://youtu.be/3ZMUiFaQ3qg)/[B247](https://youtu.be/XLEYtv3cMlw)/[B263](https://youtu.be/iCj_ATyThvc), which are genuinely research-domain).
- No corpus evidence on grant dynamics, publication incentives, or academic adoption
  culture — the biggest actual barriers in research labs.
