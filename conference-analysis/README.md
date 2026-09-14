# Conference Analysis — Enterprise AI Summit vs AI Engineer World's Fair 2026

Comparative meta-analysis of two conference playlists: what each conference talks
about, what message they carry, and how it maps to this project's workflow.

**Question:** do the two conferences differ in content and message?
**Method:** blind extraction, pre-registered hypotheses (sealed until coding done),
two-pass codebook, per-talk-rate comparisons. Spec in `analysis-spec.md`.

## Contents

| Path | Contents |
|---|---|
| `analysis-spec.md` | Study spec (v2, reviewed via Rule-of-5) |
| `HYPOTHESES.sealed.md` | User's pre-registered suspicion (opened post-coding; checksum in scorecard) |
| `analysis/layer1.py`, `layer1_orgs.py` | Layer-1 scripts: metadata, roles, org classification |
| `analysis/data/talks.json` | 385 talks with structural metadata |
| `analysis/data/codebook_v1.md` | 20 topics, 7 message frames, evidence styles |
| `analysis/data/extraction_A.json` / `extraction_B.json` | Per-talk coding (27 + 344 talks) |
| `analysis/data/aggregate.json` | Topic/frame/evidence distributions per corpus |
| `analysis/data/data_points.json` | 235 quantitative claims extracted from talks |
| `analysis/data/diff_report.md` | **Main deliverable: the comparative diff report** |
| `analysis/data/hypothesis_scorecard.md` | Sealed hypothesis scored against findings |
| `analysis/data/leverage_list.md` | 11 highest-leverage talks for this repo's workflow, with links |
| `playlist.json`, `playlist_aieng.json` | Source metadata: stats, descriptions, transcript URIs |
| `transcripts/txt/`, `transcripts_aieng/txt/` | Cleaned auto-captions (27 + 344 talks, ~1.33M words) |

Note: `transcript_uri` fields inside the JSONs are relative to this directory.

## Headline findings

1. **Content:** EAIS = transformation conference (78% org-transformation, 43% culture, no unique themes); AIEWF = construction conference (20 topics, 11 clusters EAIS never touches: evals 22%, context/harness 18%, security 16%...).
2. **Message:** both led by war stories (~52%), but EAIS's fallback is culture-first framing (30%) while AIEWF's is product/standardization claims.
3. **Evidence:** EAIS argues from personal tenure (57% war stories); AIEWF from company metrics (39% customer-data style, 210 numeric claims).
4. Neither conference talks about formal verification (4% / 2%).

Raw `.vtt` caption files were deliberately excluded from git (61 MB); regenerate
from YouTube if needed (IDs are in the playlist JSONs).
