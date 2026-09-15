# Skill Management Practices — Managing, Building & Updating Agent Skills (corpus-grounded)

**Purpose:** corpus-grounded best practices for agent-skill (SKILL.md) lifecycle
management. Complements `skills_dossier.md` (human skills for workshops) — this
note covers the *artifact* side: how conference speakers build, update, and govern
skill libraries.

**Sources:** mined from AIEWF transcripts (344 talks). Densest cluster: talk 171
(FactSet skill-centric harness). **Scope note:** the EAIS corpus contains no
skills-lifecycle talks — every practice below is AIEWF-engineering-side evidence.
Cross-references: `skills_dossier.md` §4.5 (governance gradient),
`research_labs_addendum.md` §1 (verifiable graders).

---

## 1. Building skills

### Anatomy and routing ([B171](https://youtu.be/7jjudsEhBtM) FactSet)
- `SKILL.md` frontmatter (name + description) is the **discovery/routing signal**,
  not documentation. Body = business logic + references to scripts/files.
- Descriptions must be written **for triggering, aligned to the user request**
  ("use only when user asks for a PDF report" — the trigger word is the contract),
  kept **mutually distinct** so the agent doesn't misroute, and **never stale** —
  stale descriptions are a leading reason skills silently stop getting triggered.

### Progressive disclosure scaling ladder ([B171](https://youtu.be/7jjudsEhBtM))
| Scale | Mechanism |
|---|---|
| a handful | name/description/path inline in system prompt; body read on demand |
| more than ~10 | shortlisting layer becomes worth considering: embedding similarity search or a small model selects which skills enter the prompt |
| 100s | real trouble starts: skill hierarchy, metadata filters, and governance (see §3) |

### Skill shape ([B171](https://youtu.be/7jjudsEhBtM))
- **Start narrow, refactor outward**: "earning preparation skill", not "estimate
  analysis skill" — job-shaped skills; refactor the library as use cases emerge.
- **Skills are contracts, not docs** — they are versioned against a model.
  *"Skills without evals are wishful thinking."*

### Capture loop ([B261](https://youtu.be/eBUyTS7SzV4) Garry Tan, YC)
- *"If you have to ask for something twice, you failed."* After every successful
  agent task, **"skillify it"**: convert the worked solution into a reusable skill.
  Never do one-off work. (Blog post: "skillify it" on X.)
- Low-friction scaffolding compounds adoption: convention-over-configuration
  folders (skills/tools/channels) make agent assembly declaratively simple
  ([B002](https://youtu.be/9dYcwOkpCE8) Vercel). Who ships the skills is a separate
  claim: anyone with product understanding, not just engineers
  ([B171](https://youtu.be/7jjudsEhBtM), see §4).

### Minimal harness support ([B171](https://youtu.be/7jjudsEhBtM))
Bare minimum for skill support: **skill registry + system prompt + file-read tool**;
add bash/sandbox if skills run scripts.

---

## 2. Updating skills

- **Model upgrades silently break unchanged skills** ([B171](https://youtu.be/7jjudsEhBtM)):
  a new model attended only to the *start* of skill files and ignored critical
  instructions at the end — nothing in the skill changed, agent still failed.
  **Rule: rerun skill evals on every model change.**
- **Runtime skill refresh** ([B331](https://youtu.be/Jx4ZFEAq6bY) StarlightSearch):
  accumulate outcome signals (which past runs helped/hurt); once enough
  accumulate (their threshold: ~10 memories), **bake the reasoning into the
  skill** so the agent stays current — instead of stale facts (e.g. dead schema
  columns) living on forever in the system prompt.
- **Lifecycle mechanics** ([B171](https://youtu.be/7jjudsEhBtM)): semantic
  versioning, deprecation warnings, changelogs, periodic audits + validation checks.
- **Health metric** ([B261](https://youtu.be/eBUyTS7SzV4)): Tan proposes the commit
  history of the shared skills repo as the diagnostic — *"what would the commit
  history to your shared skills repo look like... what does that trend look
  like?"* Steady flow of updates = the brain is learning; a dead repo = the
  capture loop failed (interpretation of Tan's framing).

---

## 3. Managing (governance)

### Five governance dimensions ([B171](https://youtu.be/7jjudsEhBtM))
Borrow decades of code practice; keep it automation-heavy, human-in-the-loop —
governance ≠ red tape.

| Dimension | Question | Practice |
|---|---|---|
| **Admission** | should this skill exist, or extend an existing one? | automated gate on the registry, PR-review style |
| **Ownership** | who maintains it? | named maintainers per skill (code-owners analog); maintained by application teams, like features |
| **Boundaries** | what does this skill NOT do? | distinct triggers, scope limits in descriptions |
| **Lifecycle** | what happens over time? | semantic versioning, deprecation warnings, changelogs |
| **Coherence** | does the library still make sense at scale? | periodic audits + skill validation checks |

### Governance is the rarest step ([B049](https://youtu.be/M05vON8i0aI) QuantumBlack)
- Maturity gradient: **build → share → govern**. Poll evidence (B049): nearly
every hand up for building skills, fewer for sharing, only a few for governing
— the rarest step, as `skills_dossier.md` §4.5 records.
- The paradox that justifies governance: *without it you can't discover* — but once
  governed, coding agents **automatically reuse existing skills** instead of
  duplicating them, which self-solves most redundancy problems.
- Governance table needs architects, eng leads, infra leads, cyber leads each
  owning their domain ([B049](https://youtu.be/M05vON8i0aI)). Caveat from the same
  talk: skills are **one component** of agent workflows (alongside MCP servers,
  tools, rules) — govern the whole surface, not the skill folder in isolation.

### Security — skills are supply chain, not config ([B166](https://youtu.be/iKQ78wyJEXU) Nubank)
- Skills behave like **dependencies** (they steer code that other people's agents
  generate), not like configuration. Nubank security-reviewed **2,000 skills**
  before they reached developers.
- Top observed risks: hardcoded tokens leaking into logs, skill-injected shell
  commands, excessive permissions.
- Lesson: *"protect the whole workflow, not only the code being generated."*

### The adoption wall — most honest finding ([B261](https://youtu.be/eBUyTS7SzV4))
- *"Nobody is going to write skills for another person in a GitHub repo."* A
  top-down shared-skills repo ("scrape all the Slack, build it, we'll all use it")
  dies on day two. Updating must be **embedded in the working loop** (skillify-it
  at task end), never a separate documentation duty.
- Failure modes of neglect:
  - *"A brain nobody curates becomes a garbage dump with great search."*
  - *"A bad skill file encodes a bad process forever."*
  - Orgs that don't capture learnings *"wake up every morning with amnesia"* —
    model quality is rented; the skill library is the owned asset.

---

## 4. Organizational frame

- **A skill file is an employee** ([B261](https://youtu.be/eBUyTS7SzV4)): AI-native
  companies encode written procedures as skills and **hire/maintain engineers whose
  job is maintaining the skills** and doing what skills can't yet. Skills are
  shipped by anyone with product understanding — not just engineers
  ([B171](https://youtu.be/7jjudsEhBtM), [B049](https://youtu.be/M05vON8i0aI)).
- Cross-ref `skills_dossier.md` §4.5: the build→share→govern gradient is the same
  finding seen from the org side; governance is what differentiates a sold
  workshop from a repeated one.

## 5. Workshop module hooks (raw material)

1. **"Skills are contracts"** clinic: description-writing as routing design;
   anti-pattern-first (stale descriptions, overlapping triggers) per the
   anti-pattern-first curriculum evidence ([B135](https://youtu.be/Z-c11pV_uvU)).
2. **"Skillify it"** practicum: participants convert a repeated task into a skill
   live; capture loop as habit, not ceremony.
3. **Governance minimum viable set**: admission gate + named owners + evals on
   model upgrade — practitioner inference for the three that pay for themselves
   first (corpus names the dimensions but doesn't rank them).
4. **Security vetting lab**: token/shell/permission risk patterns from Nubank's
   2,000-skill vetting, applied to participants' own skill folders.
