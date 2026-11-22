---
name: conclave
description: "Three-stage debate bench that spawns lens agents in parallel; independent first opinions, anonymized peer review with rankings, then the chairman's synthesis into council.md with a machine-derived pass|fix verdict and a receipt. Two rosters: verdict lenses (architect, reviewer, writer, researcher) for finished results, advisor styles (contrarian, first-principles, expansionist, outsider, executor) for open ideas. Use whenever Operator wants multiple agents debating whether a thing is good, what to improve, what to change, what is wrong."
license: MIT
---

# conclave, the debate bench

The council judges a RESULT (research, plan, planning output) or an IDEA. It
critiques; it never does the work. If the result is still missing, send it back
to the builder first. A lens that starts building has stepped out of role.

## Load order (progressive disclosure)

Keep this file lean. Read the deeper files only when the stage needs them:

- `references/lenses.md`: full playbook per lens. Read BEFORE any spawn.
- `references/rubric.md`: severity, confidence, and the mechanical verdict rule.
- `references/tiebreak.md`: chairman decision rules when lenses split.
- `examples/sample-run.md`: a golden run. Read before writing `council.md`.

## Input

One of, or both:

- a path to the result file (`research.md`, `plan.md`, any finished output)
- a free prompt describing the idea or result

Every lens gets the SAME input. Access to files and sources is wide open.

## Roster

Pick a roster, or run both as the ask demands. Full playbooks live in
`references/lenses.md`.

| roster | lenses |
|--------|--------|
| `verdict` | architect, reviewer, writer, researcher |
| `advisor` | contrarian, first-principles, expansionist, outsider, executor |

The orchestrator is always an extra lens, **user**, one above the debate. It
stays on top, reads the verdicts, and never joins. The `verdict` roster is the
mechanical pass|fix engine and always runs all four lenses. The `advisor`
roster is for open ideas: its five lenses return recommendations, not a
blocking severity, and the chairman weighs them with the rules in
`references/tiebreak.md`. An advisor-only run produces a direction, not a
`pass|fix` verdict; its `council.md` records the direction and closes with a
`direction=` receipt instead of `passed=`.

## Three stages

1. **First opinions.** Spawn every lens in parallel, `wait:false`, fresh
   context, same input, no cross-talk. One opinion each.
2. **Review.** The orchestrator anonymizes the Stage 1 opinions as
   `Member A`, `Member B`, ... and shuffles the order. Each lens then ranks
   them by accuracy and insight and restates its own verdict.
3. **Final response.** The chairman reads the final-round verdicts and
   rankings, weighs them through the user lens, and writes `council.md`: final
   verdict, the disagreements, the one action retained. Ship on `council.md`,
   never on a lone lens.

If the Stage 2 verdicts still split, the chairman runs one dissent pass
(`references/tiebreak.md`), then decides. Stage 1 and Stage 2 are the two
reasoning rounds; the dissent pass is the only extra.

## Token lean

Loops cost tokens. Three rules keep a debate cheap:

1. **Fresh lenses, every round.** Spawn a new lens per round; never steer an
   old session into the next round, because retained context is re-sent and
   grows. Stage 2 and the dissent pass each use a fresh lens; the chairman
   tells the fresh Stage 2 lens which Member it was, so "restate your own
   verdict" still works with no carried session.
2. **Delta payloads.** After round 1, hand each lens only the prior `COUNCIL:`
   lines plus the disputed lines named by their `loc=` fields, never the whole
   repo.
3. **Convergence gate.** Stage 2 always runs. After it, stop the moment every
   lens returned `pass` with no finding and the chairman's confidence is at
   least 0.95.

Each lens answers in one `COUNCIL:` line only; a Stage 2 Member-letter ranking
list may sit above it, but no reasoning prose and no re-printed `COUNCIL:`
lines in the ranking.

Exact prompt templates are in `references/lenses.md`.

## The verdict

The verdict roster returns one `COUNCIL:` line per lens, no prose:

```
COUNCIL: pass|fix  sev=<critical|major|minor|nit|none>  loc=<file:line|none>  reason=<one line>  diff=<what to change>
```

`sev` is the highest severity the lens found. `loc` names the file and line
of the finding, or `none` on a clean pass or when the result is a prompt with
no file; the chairman uses it to build the round-2 delta payload. A `fix` must
carry a named finding at `critical` or `major` (`references/rubric.md`); a
`fix` with no finding does not count. Only `COUNCIL:` lines are authoritative.
The advisor roster returns a `steer` line instead, no `pass|fix`, no `sev`
(`references/lenses.md`).

## Hard laws

- No member edits, creates, or deletes files. No code. Ever.
- Trust the finish notification. Do not poll.
- No result ships without real verdicts; an invented debate is worth zero.
- The council debates the RESULT, not the person who made it.

## Receipt

Every verdict-roster session closes with one machine line:

```
RECEIPT: passed=<true|false>  evidence=<files + verdicts>  diff=<gap vs request>
```

An advisor-only session closes with a direction line instead:

```
RECEIPT: direction=<one line>  evidence=<steer lines>  diff=<what to try>
```