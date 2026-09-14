# Comparative Meta-Analysis Spec — Two AI Conference Playlists

**Status:** Draft v2 — revised per Rule-of-5 review; data claims verified against files
**Snapshot:** fetched 2026 session (corpus A: 27 videos; corpus B: 358 videos, 14 private at fetch time)
**Question:** *Do the two conferences differ in content and message?*
**Principle:** Extraction runs blind. Hypotheses are pre-registered and sealed until coding is complete.

---

## 1. Data Sources

| Corpus | Playlist | Channel | Videos | Transcripts | Words (est.) |
|--------|----------|---------|-------:|-------------|-------------:|
| A | Enterprise AI Summit: Spring 2026 | IT Revolution | 27 | 27 | ~102k |
| B | AIE World's Fair 2026 | AI Engineer | 358 | 344 (14 private) | ~1.23M |

Artifacts:
- `playlist.json` — corpus A metadata + `transcript_uri`
- `playlist_aieng.json` — corpus B metadata + `transcript_uri`
- `transcripts/txt/*.txt`, `transcripts_aieng/txt/*.txt` — cleaned auto-captions

Known data constraints (measured, fetch date above):
- Dislike counts unavailable platform-wide (removed by YouTube in 2021).
- Like counts hidden: corpus A **8/27 (~30%)**, corpus B **14/358 (~4%)** → engagement metrics carry per-metric `comparable_n`.
- 14 corpus-B videos private (null stats, no transcript).
- Auto-captions: acceptable for theme coding; unreliable for verbatim quotes and exact tech names (fuzzy matching required).

## 2. Research Question, Operationalized

### 2.1 Content (topics & substance)
What is talked about, how much, by whom, with what evidence.

### 2.2 Message (normative stance)
Per talk, three extractable fields:
1. **Normative recommendations** — explicit do/don't advice; what the speaker says to *do*.
2. **Threat/opportunity framing** — what is declared urgent, changing, dying, or rising.
3. **Evidence style** — war story / framework-theory / data-survey / product pitch / opinion.

"Message difference" = same or adjacent topics carried with different recommendations, framing, or evidence styles between corpora A and B.

## 3. Extraction Layers

### Layer 1 — Structural metadata (deterministic, scripted, no interpretation)
Per talk:
- `conference` (A|B), `index`, `id`, `title`, `duration`, `upload_date`
- **Speaker role** parsed from title/description: engineer / senior / staff-principal / director / VP / C-level / founder / researcher / analyst
- **Company type**: AI or infra vendor / enterprise end-user / consultancy / academic / investor-media / other
- **Genre**: keynote / case study / product demo / panel / remarks / promo (remarks & promo flagged `message_eligible: false`)
- `appears_in_both_corpora`: speaker-name **+ affiliation similarity** match flag (name-only matching rejected: false-duplicate risk) (duplicate-speaker control)

### Layer 2 — Content claims (LLM-extracted)
Per talk, all claims stored as *attributions*, never ground truth:
- `topics[]` — against the shared codebook (see §4)
- `claims[]` — atomic statements, each with: `topic`, `evidence_type` (personal-experience / customer-data / survey / theory / product-pitch / opinion), `quote_span` (timestamp-ish reference), `numbers[]` (value, unit, context)
- `tech[]` — models, tools, frameworks (canonical list + fuzzy match for caption noise)
- `message` — the three fields from §2.2
- `selling_intent` — talk vs. disguised pitch (corroborated by vendor flag × product-mention density)

### Layer 3 — Derived comparative analyses
All frequencies as **per-talk rates within conference**, never raw counts.

1. **Topic diff**: shared topics (rate delta A vs B, with uncertainty), A-unique, B-unique (from codebook + free-coding residue)
2. **Message diff on shared topics**: for each shared topic, per-conference distribution of recommendation types, threat/opportunity framing, and evidence styles, shown as side-by-side deltas; where stances diverge, a qualitative quote pair (one excerpt per conference) is included. Panels/fireside chats are eligible but claims attributed to genre + named speakers.
3. **Evidence-quality diff**: distribution of evidence types per conference, crossed with speaker role and company type (practitioner-claimed vs vendor-claimed)
4. **Speaker-circuit effect**: rerun topic comparison excluding speakers present in both corpora
5. **Within-conference traction**: views and likes as rank-percentile *within own playlist* — **never compared across corpora** (channel reach confound: ~4k vs ~4M views)
6. **Lexicon check**: "same word, different meaning" — method: top ~15 shared terms by frequency, ~10 usage samples each, coded for sense (qualitative, sampled)
7. **Data-points inventory**: clean table of every quantitative claim (company, metric, value, context) — reusable deliverable

## 4. Codebook Construction (two-pass, joint)

- **Pass 1**: LLM free-codes themes on a stratified sample from *both* corpora → merge into one taxonomy; log themes unique to one corpus as residue.
- **Pass 2**: structured extraction of all talks against the shared codebook, identical schema for A and B.
- Codebook frozen after pass 1; additions during pass 2 go to a `late-themes` list and are reported separately.

## 5. Bias Controls

1. **Pre-registration**: user's suspicions written to `HYPOTHESES.sealed.md` before extraction; opened only after coding; each scored supported / refuted / no-signal.
2. **Bottom-up taxonomy** (joint, not per-corpus) — themes emerge from corpus, not priors.
3. **Claims ≠ facts** — every claim attributed to speaker + role + company type.
4. **Source-bias flag** on every claim (who benefits from believing it).
5. **Confounds declared in output**: audience composition, event scope, program curation, corpus-size asymmetry. Conclusions scoped to *these two programs as curated*, not "the communities".

## 6. Validity Threats & Handling

| Threat | Handling |
|---|---|
| Genre contamination (promos, remarks, demos) | Genre field mandatory; message analysis restricted to `message_eligible` talks; comparisons stratified by genre |
| Corpus size asymmetry (27 vs 344) | Rates with uncertainty (Wilson intervals); rare-topic comparisons avoided or flagged low-power |
| Speaker duplication across corpora | Both-corpus speaker flag; sensitivity rerun excluding them |
| Engagement confound (channel reach) | Traction metrics rank-normalized within conference only |
| Missing likes / private videos | `comparable_n` tracked per metric; reported with every aggregate |
| Caption noise on tech terms | Fuzzy matching; tech counts marked approximate |
| Empty/garbage transcripts | Validation step: word-count floor; failures quarantined and reported (currently 0 empty files — verified) |
| Same speaker, repeated talk within a corpus | Dedupe rule: same speaker + fuzzy title similarity > 0.8, or same core claim set → single count; borderline cases logged, not silently dropped |

## 7. Deliverables

1. `analysis/data/` — layer outputs: `talks.json`, `claims.csv`, `data_points.csv`, `topics.csv`
2. **Comparative diff report** (markdown) — minimum contents: all §3.1–3.7 analyses (or explicit "not performed + why" per item); topic rates per conference with deltas; message deltas with quote pairs; evidence-style distributions; A-unique / B-unique themes; lexicon findings; within-conference traction findings
3. **One-page synthesis** per corpus (who speaks, about what, with what authority)
4. **Hypothesis scorecard** — sealed file opened, each pre-registered suspicion scored
5. Limitations section (§5 confounds + §6 threats)

## 8. Execution Plan

| Step | Action | Scope |
|---|---|---|
| 0 | Seal hypotheses file; write `talks.json` skeleton from metadata | both corpora, scripted |
| 1 | Layer-1 structuring (roles, company type, genre, duplicates) | all 371, scripted + LLM assist |
| 2 | Pass 1 free-coding → codebook v1 | stratified sample (~40: all of A + stratified B) |
| 3 | Pass 2 structured extraction | all message-eligible talks |
| 4 | Derived analyses + diff report | scripted over extraction outputs |
| 5 | Open hypotheses, scorecard, final report | — |

Cost note: pass 2 over ~350 transcripts (~1.2M words) is a batch LLM job; chunked, resumable, cached per talk.

## 10. Changelog
- v1: initial draft
- v2: Rule-of-5 revision — verified data-constraint figures (A likes hidden 8/27, B 14/358); added snapshot date; defaults for §9; message-diff metric defined; dedupe rule made operational; duplicate-speaker matching requires affiliation; transcript validation step; diff-report acceptance criteria; panel/fireside eligibility clarified

## 9. Open Decisions (defaults chosen; override before execution)

| Decision | Default (per review) |
|---|---|
| Pass 2 scope | Full corpus (all message-eligible talks) — stratified sample only if cost forces it |
| Opening/closing remarks | Excluded from message analysis (`message_eligible: false`), retained in topic counts |
| Hypotheses file | Sealed now, before any extraction |

Any override to these defaults must be recorded in this file's changelog before step 2 begins.
