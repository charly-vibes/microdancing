# Thematic Report — Memory Systems & Enterprise Knowledge Bases

**Generated:** 2026-09-15

**TL;DR:** The corpus has converged on one memory architecture (running profile + on-demand retrieval tools, no vector RAG), agrees memory must be owned and co-evolve with the product, and shows in ablations that *recall policy* — not storage choice — is the variable that matters.

**Purpose:** a self-contained synthesis of what the two conference playlists say about
agent memory and enterprise knowledge management. Passes the amnesia test: readable
with zero prior context (corpora, terms, and sources are all defined inline).

**Sources:**
- **Corpus A** = *Enterprise AI Summit 2026* playlist: 27 talks, all coded from full abstracts; 4 transcript openings read.
- **Corpus B** = *AI Engineer World's Fair 2026* playlist: 358 talks, ~344 transcripts (~1.33M words); deep coding from titles + narrative descriptions, transcripts read for the talks cited in §1–5.
- Underlying coding: `analysis/data/extraction_A.json` / `extraction_B.json`,
  `analysis/data/data_points.json` (235 quantitative claims), `analysis/data/diff_report.md`.
- **Distribution note:** memory/continual-learning is a **Corpus-B-only cluster** (10+ talks;
  0% of Corpus A as primary topic). Every talk cited below is from Corpus B. The absence
  itself is a finding: the enterprise-leadership conference does not discuss how agent
  memory should be built; the engineering conference has a full cluster on it.

**Method caveats:** all claims below are attributions to speakers (what they said on
stage), not independently verified facts. All verbatim quotes are transcribed from
YouTube auto-generated captions; wording, model names, and speaker names may be
slightly garbled. Talk IDs are stable; links point to YouTube. File paths are
relative to this file (`conference-analysis/`).

---

## Glossary (terms as used by the corpus)

| Term | Meaning as used in these talks |
|---|---|
| **Running profile** | An async-generated, periodically re-synthesized summary of a user/project, injected into every new conversation (ChatGPT, Claude architecture) |
| **Dreaming** | Community term for the background re-synthesis pass that updates the running profile |
| **Harness** | Everything wrapped around the model: tools, context management, memory, guardrails |
| **Recall policy** | The rule deciding what gets retrieved into context, when, and how it is ranked |
| **Write–manage–read loop** | Memory viewed as a control loop around the model, not just a store |
| **Oracle** | In Druga's ablation (§3): the evaluation condition where ground-truth-correct memories are injected every loop — the upper-bound comparator |
| **Memory taxonomy** (Malcolm) | Short-term (session), long-term (cross-session), episodic (past interactions), procedural (steps taken), semantic (facts) |
| **Knowledge taxonomy** (Castro) | Intrinsic (in weights) / extrinsic (retrieved, context-engineered) / learned (continual) |

---

## 1. Consumer memory has converged — and it is not vector RAG

Source: [Lessons from Studying Every Memory System — Shlok Khemani](https://youtu.be/5ZGyKWjQDr0) (3.2k views).

Khemani spent a year reverse-engineering ChatGPT, Claude, and Gemini memory. Findings:

- **Convergent architecture after independent evolution.** ChatGPT (Feb 2024 fact-list →
  Apr 2025 running profile) and Claude (Aug 2025 pure retrieval tools → Sep 2025 profile +
  retrieval) both landed on: **running profile always in context + on-demand tools to
  search past conversations**. Neither uses chunk-embed-vector-search as its memory.
- **Memory is a function of compute.** ChatGPT: dense ~4,000-token profile, updated every
  few days (high serving cost, low update cost). Claude: ~1,000-token profile in complete
  sentences, updated every 24h — the exact opposite trade-off. Same architecture, opposite
  points on the compute-vs-serving curve.
- **Staleness is unsolved.** Both systems still confidently store facts that were never
  true (his profile said he *traveled to Turkey* after a conversation *deciding between*
  Turkey and Thailand).
- **Strategic claim: memory cannot be outsourced.** Every top consumer product builds
  memory in-house; it must co-evolve with the product, not be bolted on.
- **The loop is de facto continual learning** (profile → conversations → synthesis →
  profile), currently outside the weights. Open questions he poses: will it ever move
  into weights, what data kicks it off, and who pays for a per-user self-learning model.
- **Product problem, not technology problem:** his chatbot held contradictory travel
  facts because it never reasoned over his email — and worse, is not even *aware* of the
  conflict. Products build private siloed memories of the same person and don't share.

## 2. Enterprise memory is a shared-state problem, not a storage product pitch

Source: [No Memory, No Harness — Kay Malcolm, Oracle](https://youtu.be/jA_x7F8caHI) (1.0k views).

- **The original war story:** her distributed team checked in code via Codex but not the
  *context* behind it — "git records the code and not human intent." AI made individuals
  faster while team throughput stalled. Fix: a shared **memory broker** holding
  procedural/episodic/semantic memory keyed to forks and commits. Her punchline:
  "AI makes individuals faster; shared memory makes teams faster."
- **Agent = model + tools + context + memory + guardrails**, with memory as "the central
  nervous system" connecting the brain (model) to the body (harness).
- **Storage fragmentation is the enterprise knowledge-base failure mode:** data scattered
  across relational / JSON / graph / vector stores means the agent must guess the single
  source of truth — "sometimes it'll get it right, most times it'll get it wrong and it's
  going to burn up a whole bunch of tokens."
- Quotes Harrison Chase's maxim: **"If you don't own your harness, you don't own your
  memory."** File-system memory (the `MEMORY.md` pattern) "works with one" agent but
  breaks when you scale past one — which every enterprise does.

## 3. The most rigorous engineering result: retrieval policy beats oracle injection

Source: [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](https://youtu.be/R3-anFK1YM8) (25.6k views — the most-watched talk cited here).

- Mental model: **memory = write–manage–read control loop**, not a database.
- Ablations on local models (Qwen 27B 4-bit + DeepSeek V4 flash on a single M3 Ultra;
  model names per captions, which garble them), 68
  Xbench long-horizon questions × multiple recall policies and seeds:
  - **Negative result as boundary:** when the task fits in context, memory added *zero*
    capability at added cost. Memory pays off only past the context horizon (in her
    benchmark, the needed fact sat at step 124 while the agent asked at step 500).
  - **A ranked decisions-ledger recall policy beat vector RAG in the tested ladder —
    and even beat an "oracle"** (see glossary) that injected ground-truth memories,
    because giving the model the right memory doesn't force it to *use* it. Result
    held across both models and a second benchmark (Spider V2).
- Her maxim: **"Bad memory is expensive"** — it burns tokens and sends the agent the
  wrong way. Recommendation: treat the **recall policy as a first-class metric**
  (what to store, how to rank, what survives repeated sessions).

## 4. The markdown-files backlash: graph memory and structured recall

Source: [CrabRAG — Stephen Chin, Neo4j](https://youtu.be/Q0VkgCyNVUg) (21.9k views).

- Current agent memory (OpenClaw-style `MEMORY.md`, daily notes, skills-as-markdown) is
  readable and hackable, but "if your whole memory is a bunch of markdown files, you're
  wasting a lot of tokens" — his agents load ~100k tokens per round "in the hopes that
  something will be useful."
- Pitch: **graph memory** (relations instead of bulk token-loading), including a
  graph-of-skills approach (cites a Neo4j arXiv paper) so agents select the right skill
  chain instead of guessing.
- Notable counter-note in the same talk: **Goose** treats memory as just another MCP
  server (pluggable remember/forget/retrieve) — structured interface, plain files underneath.

## 5. Personal knowledge bases as agent substrate

- [Turn 10,994 Notes Into Memory — Iusztin & Bouchard](https://youtu.be/ZRM_TfEZcIo)
  (19.2k views): the pattern is a system **between the harness and the second brain** —
  pulling high-signal notes from Obsidian/Readwise/Notion into agent work. Ownership is
  the differentiator vs NotebookLM: "you don't own it, it's not agent-native, it's weak
  for coding tasks."
- [On AI and Knowledge — Pablo Castro, Microsoft](https://youtu.be/RGSFUqzqErE) (2.3k views): the
  taxonomy grounding all of the above — **intrinsic** (weights) / **extrinsic**
  (retrieved, context-engineered) / **learned** (continual) knowledge — and the claim
  that intrinsic knowledge alone powered the first exponential (IntelliSense '96 →
  Copilot 2021 → agents), but "only gets you so far" for agents that must participate
  in an organization.

## 6. Corroborating cluster talks (secondary evidence)

*Lighter-weight than §1–5: these are coded from titles/descriptions and transcript
openings, not full-transcript reads.*

- [Claude for Long-Horizon Tasks — Lance Martin, Anthropic](https://youtu.be/9QebvrrY3KY) (18.3k views): Anthropic's account of the "dreaming"/profile-synthesis mechanics that Khemani reverse-engineered — the two talks triangulate.
- [Continual Learning for AI Agents — Soheil Feizi, RELAI](https://youtu.be/2IxD9OB3XuQ): turning failures into durable improvements — the write side of the loop as an enterprise discipline.
- [User Signal Dies at the Retrieval Boundary — Sonam Pankaj, StarlightSearch](https://youtu.be/Jx4ZFEAq6bY): task-relevant signal dies at the retrieval boundary — agents then fail and repeat the same work.
- [Video Has No Memory — James Le, TwelveLabs](https://youtu.be/mOf-PP4mVjA): vertical-domain memory build (video corpora) — evidence for Khemani's "nobody outsources memory" claim from a non-chat domain.
- Coded data point from [The Factory That Dreams: 39 AI Agents, No Framework — Rushabh Doshi, Machinecraft](https://youtu.be/jtzh-GBXBWc) (1.8k views): a 39-agent operating system (sales, recruitment, quoting, marketing) explicitly includes **org memory** as a component — memory as shared team infrastructure, not per-chat state.

---

## Cross-cutting takeaways

1. **Consensus architecture exists:** running/synthesized profile (always in context) +
   on-demand retrieval tools + async background re-synthesis. Vector RAG as *the* memory
   system is dead; it survives only as one recall policy among several, and loses in
   ablations (§3).
2. **Own your memory.** Memory co-evolves with the product and can't be outsourced
   (Khemani), and if you don't own the harness you don't own the memory (Chase, via
   Malcolm). File-based memory works for one agent, breaks at team/enterprise scale.
3. **Retrieval policy > storage choice.** What to write, how to rank, what to recall —
   measured as a first-class metric — matters more than the backing store.
4. **Enterprise twist:** memory is a *team* artifact (shared context across humans,
   agents, forks, commits), and multi-store fragmentation without a source-of-truth
   strategy silently burns tokens.
5. **Known boundaries:** memory adds nothing when the task fits in context; staleness
   and conflict-awareness remain unsolved — and per Khemani, their resolution is a
   product-design problem, not a model-capability problem.

## Gaps & counter-evidence (for balance)

- Every cited talk is a single speaker's account; none of the numbers (4k vs 1k tokens,
  step 124/500, ~100k tokens/round) are independently verifiable from the corpus alone.
- The strongest quantitative result (Druga) is on *local, small* models and two
  benchmarks; transfer to frontier models is asserted, not shown.
- The graph-memory and unified-database claims come from vendors with obvious stakes
  (Neo4j, Oracle) — the corpus contains no neutral head-to-head of markdown files vs
  graph vs database memory at enterprise scale.
- Nobody in the corpus demonstrates memory moving into weights at individual-user
  granularity; continual learning remains an extrapolation, not a shipped pattern.
