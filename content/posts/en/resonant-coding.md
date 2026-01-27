---
title: "Resonant Coding: or How I Learned to Stop Worrying and Love the Chaos"
date: 2026-01-25
lang: en
translations:
  es: /es/resonant-coding
---

<nav class="progress-nav"><a href="#s1">1</a> <a href="#s2">2</a> <a href="#s3">3</a> <a href="#s4">4</a> <a href="#s5">5</a> <a href="#s6">6</a> <a href="#s7">7</a> <a href="#s8">8</a></nav>

*This post is a cover of [Sasha's](https://ak.saxa.xyz/2026/01/25/resonant-coding-en.html) ideas.*

There's a phenomenon that occurs when you stare too long at a screen full of code you don't understand[^foreign-code]. The brain starts doing something similar to what it does when you look at clouds: it searches for patterns, faces, familiar shapes. Except instead of seeing a rabbit or your Aunt Martha's profile, you start seeing intentions. Purpose. A logic that surely must be there, that has to be there, because someone—or something—wrote it with some goal in mind. The problem is when that something is a language model and the goal was simply to generate the most probable sequence of characters given an input, which, if you stop to think about it with the seriousness it deserves, is a rather disturbing way to create the instructions that will move money, control systems, decide things.

This is not paranoid exaggeration[^paranoia]. Or maybe it is. But during the months I spent leading a development team—a new team, built from scratch to support a department that handled numbers with many zeros—that paranoia became something resembling a methodology, or at least something that worked better than having nothing, which was exactly what we had before.

<span class="progress-marker" id="s1">⸻ 1/8 ⸻</span>

The context, because context always matters even when you'd prefer it didn't: there was pressure from above to use Artificial Intelligence and accelerate everything[^pressure]. The team had few experienced developers, which meant I had to review almost everything. And when I say "almost everything" I mean that particular situation where every *pull request*[^pr] that arrived was like opening a Pandora's box manufactured by a statistical oracle that had read the entire internet but hadn't necessarily understood any of what it read[^understanding].

The first months were a slow-motion disaster. Code that at first glance seemed reasonable but, upon examination, revealed structures that no human programmer would have chosen. Solutions that worked but for the wrong reasons. Patterns that smelled like something, but you didn't know what until they exploded in production at the worst possible moment, at which point you discovered that the model had interpreted "validate user input" as "assume the user always sends perfect data and pray."

There was a moment—and this is important for understanding why I eventually stopped trusting in magical solutions—where the quality of code the team delivered improved dramatically. For approximately forty-eight glorious hours I thought we had achieved something. That the method we'd been refining was working. That we were, finally, good at this.

Then I discovered that Cursor had updated.

It wasn't us. It was the model. And if the model could improve without our intervention, it could also get worse. Or change in ways we didn't understand. Or be replaced by another model with other idiosyncrasies we'd have to learn from scratch. We were building on quicksand and celebrating every time the sand, for a moment, stopped shifting[^quicksand].

<span class="progress-marker" id="s2">⸻ 2/8 ⸻</span>

I have to make a detour here because without this detour nothing that follows will make sense, and besides it's the kind of detour I enjoy because it involves waves, and waves are beautiful in a way that code rarely manages to be[^waves-beautiful].

One night, at three in the morning, in one of those YouTube rabbit holes where you end up without knowing how[^rabbit-hole], I found a video of a physics demonstration[^station]. Someone grabs a rope—or a string, or something like that—and starts shaking it. At first it's pure chaos. Formless movement, waves crashing into each other, destructive interference everywhere. But if you find the right frequency, if you shake at exactly the necessary rhythm, something extraordinary happens: chaos organizes itself. Points that don't move appear—the nodes—and points that oscillate at maximum—the antinodes. Standing waves. Patterns that sustain themselves because the system has entered resonance.

I probably watched that video more times than I'd admit in public. The idea that chaos contains latent structures waiting for someone to find the right frequency to reveal them. That disorder is not the absence of order but potential order seeking to manifest[^potential].

And years later, while looking at another incomprehensible *pull request* and wondering how the hell we were going to get out of this swamp, I remembered the standing waves. And I thought: maybe the problem isn't the AI. Maybe the problem is that we're shaking the rope at any frequency and expecting patterns to appear.

<span class="progress-marker" id="s3">⸻ 3/8 ⸻</span>

Language models, for those who haven't had the pleasure of interacting with them beyond the occasional chat, are essentially text prediction machines. This sounds simple and in a sense it is: you give them a sequence of words and they return the most probable word that follows. Like your phone's autocomplete but trained on an amount of data that's difficult to conceptualize without resorting to astronomical metaphors[^data].

The problem is that this fundamental simplicity generates emergent behaviors that seem like intelligence, that sometimes function as intelligence, but that aren't intelligence in any sense that a philosopher of mind would find satisfactory[^philosopher]. They're simulacra of reasoning built from statistical patterns. And this has very concrete practical consequences:

They have no memory. Every time you talk to them it's like the first time. The model that helped you solve a bug five minutes ago has no idea you exist, or that there was a bug, or that you solved it together. What some tools call "memory" is actually a trick: they save part of the previous conversation and silently paste it at the beginning of each new message. It's prosthetic, artificial memory, and it has limits[^memory].

Their attention is limited. They have a context window—the amount of text they can process at once—and the longer the input, the worse they perform. The best way to think about this is to imagine you have a bucket of water and you need to wash dishes[^bucket]. For one dish, the bucket is more than enough. For ten, the water starts getting cloudy. For a hundred, the water is so dirty that the last dishes come out worse than they went in. And if at any point you throw something greasy into the bucket—irrelevant information, context that doesn't apply—the water becomes unusable for everything that follows. Moreover, the degradation isn't uniform: the beginning and end of the context receive more attention than the middle, which explains why sometimes the model "forgets" instructions you gave it three paragraphs earlier[^attention].

They're probabilistic. For the same input they can give different outputs. This sounds minor but has profound implications: you can't trust that a result that worked once will work again. Each interaction is a die being rolled, and sometimes you get seven and sometimes you get a snake that eats your prompt[^dice].

<span class="progress-marker" id="s4">⸻ 4/8 ⸻</span>

At some point during winter, during a vacation I spent reading instead of resting because apparently I have a dysfunctional relationship with free time, I found two lines of thought that eventually converged into what I now call Resonant Coding. One came from Steve Yegge, a programmer who's been writing about software for decades with a mix of technical brilliance and opinions that oscillate between visionary and deliberately provocative[^yegge]. The other came from Dex Horthy and his concept of Context Engineering, which is basically the idea that the context you give a model matters more than anything else[^context].

From Yegge I took something he calls the Rule of 5, which isn't so much a rule as an iterative refinement process. The simplified version is: when you generate something, you pass it through five successive filters. First a draft where what matters is that everything is there, even if it's messy. Then a correctness review where you fix factual errors. Then clarity, where you simplify and eliminate ambiguities. Then edge cases, where you think about everything that could go wrong. And finally excellence, where you polish and optimize[^five].

From Horthy I took the obsession with context. The formalization of what I already intuited with the bucket metaphor: that the quality of what you give the model determines the quality of what it gives you back, and that if the problem is too big for a single bucket, you have to divide it into smaller parts and use clean water for each one.

These two sets of ideas, combined with the professional desperation I already mentioned and a moderate amount of caffeine, crystallized into something that seemed to work. We didn't invent anything new—we simply glued two existing frameworks together and gave them a pretentious name—but sometimes innovation is exactly that: seeing that two pieces fit when nobody had put them together before.

<span class="progress-marker" id="s5">⸻ 5/8 ⸻</span>

I'm not going to describe the method as a numbered series of steps because that would betray the spirit of how it actually works, which is more chaotic, more iterative, more like a spiral than a staircase. But there are three general movements that repeat:

First there's what we might call research—this step comes directly from Horthy's Context Engineering framework[^context]—though "reconnaissance" better captures the feeling. Before doing anything, you need to understand the problem. And this is where the model can help: you ask it to investigate the existing code, map dependencies, find relevant documentation, tell you what the hell is going on in this system you inherited from someone who no longer works here[^legacy]. The model does this work pretty well because it's essentially reading and synthesis, which is exactly what it was trained for.

But—and this but is crucial—the document the model generates has to be reviewed. Not accepted, reviewed. With the Rule of 5 or something similar, it doesn't matter, but with the firm conviction that the model may have misunderstood, may have invented things, may have mixed information from different projects because in its training it read similar code and got its wires crossed[^hallucinations]. Human review here is not optional; it's the entire point of the exercise.

Then comes something like planning, which is using the research document (already reviewed) to generate an action plan. The trick here is that each task in the plan has to be small enough to fit in a single bucket. If a task is "implement the authentication system," it's too big. If it's "add JWT token validation to the login endpoint," we're better off. And each of these small tasks goes, again, through the Rule of 5, because a poorly defined plan can generate thousands of lines of incorrect code and by that point it's too late[^late].

And finally there's implementation, which by this point should be almost mechanical. Each task is so well defined that the model has no room to invent. And this is where models truly shine: they can edit twenty files in seconds, create test batteries, refactor entire structures. What would take a human hours. But only because the hard work—the thinking—was already done before[^thinking].

<span class="progress-marker" id="s6">⸻ 6/8 ⸻</span>

There's something that deeply bothers me about the dominant narrative around AI in programming, which is the idea that these tools let you "go faster." It's not exactly false, but it's also not true in the way it's usually presented. It's like saying a car lets you get to your destination faster: true, but only if you know how to drive, if you know the way, if the car is in good condition, if the roads are clear. If those conditions aren't met, the car can take you very quickly anywhere, including off a cliff[^cliff].

The same happens with AI. Yes, it can generate code faster than any human could write it. But generating code is not the same as solving problems. And if you generate code without understanding the problem, what you get is a quick solution to the wrong question, which is worse than having no solution because now you have to undo what you did before you can move forward.

The method I describe is not a shortcut. It's a process that takes more time than throwing a prompt at the model and hoping something good comes out. But that time is recovered multiplied because errors are detected early, because work doesn't have to be redone, because when something is implemented you already know it's correct[^correct].

<span class="progress-marker" id="s7">⸻ 7/8 ⸻</span>

For a while I doubted the name. "Resonant Coding" sounds pretentious, I know. There were alternative versions: "Structured Prompting," which was too generic; "Context-First Development," which sounded like a management consultancy; "The Bucket Method," which was too literal and besides nobody was going to take seriously something called that[^naming].

But I kept coming back to the image of standing waves. To the idea that there's a right frequency waiting to be found. To the difference between shaking the rope chaotically and shaking it with precision.

The "Vibe Coding" that became popular[^vibe] proposes something like going with the flow, trusting the model, iterating until something works. I'm not saying it's useless—there are situations where that approach is perfectly valid—but for serious work, for systems that have to function, for code that's going to be maintained by other humans, you need something more rigorous. You need to find the resonance[^resonance].

<span class="progress-marker" id="s8">⸻ 8/8 ⸻</span>

I should probably close with some elegant conclusion but the truth is I don't have one. What I have is a process that works better than having no process, that can be refined, that generates reusable artifacts[^artifacts], that forces you to think before acting. It's not perfect. There are days when everything fails anyway. There are models that resist cooperating. There are problems that are genuinely difficult and no method makes them easy.

But when it works—when the context is well constructed, when the plan is well defined, when each task fits in its bucket and the water is clean—there's a moment where everything clicks. Where the model does exactly what you need it to do. Where the code it generates is the code you would have written yourself, only faster and probably with fewer errors.

In those moments you understand, viscerally, what it means to find the right frequency.

And then, invariably, the next incomprehensible *pull request* arrives, and you have to start again.

---

## Appendix: The Method in Practice

Everything above sounds good in theory, but theory has that annoying particularity of dissolving when it touches reality. So here's how this materializes in day-to-day work, with the caveat that any system that claims to be definitive is doomed to fail, and this one is no exception[^system].

What follows is an expansion of the three-step method—research, planning, implementation—with the additional structures we discovered we needed as we applied it to real projects.

The first decision was structural: if context is a bucket that gets dirty, then you need separate buckets for each type of water. In practice this translates to folders with specific functions[^folders]:

- `research/` for research documents, named with dates to track the evolution of understanding
- `plans/` for implementation plans, also dated, also versioned
- `specs/` for formal specifications in Gherkin format[^gherkin], which function as living documentation and executable tests at the same time
- `handoffs/` for handoff documents between sessions, because the model doesn't remember anything and someone has to remember for it

The second decision was procedural: before writing code, write a plan. Always. Without exception. The plan divides work into phases that can be completed in a reasonable amount of time, with explicit success criteria—automated when possible, manual when there's no other option. Each phase is a clean bucket: the model receives only the plan for that phase and relevant information, nothing more.

For tasks with architectural risk—those where you don't know if the solution you imagine will work until you try it—we use what's called a *tracer bullet*[^tracer]: a minimal implementation that traverses the entire system end to end, without polish, without optimization, just to verify that the parts connect as we expected. It's cheaper to discover that your architecture doesn't work when you have a hundred lines of code than when you have ten thousand.

The third decision was about memory. Models don't remember, but files do. At the end of each work session—or when you need to pass context to another person, or another model, or your future self—a *handoff* document is generated that captures the current state: what was done, what was learned, what's pending, what files are relevant. It's externalized prosthetic memory, and it works better than it has any right to[^handoff].

For design decisions that aren't obvious—when there are multiple possible paths and choosing one means discarding others—we maintain a `debates/` folder where the options considered are documented, the pros and cons of each, and the reason why what was chosen was chosen. This seems like bureaucracy until, six months later, someone asks "why did you do it this way?" and the answer is written instead of lost in the head of someone who no longer works here[^debates].

The typical flow ends up being something like this:

1. A requirement arrives. Before touching code, a research document is created. The model reads the existing code, documentation, whatever exists, and generates a summary of the current state. That summary goes through the Rule of 5 until it's reliable.

2. With the research document as input—and only that document, in a new conversation, with a clean bucket—a plan is generated. The plan divides work into phases, each phase has success criteria, each task is small enough to fit in a single bucket. The plan also goes through the Rule of 5.

3. Implementation happens phase by phase, each in its own conversation, each validated before moving to the next. If something doesn't work, the plan is adjusted, not improvised.

4. At the end of the session, the handoff is generated. Whoever picks up the work next—whether human or model—has all the context they need.

There's a constant temptation to skip steps, to go straight to code because "this is simple" or "I already know how to do it." Sometimes it works. More often than I'd like to admit, it doesn't, and the time you saved skipping steps you lose multiplied fixing what went wrong. The method is slower at the beginning and faster at the end. The question is whether you have the patience to reach the end[^patience].

---

## Notes

[^foreign-code]: Other people's code, like a doctor's handwriting, operates under the implicit assumption that someone at some point knew what it meant. This assumption is frequently incorrect.

[^pressure]: "Accelerate" is one of those words that in corporate contexts simultaneously means everything and nothing. It can mean "produce more" or "spend less" or "fire people" or "adopt the trendy technology" or some combination of the above. In this case it meant "use AI for everything" without much clarification on what "everything" was or how success was measured.

[^paranoia]: The distinction between paranoia and reasonable caution has become blurry in recent years. Maybe it always was and we only now have vocabulary to discuss it. Or maybe reality has become strange enough that paranoia is the correct adaptive response.

[^pr]: A *pull request*, for the fortunate souls who don't work in software, is the mechanism by which someone proposes changes to code and others review them before accepting. In theory it's an orderly process of collective validation. In practice it's where interpersonal relationships, expectations of reasonable hours, and any illusion that programming is a rational discipline go to die.

[^understanding]: There's a genuine philosophical debate about whether language models "understand" anything or simply process statistical patterns in a way that simulates understanding. My personal position, which I won't defend in detail because this is already a long text, is that the question is poorly formulated: human "understanding" is probably also pattern processing, just on a different substrate. This doesn't resolve anything but at least distributes the mystery more equitably.

[^quicksand]: The feeling of building on quicksand is not exclusive to working with AI. It is, I would venture to say, the fundamental condition of any technical work in the 21st century. Frameworks change, languages evolve, "best practices" from three years ago are today's antipatterns. The difference with AI is the speed: what used to change in years now changes in months.

[^waves-beautiful]: I'm not going to try to explain why waves are beautiful because that would require a separate essay on aesthetics and physics, and this text already has too many digressions. But trust me: they're beautiful. Search "standing waves" on YouTube and lose half an hour. It's worth it.

[^rabbit-hole]: YouTube's recommendation algorithm is, in a sense, the original language model: a prediction machine optimized to keep you watching. At three in the morning, when defenses are down and willpower is an abstract concept, the algorithm wins. It always wins.

[^station]: The specific video was of something called "Estación de Ondas" (Wave Station), a demonstration from Physics Week at UBA (University of Buenos Aires). [Here it is](https://www.youtube.com/watch?v=6zBknO95rB4). I don't know how I got there from whatever I was watching before. I probably started with something about cooking or music. That's how the rabbit hole works.

[^potential]: This idea—that disorder contains latent order—appears in so many different contexts that it's probably one of those fundamental truths about how the universe works, or at least about how our perception of the universe works. From thermodynamics to chaos theory, from crystallography to biological evolution, there are structures emerging from what appears to be noise. The trick is always finding the right conditions for the structure to manifest.

[^data]: According to [leaked information later confirmed by Microsoft](https://the-decoder.com/gpt-4-architecture-datasets-costs-and-more-leaked/), GPT-4 was trained on approximately 13 trillion tokens, which is equivalent to about 10 trillion words. To put this in perspective: if you read a book a day from birth until death, you wouldn't come close. The [Library of Congress](https://www.loc.gov/about/general-information/) has approximately 25 million catalogued books. Current models have "read" orders of magnitude more than that. Which doesn't mean they understood anything they read, but that's another problem.

[^philosopher]: Philosophers of mind have been discussing what it means to "understand" and "be conscious" for decades. They haven't reached any consensus. What they have established is that the question is much harder than it seems, and that anyone who gives you a simple answer probably hasn't thought enough about the problem.

[^memory]: The prosthetic memory of language models has a hard limit: the context window. When the accumulated "conversation" exceeds that limit, you have to trim. Which means deciding which parts of the memory to keep and which to discard. There are sophisticated systems for doing this—automatic summaries, semantic vectorization, embedding databases—but they're all approximations. Something is always lost.

[^attention]: This phenomenon is documented in the paper ["Lost in the Middle: How Language Models Use Long Contexts"](https://arxiv.org/abs/2307.03172) by Liu et al. (2023). The short version is that models pay more attention to the beginning and end of context, and tend to "forget" what's in the middle. This has obvious practical implications: if you want the model to pay attention to something, put it at the beginning or end, not in the middle.

[^dice]: The die metaphor is imperfect because dice are uniformly random, while language models have complex and non-uniform probability distributions. But it captures the essence: the result isn't determined beforehand, and the same input can produce different outputs.

[^yegge]: Steve Yegge worked at Amazon and Google, wrote some of the most influential (and inflammatory) posts about engineering culture, and has the particularity of combining genuinely brilliant insights with takes so hot they generate flame wars for weeks. His Rule of 5 is buried in a [GitHub repository](https://github.com/steveyegge/gastown/blob/main/internal/formula/formulas/rule-of-five.formula.toml) that few people read, which is a shame.

[^context]: Horthy's Context Engineering document is [publicly available](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) and is probably the best introduction to the topic that exists. Warning: it's technical, detailed, and once you start reading it's hard to stop.

[^five]: The five steps—draft, correctness, clarity, edge cases, excellence—don't always have to be applied in that order or always completely. Sometimes a document needs more work on clarity than correctness. Sometimes the edge cases are obvious and the effort needs to go elsewhere. The point is to have a review structure, not to follow it blindly.

[^bucket]: This metaphor came to me during a conversation about camping. We were discussing the logistics of washing dishes in the field and someone mentioned that with limited water you have to be strategic: glasses first, then plates, greasy pots last. And suddenly everything clicked. A language model's context works exactly the same: you have to be strategic about what you put in and in what order, because once the water gets dirty there's no going back.

[^legacy]: Legacy code—the term in the jargon—is the euphemism we use to refer to code that someone wrote before, that nobody fully understands, and that nobody dares to touch for fear of breaking something. Every software company old enough has mountains of legacy code. It's like geological strata: you can see the organization's history in the layers of questionable technical decisions.

[^hallucinations]: The "hallucinations" of language models—when they generate incorrect information with total confidence—are probably the hardest problem to solve because they're hard to detect. An obvious error jumps out at you. Subtly incorrect information can pass all checks and explode months later. It's like a semantic time bomb.

[^late]: There's a saying that circulates in the programming community, of uncertain origin: "Weeks of coding can save you hours of planning." It's sarcastic, obviously, but it captures a profound truth about how we tend to underestimate planning and overestimate our ability to fix things on the fly.

[^thinking]: The paradox of using AI for programming is that the work it automates—writing code—is relatively easy, while the work it doesn't automate—deciding what code to write—is the genuinely difficult part. Models can generate implementations, but they can't generate requirements. They can write solutions, but they can't understand problems. At least not yet. Although "yet" is an increasingly loaded word in this context. There's an insight from [Dex Horthy](https://www.youtube.com/watch?v=42AzKZRNhsk) that I find fundamental: now that most of our work is reviewing what the AI generates instead of writing from scratch, we need tools for *editing*—leaving comments, striking through, marking as unclear—instead of tools for *writing*. From that frustration [fabbro](https://github.com/charly-vibes/fabbro) was born, a code annotation tool for structuring feedback to models.

[^cliff]: This is not a theoretical metaphor. I've seen projects where the speed of code generation exceeded the capacity for review, and the result was a system nobody understood, nobody could maintain, and that eventually had to be discarded and rewritten from scratch. Speed without direction is just a faster way to get lost. In an upcoming post about what I'm provisionally calling [Resonant Development](/en/resonant-development) I want to explore how to combine these ideas with *spec-driven development* to attack exactly this problem: how to scale review when code grows faster than any human can read.

[^correct]: "Correct" is a complicated word in software. Correct according to what specification? According to what use cases? Correct now or correct when conditions change? The method I describe doesn't resolve these ambiguities, but at least it makes them explicit. And making ambiguities explicit is the first step to resolving them.

[^naming]: The process of naming things is, according to the [famous Phil Karlton quote](https://martinfowler.com/bliki/TwoHardThings.html) that has circulated since the 90s, one of the two hardest things in computer science (the other is cache invalidation). The off-by-one errors bit is a later addition by Leon Bambrick. That there are three things is part of the joke.

[^vibe]: The term "Vibe Coding" was coined by Andrej Karpathy in a tweet, but the concept was developed in depth in the book [*Vibe Coding*](https://itrevolution.com/product/vibe-coding-book/) by Steve Yegge and Gene Kim. I'd been experimenting with CHOP (Chat Oriented Programming) since Steve's video came out a year earlier, so I was anxiously awaiting the book's release. That it happened to fall on my birthday felt like a sign from the universe. When it came out I could barely tear my eyes from the screen; I nearly blew out my birthday candle with the Kindle still in my hand. The book is excellent and worth reading, although my methodology goes in a slightly different direction.

[^resonance]: There's something deeply satisfying about the idea that working well with a tool is finding its resonance frequency. It implies that the tool has a correct way of being used, that it's not arbitrary, that it can be discovered. It's an optimistic vision, perhaps naively optimistic, but it's the one that lets me keep doing this.

[^artifacts]: The "artifacts" the process generates—research documents, action plans, refined prompts—have value beyond their immediate use. They can be reused, adapted, serve as a base for future projects. It's a form of intellectual capital that accumulates. This is important because it means the time invested isn't lost: it's invested. I maintain a collection of these prompts at [incitaciones](https://github.com/charly-vibes/incitaciones), in case it's useful as a starting point for anyone.

[^system]: Every work system is a hypothesis about how the world functions. Like any hypothesis, it should be subject to revision when evidence contradicts it. The problem is that humans become attached to our systems and defend them beyond reason. I try to remind myself of this regularly. I don't always succeed.

[^folders]: Folder structure seems like a minor detail until you have to find something you wrote three months ago and can't find it. Naming things with dates in `YYYY-MM-DD` format at the beginning of the name has the advantage that they sort chronologically automatically, which sounds trivial until it saves you twenty minutes of searching.

[^gherkin]: Gherkin is a format for writing specifications in near-natural language that can be executed as tests. The structure is "Given-When-Then" and forces you to think in terms of observable behavior instead of internal implementation. It's one of those cases where the format's constraint improves the quality of thinking. To test spec-driven development I asked the AI to describe the features of [fabbro](https://github.com/charly-vibes/fabbro) following this format, and I ended up creating [nayra](https://github.com/charly-vibes/nayra)—a project I always wanted to have—specifically to explore more formal tools like [OpenSpec](https://github.com/humanlayer/openspec).

[^tracer]: The term "tracer bullet" comes from ballistics: tracer rounds leave a visible trail that allows adjusting aim in real time. In development, a tracer bullet is a minimal implementation that traverses all layers of the system to verify that the architecture works before investing in building it well. The idea comes from the book *The Pragmatic Programmer* by Hunt and Thomas, which by now is almost a classic.

[^handoff]: The handoff document is, in a sense, a letter you write to your future self. Or to another person. Or to a model that will pick up your work. The key is to include not only what you did but what you learned: the dead ends you explored, the decisions you made, the things that surprised you. The context that seems obvious today will be completely opaque in two weeks.

[^debates]: Documenting design decisions is one of those practices everyone knows they should do and almost nobody does. The usual reason is "there's no time." The irony is that the time you don't invest documenting you spend multiplied six months later trying to reconstruct the reasoning from scratch.

[^patience]: Patience is probably the most underestimated skill in software development. Not passive patience of waiting for things to happen, but active patience of doing things well even if it takes longer. It's difficult because everything conspires against it: deadlines, pressure, the illusion that "this time it'll work out" even though the last ten times it didn't. The method doesn't give you patience, but at least it gives you a structure where patience makes sense. To practice without the pressure of a real project, I started [jams](https://github.com/charly-vibes/jams): simple, self-contained web applications, perfect for testing the complete flow without risking anything important.
