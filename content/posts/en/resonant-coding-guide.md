---
title: "Resonant Coding: Practical Guide"
date: 2026-01-25
lang: en
---

Everything above sounds good in theory, but theory has that annoying particularity of dissolving when it touches reality. So here's how this materializes in day-to-day work, with the caveat that any system that claims to be definitive is doomed to fail, and this one is no exception[^system].

This document is an expansion of the three-step method—research, planning, implementation—described in [Resonant Coding](/en/resonant-coding), with the additional structures we discovered we needed as we applied it to real projects.

## Folder Structure

The first decision was structural: if context is a bucket that gets dirty, then you need separate buckets for each type of water. In practice this translates to folders with specific functions[^folders]:

- `research/` for research documents, named with dates to track the evolution of understanding
- `plans/` for implementation plans, also dated, also versioned
- `specs/` for formal specifications in Gherkin format[^gherkin], which function as living documentation and executable tests at the same time
- `handoffs/` for handoff documents between sessions, because the model doesn't remember anything and someone has to remember for it

## Procedure

The second decision was procedural: before writing code, write a plan. Always. Without exception. The plan divides work into phases that can be completed in a reasonable amount of time, with explicit success criteria—automated when possible, manual when there's no other option. Each phase is a clean bucket: the model receives only the plan for that phase and relevant information, nothing more. For tasks with architectural risk, we sometimes use *tracer bullets*[^tracer].

## Memory

The third decision was about memory. Models don't remember, but files do. At the end of each work session—or when you need to pass context to another person, or another model, or your future self—a *handoff* document is generated that captures the current state: what was done, what was learned, what's pending, what files are relevant. It's externalized prosthetic memory, and it works better than it has any right to[^handoff].

## Design Decisions

For design decisions that aren't obvious—when there are multiple possible paths and choosing one means discarding others—we maintain a `debates/` folder where the options considered are documented, the pros and cons of each, and the reason why what was chosen was chosen. This seems like bureaucracy until, six months later, someone asks "why did you do it this way?" and the answer is written instead of lost in the head of someone who no longer works here[^debates].

## Typical Flow

The typical flow ends up being something like this:

1. A requirement arrives. Before touching code, a research document is created. The model reads the existing code, documentation, whatever exists, and generates a summary of the current state. That summary goes through the Rule of 5 until it's reliable.

2. With the research document as input—and only that document, in a new conversation, with a clean bucket—a plan is generated. The plan divides work into phases, each phase has success criteria, each task is small enough to fit in a single bucket. The plan also goes through the Rule of 5.

3. Implementation happens phase by phase, each in its own conversation, each validated before moving to the next. If something doesn't work, the plan is adjusted, not improvised.

4. At the end of the session, the *handoff* is generated. Whoever picks up the work next—whether human or model—has all the context they need.

There's a constant temptation to skip steps, to go straight to code because "this is simple" or "I already know how to do it." Sometimes it works. More often than I'd like to admit, it doesn't, and the time you saved skipping steps you lose multiplied fixing what went wrong. The method is slower at the beginning and faster at the end. The question is whether you have the patience to reach the end[^patience].

---

## Notes

[^system]: Every work system is a hypothesis about how the world works. Like any hypothesis, it should be subject to revision when the evidence contradicts it. The problem is that we humans get attached to our systems and defend them beyond what is reasonable. I try to remind myself of this regularly. I don't always succeed.

[^folders]: The folder structure seems like a minor detail until you have to find something you wrote three months ago and can't find it. Naming things with dates in `YYYY-MM-DD` format at the beginning of the name has the advantage of ordering them chronologically automatically, which sounds trivial until it saves you twenty minutes of searching.

[^gherkin]: Gherkin is a format for writing specifications in almost-natural language that can be executed as tests. The structure is *Given-When-Then* and it forces you to think in terms of observable behavior instead of internal implementation. It's one of those cases where the constraint of the format improves the quality of thought. There's an insight from [Dex Horthy](https://www.youtube.com/watch?v=42AzKZRNhsk) that I find fundamental: now that most of our work is reviewing what the AI generates instead of writing from scratch, we need tools for *editing*—leaving comments, striking through, marking as unclear—instead of tools for *writing*. Out of that frustration was born [fabbro](https://github.com/charly-vibes/fabbro), a tool I'm developing to annotate code and structure feedback to models. To test *spec-driven development*, I asked the AI to describe its functionalities following the Gherkin format, and I ended up creating [nayra](https://github.com/charly-vibes/nayra)—a project I always wanted to have—specifically to explore more formal tools like [OpenSpec](https://github.com/humanlayer/openspec).

[^tracer]: The term *tracer bullet* comes from ballistics: tracer bullets leave a visible trail that allows for real-time aim adjustment. In development, a *tracer bullet* is a minimal implementation that cuts across all layers of the system to verify that the architecture works before investing in building it out properly. The idea comes from the book *The Pragmatic Programmer* by Hunt and Thomas. For tasks with architectural risk—those where you don't know if the solution will work until you try it—it's cheaper to find out your architecture doesn't work when you have a hundred lines of code than when you have ten thousand.

[^handoff]: The handoff document is, in a sense, a letter you write to your future self. Or to another person. Or to a model that will pick up your work. The key is to include not only what you did but what you learned: the dead ends you explored, the decisions you made, the things that surprised you. The context that seems obvious today will be completely opaque in two weeks.

[^debates]: Documenting design decisions is one of those practices that everyone knows they should do and almost nobody does. The usual reason is that "there's no time." The irony is that the time you don't invest in documenting, you spend multiplied six months later trying to reconstruct the reasoning from scratch.

[^patience]: Patience is probably the most underestimated skill in software development. Not the passive patience of waiting for things to happen, but the active patience of doing things right even if it takes longer. It's difficult because everything conspires against it: the deadlines, the pressure, the illusion that "this time it will work out" even though the last ten times it didn't. The method doesn't give you patience, but at least it gives you a structure where patience makes sense. To practice without the pressure of a real project, I started [jams](https://github.com/charly-vibes/jams): simple, self-contained web applications, perfect for testing the full flow without risking anything important.
