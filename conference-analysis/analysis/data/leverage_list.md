# High-Leverage Talks for Your Workflow

From the comparative analysis of the two conference playlists (Enterprise AI Summit / AI Engineer World's Fair 2026).
Selected against your usage profile: **solo fleet operator** (48 projects), **context churn** (307 `/clear`, 9 compactations, 48% sessions <10 turns), **review-centric craft** (rule-of-5 ×115, commit ×75), **29 untested skills**, **rate-limit pressure** (54 checks, multi-model juggling).

## Tier 1 — direct hits on your bottlenecks

### 1. The Era of Compound Engineering — Kieran Klaassen, Every/Cora
- **Watch:** https://youtu.be/_ehJyfHg1Vk
- **Stats:** 8412 views / 163 likes
- **Transcript:** transcripts_aieng/txt/081 - The Era of Compound Engineering — Kieran Klaassen, Every⧸Cora [_ehJyfHg1Vk].txt
- **Why:** The closest peer profile in the corpus: a solo operator who hasn't read most of his code this year and still ships a full email client. Maps the exact bottleneck sequence (code quality → review → skills → verification) you'll hit as your fleet grows.

### 2. Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI
- **Watch:** https://youtu.be/WP3hjUXd918
- **Stats:** 7700 views / 153 likes
- **Transcript:** transcripts_aieng/txt/106 - Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI [WP3hjUXd918].txt
- **Why:** Their finding: doing NOTHING to context beat every compaction technique on recall, cost, and latency (97% cache hits). Your /clear-307-times reflex is exactly what this talk questions.

### 3. Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind
- **Watch:** https://youtu.be/0vphxNt4wyk
- **Stats:** 78558 views / 1681 likes
- **Transcript:** transcripts_aieng/txt/268 - Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind [0vphxNt4wyk].txt
- **Why:** You maintain 29 skills, run rule-of-5 115 times, and have zero evals on any of them. This is your gap stated bluntly, with a full build→test lifecycle.

### 4. A Genius With Amnesia - Victor Savkin, Nx
- **Watch:** https://youtu.be/jVjt-2g8NMY
- **Stats:** 2181 views / 42 likes
- **Transcript:** transcripts_aieng/txt/338 - A Genius With Amnesia - Victor Savkin, Nx [jVjt-2g8NMY].txt
- **Why:** Your short-session pattern means agents relearn your 48 projects' context every session. Memory/persistence architecture is your biggest structural unlock — this talk frames the problem precisely.

### 5. The State of Model Routing — NVIDIA, Cognition, OpenRouter
- **Watch:** https://youtu.be/QHBjufYK8TA
- **Stats:** 3252 views / 61 likes
- **Transcript:** transcripts_aieng/txt/140 - The State of Model Routing — NVIDIA, Cognition, OpenRouter [QHBjufYK8TA].txt
- **Why:** Your 54 rate-limit checks and 6-model rotation. Key counterintuitive finding: small models thrash outside their training distribution — tool-call loops until they cost MORE than the expensive model. Changes how you downgrade under rate limits.

## Tier 2 — upgrade your review loop (your current moat)

### 6. How to Kill the Code Review — Ankit Jain, Aviator
- **Watch:** https://youtu.be/YgEv7IQzGdM
- **Stats:** 8070 views / 143 likes
- **Transcript:** transcripts_aieng/txt/104 - How to Kill the Code Review — Ankit Jain, Aviator [YgEv7IQzGdM].txt
- **Why:** >30% of changes now merge with no review; AI writes, AI reviews in a loop. Your rule-of-5 habit is the human version — this is the shape of its successor.

### 7. ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay
- **Watch:** https://youtu.be/TJPInBjhE4Q
- **Stats:** 1982 views / 28 likes
- **Transcript:** transcripts_aieng/txt/280 - ReviewDebt： a practical framework for scoring every pull request — Sachin Gupta, Ebay [TJPInBjhE4Q].txt
- **Why:** Metrics that see what your review skill can't: bloated diffs, weak tests, ownership sprawl. Quantifies your review loop's blind spot.

### 8. Guide, Verify, Solve — Anirban Chatterjee, Sonar
- **Watch:** https://youtu.be/03l29gJXpCE
- **Stats:** 11525 views / 205 likes
- **Transcript:** transcripts_aieng/txt/130 - Guide, Verify, Solve — Anirban Chatterjee, Sonar [03l29gJXpCE].txt
- **Why:** CMU study: AI-tool productivity gains evaporate after ~3 months while verification debt stays. Directly relevant to your 5-month usage arc.

## Tier 3 — scale patterns to steal

### 9. I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON
- **Watch:** https://youtu.be/4kYl2_mqmnQ
- **Stats:** 2469 views / 71 likes
- **Transcript:** transcripts_aieng/txt/293 - I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON [4kYl2_mqmnQ].txt
- **Why:** Honest field report of multi-machine agent ops. You're one machine today — this is your next 6 months ('before any machine broke, I broke').

### 10. AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack
- **Watch:** https://youtu.be/M05vON8i0aI
- **Stats:** 24518 views / 181 likes
- **Transcript:** transcripts_aieng/txt/049 - AI-Native Organisations Run on Skills： How to Structure and Scale Them — Imad Touil, QuantumBlack [M05vON8i0aI].txt
- **Why:** The build → share → GOVERN skills gradient. You're at step 1 with 29 skills; governance is what keeps them from rotting.

### 11. Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company
- **Watch:** https://youtu.be/bdHaOXZOhcM
- **Stats:** 2007 views / 46 likes
- **Transcript:** transcripts_aieng/txt/083 - Prototyping as Leadership： How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company [bdHaOXZOhcM].txt
- **Why:** CTO shipping 2–10 PRs/week from a manager schedule — the template for combining your para/areas admin work with actual building.
