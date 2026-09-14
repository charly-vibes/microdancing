# Hypothesis Scorecard — pre-registered vs findings

**Sealed hypothesis (verbatim):**
> "I think that the AIEng is pure hype, most of speakers and companies do not have a lot of experience and all are trying the same things disregarding all the Industry experience. On the other side the Enterprise AI Summit has a lot of experienced, old, known names in industry given their opinion."

Scored against: diff_report.md, aggregate.json, data_points.json, talks.json Layer-1.

## Claim-by-claim

### 1. "AIEng is pure hype" — **REFUTED (as stated), with a partial truth**
- B's evidence posture is the *most* data-dense of the two corpora: 39% customer-data style, 210 numeric claims cataloged (vs A's 57% personal-anecdote / 25 numeric claims). "Pure hype" does not match the evidentiary texture.
- Partial truths that survive: 18% of B talks carry product-pitch framing; "X is the new Y" standardization claims and "X is dead" declarations are a real pattern (MF2 11%, MF3 15%); titles are message-dense in a promotional house style. So: *promotional accent, but metric-grounded* — not hype-dominant.
- Irony check: the corpus with the *least* quantitative grounding is A (the one trusted in the hypothesis): 57% of A talks rest on personal war stories, 0-4 survey data.

### 2. "Most speakers and companies do not have a lot of experience" — **PARTIALLY SUPPORTED, evidence incomplete**
- Supported structurally: B is 70% vendor (mostly small AI-native startups: "built in a weekend", "5 years old", "single weekend build" framings recur); 221/358 speaker roles unspecified (thin org credentials on stage). A skews to named-tenure veterans (19 yrs ThoughtWorks, 50 yrs programming, CTOs/CEOs of established firms).
- Refuting evidence: B is *not* short of deeply credentialed speakers — GPT-4 co-author, Distinguished Engineer at Microsoft, Mike Krieger, Richard Socher, Garry Tan, 20-yr security educator, MIT Media Lab, frontier-lab research leads. The credential gap is real at the *median* but the tails overlap heavily.
- Caveat: "most lack experience" cannot be fully verified — role data for B is title-derived only (recorded limitation).

### 3. "They are all trying the same things" — **REFUTED at topic level, PARTIALLY SUPPORTED at format level**
- Topic spread in B is broad: 20 topics, top topic only 28%. Eleven clusters don't exist in A at all. That is the opposite of monoculture.
- But: literal repetition exists — a 7-talk "How FDE is done at X" series, an evals cluster, MCP-Apps talks, skills talks. Same *formats* recur more than same *ideas*.

### 4. "Disregarding all the Industry experience" — **REFUTED, strongly**
- B explicitly and repeatedly anchors claims in prior engineering history: "Agents are where microservices were in 2015" (B044), "AI teams are about to learn why [feature flags]" (B255), "solo builders reinvent a worse CI/CD" (B286), "your LLM stack is a 2008 database" (B228), control-theory loops (B188), psychology's measurement theory applied to evals (B272), Vannevar Bush 1945 (B136), distributed-systems timeout semantics (B045).
- If anything, B invokes accumulated industry experience *more often* than A, whose historical anchor is a single analogy (DevOps, MF1, 13% and B ~0%).

### 5. "Enterprise AI Summit has experienced, old, known names giving their opinion" — **SUPPORTED (most accurate part)**
- A's evidence style is 57% personal war story; speakers carry explicit long-tenure credentials; well-known names (Beck, Yegge, Majors, Cockcroft, Kim). A is genuinely experience- and opinion-led.

## Overall verdict
**Half supported, half refuted.** The structural skepticism (younger/vendor-heavy corpus with pitch accents vs a tenured experience-led program) is confirmed by the data. The dismissal ("pure hype", "disregards industry experience", "all the same") is contradicted: B is the more metric-grounded corpus, invokes prior industry knowledge more explicitly, and covers more distinct technical ground. The *real* difference the data shows is not experience-vs-hype but **transformation-programming vs construction-programming**, and **anecdote-led vs metric-led persuasion**.

## Scorecard meta-note
Extraction ran blind to this file (checksummed at sealing: ee98fe67…); framing taxonomy, topic codes, and evidence styles were fixed before opening. No post-hoc recoding was done.
