# AIX Practices from Industry → genesis-vibes (corpus-grounded)

**TL;DR:** the AIEWF corpus converges on four adoption-ready practices — receipt
contracts, budget-aware context artifacts, evals-as-merge-gate, and a
closed feedback→scenario loop — all of which genesis-vibes can adopt
incrementally because it already owns the substrate.

**Purpose:** extract practices from the AIEWF corpus (344 talks, ~1.33M words) that
the **genesis-vibes** crate (agent-experience infrastructure for the charly tool
family) can leverage. Companion to `memory-systems-report.md` and
`analysis/data/ddl-family-evaluation.md`; complements
`workshop/skill_management_practices.md` (skill-artifact side) — this report covers
the **tool-side** AIX surface: envelopes, self-healing errors, managed blocks,
llms.txt, evals, doctor/status/feedback.

**Method:** targeted mining of the 67 AIX-relevant AIEWF talks (harness, evals,
skills, context, observability clusters), plus the corpus's existing analysis
artifacts. **Scope note:** the AIX/harness/evals cluster is AIEWF-only — the EAIS
corpus (27 org-transformation talks) contains no tool-side AIX content, mirroring
the skills-side finding in `workshop/skill_management_practices.md`.
Cross-checked against genesis source (`src/aix.rs`, `src/evals.rs`) and
`.wai/projects/genesis-foundation/research/`. Caveat: transcripts are
auto-captions; quoted wording is approximate. Load-bearing numbers were verified
verbatim where quoted (the 2% skills cap, the 200→2,000–5,000 instruction
celing, the five failure shapes, the eval-gate policy).

**Headline:** the corpus converges on four industry practices that genesis is
*uniquely positioned to adopt* because the crate already owns the substrate
(four adoption themes developed across eight sections below; sections 6 and 8
are confirmations of positioning rather than gaps):
1. **Receipt-based harness contracts** (envelope = receipt, not just status)
2. **Budget-aware context construction** (llms.txt/managed blocks sized like Codex caps skills)
3. **Evals-as-merge-gate + evals-on-model-change** (Scenario replay as the gate)
4. **Closed loop: production failures → scenarios** (feedback module → eval corpus)

---

## 1. The receipt contract: "model proposes, harness commits, receipt proves"

**Evidence** — [B173](https://youtu.be/BInpv7lGp1o) (OpenAI, *Your Agent Didn't Fail. Your Harness Did.*):
most production agent failures are harness failures, not model failures. Five
failure shapes, each invisible to the user edge: **state hole** (delivered ≠
remembered), **overlapping writers** (two locally-correct writes, one wrong
outcome), **dangling tool call** (run waits for an event that never arrives),
**approval drift** (capability mistaken for authority), **missing edge proof**
(internal success ≠ user-visible proof). Key line: *"A transcript tells you what
the agent said. A receipt tells you what the system allowed, attempted, executed,
and what the user-visible edge confirmed."* Five-question audit: what woke it up
/ what state did it inherit / which authority / what executed / what evidence survived.

**Genesis mapping:** the envelope is already half a receipt (`ok`,
`envelope_version`, `data`, `warnings`, `hints`). The B173 contract suggests
receipt fields genesis doesn't emit: **terminal outcome classification**
(success/failure/timeout/cancelled — "silence cannot be neutral"), **attempt +
idempotency key** for mutating commands, and an **evidence pointer** (what the
user-visible edge can verify). The exit-code contract shipped in genesis-u40
(the exit-2-for-internal-I/O ticket, closed 2026-09-15) covers the crash
boundary; B173's claim is the stronger one — *coherent success
can still be a lie*, which is exactly what a structured envelope makes detectable.

**Leverage:** extend `Envelope` with optional receipt metadata (tool-owned, additive
— no breaking change under the caller-supplied `cli_version` contract); add a
Scenario check `receipt_records_terminal_outcome` alongside the existing
`ok_envelope` / `agent_followed_hint` checks.

## 2. Budget-aware AIX artifacts: size, flexibility, cacheability

**Evidence** — [B128](https://youtu.be/shRR1e2HXMk) (OpenAI, *Codex, Behind the Harness*):
Codex constructs context against three concerns — **size** (contradiction risk
grows with context), **flexibility** (good experience at any skill/plugin count),
**cacheability**. Concrete mechanisms: the available-skills list is **capped at 2%
of the context window**, with description text *gracefully degraded* when over
budget; rarely-used tools are **deferred** behind tool search rather than loaded
eagerly; stateful delta updates send only what changed.

**Genesis mapping:** `genesis::aix` generates `llms.txt` / `llm.txt` artifacts with
no budget notion. The corpus says the cost side is real: an AIX artifact that
overstays its token budget silently degrades the very agents it serves (cf. the
"contradicting information" risk — genesis emits 7 managed blocks in DDL's
AGENTS.md; the ddl-family evaluation flagged exactly this proliferation).

**Leverage:** teach `aix.rs` to report the **token cost of each generated artifact**
(and a `--budget` mode that trims section verbosity like Codex degrades skill
descriptions). This also makes the planned **AIX-ablation eval slice** measurable:
the metric is not just task delta with/without artifacts but *delta per token spent*.

## 3. The instruction ceiling moved 10×: compression → verification

**Evidence** — [B019](https://youtu.be/XzJD1bvXKjs) (Voss, Arize AI): instruction-following
capacity went from ~200–300 rules (IFScale, 2025) to **2,000–5,000** (frontier, 2026).
Consequences: (a) the compression problem is gone — "the new hard part is knowing
whether it actually did what you said"; (b) failure modes are now **model-specific**:
quiet forgetting, loud refusal, overthink-into-silence, and **polite half-finish**
(does the work, then quits mid-way with a confident tone — the most dangerous
because it looks like success); (c) reordering instructions changes reliability
(46-model replication), and context-rot research found *coherent, well-structured
text can fail more* than shuffled instructions.

**Genesis mapping:** three direct hits.
- **Re-audit size assumptions.** Any genesis decision made >6 months ago about how
  compact managed blocks / distilled skill bundles must be is "probably already
  wrong" (Voss's own phrasing). The incitaciones essentials-bundle rationale
  (161 distilled files) deserves a re-check against current models.
- **The polite half-finish failure is the envelope's raison d'être.** Parseable
  envelopes + nonzero-exit contracts are the industry-grade antidote to silent
  partial success — worth stating explicitly in evals.md as the *why*.
- **Per-model eval matrix.** `genesis::evals` scenarios should be replayable
  across a model list, since failure modes (refusal vs. drift vs. half-finish)
  differ by model. No existing ScenarioCheck covers the refusal,
  overthink-silence, or half-finish shapes — the composable check design makes
  adding them straightforward.

## 4. Evals as merge gates; evals on every model change

**Evidence** — [B268](https://youtu.be/0vphxNt4wyk) (Schmid, DeepMind): "skills without
evals are wishful thinking" (also B171/FactSet). Their gate: **a change is not
merged unless it improves existing evals or adds new ones**; every skill change
carries regression tests; **rerun skill evals on every model change** — a new
model attended only to the *start* of skill files and silently ignored critical
end-of-file instructions; nothing in the artifact changed and the agent still failed.

**Genesis mapping:** managed blocks, llms.txt, and AGENTS.md blocks are
skill-analogous contracts that genesis injects into 6+ tool repos. None is
eval-gated today. The evals module exists but nothing *consumes* it as a gate —
echoing the ddl-evaluation finding that the pipeline "exists in docs only."

**Leverage:** wire `genesis evals` (Scenario replay) into CI as a required check for
changes that touch AIX artifact generation (`src/aix.rs`, scaffold managed-block
templates, doctor output wording). Add an `evals --models` matrix job. This is the
cheapest high-value integration in this report.

## 5. Closed loop: production failures become scenarios

**Evidence** — [B192](https://youtu.be/31GUkCBD-Uc) (Uber): closed-loop evals — production
failures are mined back into the eval corpus continuously. [B190](https://youtu.be/Ib5t2RLtxvM)
(Snorkel): traces → simulations; production runs generate the scenario set.
[B085](https://youtu.be/nxokqOq1imY) (Braintrust): evals rot as the agent evolves — they must
be regenerated from live behavior.

**Genesis mapping:** genesis owns **both ends already** — the `feedback` module
(agent-reported `bug`/`friction`/`docs-gap`/`aix-gap` issues) and the `evals`
module (Scenario replay). Nothing connects them. This is the "no tool consumes
another's workflow state" gap from the ddl evaluation, but *inside* genesis itself.

**Leverage:** make `feedback --kind aix-gap` (and bug reports) **scenario-convertible**:
a real failure's transcript (AgentSteps) becomes a replayable Scenario fixture in
the tool repo's eval corpus. Each aix-gap issue then closes with a regression
scenario, not just a fix. This operationalizes agent-issue-reporting.md §10.

## 6. Falsifiable goals and completion detection

**Evidence** — [B128](https://youtu.be/shRR1e2HXMk): Codex's goal loop works because the
model must call `update_plan` to declare completion against a **concrete,
falsifiable** objective; harness injects continuation prompts until then.
B173's audit question 5 ("what evidence survived?") is the same principle at the
system boundary.

**Genesis mapping:** genesis-ntg (P0 epic) found **no falsifiable value proposition**
in any of the 7 tool repos. The corpus provides the argument for why this matters
beyond hygiene: falsifiability is the mechanism that lets *any* harness (or eval,
or status dashboard) detect completion and drift. Genesis's `status` module is
the natural consumer: StatusItems with Healthy/Warning/Error are only meaningful
against falsifiable per-tool value claims.

**Leverage:** ntg's L1 slice should produce, per tool, a value proposition stated as
a checkable StatusContributor condition — not prose. That unifies the epic's
L1 (falsifiable VPs) with L4 (alignment observability) using existing genesis
substrate.

## 7. Long-horizon and distractor-rich scenarios

**Evidence** — [B198](https://youtu.be/cO8qC6HBuBg) (Andon Labs): long-horizon evals need
**distractors and atmosphere** (multi-hour tasks with irrelevant pressure); existing
long-horizon evals are "an order of magnitude or two shorter." Context-rot
findings (B019) reinforce: accuracy falls 30–50% *before* window limits, and
conflicting instructions are the killer.

**Genesis mapping:** `Scenario::run` replays single-pass, single-agent transcripts
against in-memory fixtures. Real agent-tool interaction is multi-turn with noise:
stale llms.txt sections, overlapping managed blocks, contradicting hints.

**Leverage:** a follow-up evals slice: **multi-step scenarios with distractors** —
e.g., a stale managed block contradicting the current `--help` text, and a check
that the agent trusted the tool's envelope over the stale doc (generalizes
hint-blindness into *doc-drift blindness*). Cheap to add; directly tests what
B171/B128 identified as the top silent failure (stale artifact).

## 8. Observability is the first-class harness component

**Evidence** — [B007](https://youtu.be/gxVZ_1tuuq4) (AWS): harness = everything left when
you remove the model; components enumerated in order — loop, memory, skills, tools,
runtime, context management — with the explicit correction that **observability
and evaluations "should be the first thing that I say."** [B014](https://youtu.be/8KkibGU_DDY)
(Yutori): "agents that can't be measured, can't be managed."

**Genesis mapping:** genesis's `status` + `doctor` + `evals` triad *is* the
observability layer for the charly family — this is a market-positioning
confirmation, not a gap. The gap is adoption: pretender hook missing (flagged in
the genesis-foundation status report), doctor/status initialized-and-forgotten in
most repos (ddl evaluation).

**Leverage:** the corpus supports the ddl-evaluation's "fund the spine" verdict with
an industry norm: harness observability is table stakes. Positioning genesis as
"the observability + contract layer for agent-first CLI tools" is
corpus-supported language for the README/llms.txt.

**Reconciliation with `ddl-family-evaluation.md`:** that evaluation's verdict —
fund wai + testaruda, demote init-and-forget tools unless they earn a falsifiable
metric — governs *adoption effort*, not substrate value, and it explicitly noted
the "genesis = status aggregation only" confound. This report is the substrate
counterpart: recommendation #1 below (evals as merge gate) is precisely the
"falsifiable metric or demotion" mechanism the ddl evaluation demanded,
applied to genesis's own artifact claims. Read the two together, not in conflict.

---

## Prioritized recommendations (mapped to existing tickets)

Effort scale: **S** = ≤1 session, **M** = 1–3 sessions.

| # | Recommendation | Substrate | Effort | Ticket hook |
|---|---|---|---|---|
| 1 | Wire Scenario replay as CI merge gate for AIX-artifact changes; `--models` matrix | evals module | S | new (ntg L4 slice). Precondition: each consumer repo has CI — note whisper-bez currently has none |
| 2 | feedback → Scenario converter: every aix-gap closes with a regression scenario | feedback + evals | M | new (operationalizes agent-issue-reporting §10) |
| 3 | Envelope receipt metadata: terminal-outcome class, attempt/idempotency, evidence pointer | envelope (additive) | M | new (extends genesis-u40 contract) |
| 4 | Token-budget reporting + graceful degradation for llms.txt/managed blocks; per-token ablation metric | aix.rs | M | planned AIX-ablation slice |
| 5 | Multi-step distractor scenarios (stale managed block vs live help → doc-drift blindness check) | evals | S | follow-up slice of genesis-zxv |
| 6 | Falsifiable VPs as StatusContributor conditions per tool | status + ntg | M | genesis-ntg L1+L4 combined |
| 7 | Re-audit size assumptions (essentials bundle distillation, managed-block compactness) against current models | docs/aix | S | EXCL-002 adjacent |

**Sequencing note:** 1 and 2 together close the "pipeline exists in docs only"
verdict from `ddl-family-evaluation.md`; 3 is the only envelope-schema change and
should ride the next minor release (EXCL-002 — the pending decision on whether to
changelog it under Unreleased — gates the release, not this change); 4 unblocks the
already-planned AIX-ablation with a real metric.

**Sources (cited talks only):** B007, B014, B019, B085, B128, B171, B173, B190,
B192, B198, B268 (transcripts_aieng/txt/); corpus artifacts: leverage_list.md,
skill_management_practices.md, ddl-family-evaluation.md; genesis source:
src/aix.rs, src/evals.rs, src/envelope.rs; whisper env.md (module contracts).
