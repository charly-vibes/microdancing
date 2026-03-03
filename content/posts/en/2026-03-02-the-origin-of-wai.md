---
title: "Walk this WAI: The Origin"
date: 2026-03-02
lang: en
translations:
  es: /es/posts/el-origen-de-wai.html
---

# Walk this WAI: The Origin

There is something in the act of programming that doesn't quite click. I've been saying it [for years](https://youtu.be/ioeMeQNEgL8?si=4b66Jm53aEtlQMfr&t=99): hands are a bureaucracy of flesh that arrives late to what the head already solved three blocks ago. Without formal training, software appears as an alien labyrinth, without blueprints. But that same ignorance ends up being a machete; it allows for questioning every gesture of the ritual and seeking, out of pure survival instinct, the path of least effort. The goal was always to find a direct resonance between thought and result, without code acting as interference.

Today, the machine writes in an afternoon what used to cost months of sweat. The cost of production is zero, but the systems being produced are no better for it. The problem has shifted. Syntax no longer matters when the token tap is wide open; the risk is that volume blinds us and we lose our way. The only thing that really matters is intentionality.

## Against Human Entropy

The weakest link in any complex system is the human being. We have that habit of forgetting, of getting tired, of letting an instruction manual become dead paper within two days. It's not ill will; it's material fatigue.

Faced with this, automating is not a commercial productivity shortcut; it is pure prevention. It is shielding the software architecture against our own clumsiness. There is a rule that helps me prioritize what to do: the Rule of Three. If a manual process repeats three times, it is no longer a coincidence and is a signal that the system is screaming for you to automate it. The instruction has to be an executable command[^just]; the correct path must be the easiest to walk. Everything else is just wasting energy without sense[^humanos].

## The Vertigo of the Black Box

The first real contact with AI leaves you a bit disoriented. It returns entire files in the time it takes to brew a coffee. The instinct of those from the traditional craft is to audit every line, checking every nut and bolt for fear of error. For years, not reading your own code was pure negligence; it was malpractice.

Letting go of that reflex gives you physical vertigo. It feels like a fraud. The proposal is to embrace the machine and stop looking at the code closely[^vibecoding]. It is a painful renunciation; it means accepting that code has become a black box and that the manual skill that fed you for years is now worth much less.

But trying to read the output of an AI is useless; it's like trying to keep up with a verbose and chaotic torrent. Our job is no longer writing, but marking the edges and the context to ensure the machine operates without destroying everything around it.

## The Ethics of the Contract

Generating code is trivial. Reviewing it is hell.

When the machine hands you back a massive file with thousands of modifications, the interaction collapses. The solution has to be surgical. The premise is simple: you don't annotate the code, you annotate the behavior. Through strict documents where you define exactly what you expect to happen, chatting with the machine stops being a list of vague requests and becomes a contract[^sdd].

The focus shifts from the *how* to the *what*. Intent is audited; the machine implements and you mark the boundary.

## Diplomacy and Environment

An isolated AI is amnesiac. It is an erratic actor without historical memory. Starting a project from scratch is subjecting the machine to total disorientation.

[WAI](https://github.com/charly-vibes/wai) was born to solve that problem. It is not a tool intended for human use. It is a diplomatic treaty, an explicit operations manual for the AI to navigate the project under non-negotiable rules.

This utilizes the practice of **AIX** (AI Experience). Designing the environment assuming your primary user does not breathe. Structuring information in an orderly fashion[^para] and forcing clear rules and hard conventions[^pressure]. The environment molds the actor. If the machine hallucinates or makes systematic mistakes, the fault lies not with the artificial intelligence; it lies with the mediocre ecosystem you built for it.

## Aura, Velocity, and Pause

When the environment is shielded, harmonic coupling occurs. You describe a problem, the machine assembles, the product emerges. The distance between thought and execution becomes imperceptible. And therein lies the death trap.

Historically, code was craft work. It had friction. Today it is a mass-produced, free good. It has lost its aura[^aura]. Faced with this capacity to produce without pause, the AI Vampire appears: the idiotic impulse to use hyper-speed to spit out ten times more mediocre software[^vampire].

Building without pause is accumulating ruins at a higher speed.

The true antidote to blind automation is counter-intuitive: produce less. By delegating manual work, we recover the most expensive and scarce resource in engineering: the mental space to think. Use the time saved to doubt the architecture before starting to build. To ask if the system even deserves to exist.

The machine accelerates. The code is just the concrete. The direction, the meaning, and the responsibility remain exclusively ours.

---

[^humanos]: **Removing people from the process** is not a stance of hatred towards the human, but an extreme form of respect for our fallibility. People forget, tire, and get distracted. Leaving critical infrastructure tasks in the hands of memory is, at best, blind optimism; at worst, negligence that guarantees failure.

[^just]: [just](https://just.systems/) is a command runner that allows you to encode working recipes. The great advantage over an instruction manual is that the command is the ultimate truth: if the command fails, the system is broken. There is no room for interpretation or forgotten steps.

[^vibecoding]: The concept of *Vibe Coding* (Yegge and Kim, 2025) marks the end of the era of "cranking out code" as a core skill. The programmer shifts towards orchestration. It is a painful identity change: from being the one who "writes" to being the one who "decides" and "validates" intent.

[^sdd]: *Spec-Driven Development* (SDD) uses structured natural language files so that chatting with the AI is not a vague request but a binary contract: either the functionality meets the specification or it doesn't. No middle ground or vague requests.

[^para]: The [PARA Method](https://fortelabs.com/blog/para/) (Projects, Areas, Resources, Archives). Organizing the repository under this scheme is not just for human order; it is so the AI has a clear context map and doesn't "hallucinate" by mixing files of different natures.

[^pressure]: [BackPressure](https://ghuntley.com/pressure/), by Geoff Huntley. The idea is that the infrastructure (linters, tests, conventions) must force quality before the code is even proposed. Without this environment pressure, the machine tends towards entropy and junk code.

[^aura]: Walter Benjamin (*The Work of Art in the Age of Mechanical Reproduction*). Craft code had an aura: the trace of unique human effort and decision. AI code is mass-produced; it lacks aura. Value now lies solely in the original architectural design.

[^vampire]: [The AI Vampire](https://steve-yegge.medium.com/the-ai-vampire-eda6e4f07163), by Steve Yegge. A warning about AI burnout: using time savings to produce 10 times more digital junk. The act of resistance is to use that time to think and contemplate the system before executing it.
