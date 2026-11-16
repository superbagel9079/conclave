---
name: council
description: Three-stage debate bench that spawns lens agents in parallel: independent first opinions, anonymized peer review with rankings, then a chairman synthesis into council.md with a machine-derived pass|fix verdict and a receipt. Two rosters: verdict lenses (architect, reviewer, writer, researcher) for finished results, advisor styles (contrarian, first-principles, expansionist, outsider, executor) for open ideas. Use whenever Operator wants multiple agents debating whether a thing is good, what to improve, what to change, what is wrong.
license: MIT
user-invocable: true
---

# council, the debate bench

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

Pick one, or mix as the ask demands. Full playbooks live in
`references/lenses.md`.

| roster | lenses |
|--------|--------|
| `verdict` | architect, reviewer, writer, researcher |
| `advisor` | contrarian, first-principles, expansionist, outsider, executor |

The orchestrator is always a fifth, extra lens, **user**, but it stays on
top, reads the council, and never joins the debate.

## Three stages

1. **First opinions.** Spawn every lens in parallel, `wait:false`, fresh
   context, same input, no cross-talk. One opinion each.
2. **Review.** Each lens receives the other members' Stage 1 opinions,
   anonymized as `Member A`, `Member B`, ... in shuffled order, and ranks them
   by accuracy and insight, then restates its own verdict.
3. **Final response.** The chairman reads all Stage 2 outputs, weighs them
   through the user lens, and writes `council.md`: final verdict, the
   disagreements, the one action retained. Ship on `council.md`, never on a
   lone lens.

Exact prompt templates are in `references/lenses.md`.

## The verdict

One line per member, no prose:

```
COUNCIL: pass|fix  reason=<one line>  diff=<what to change>
```

A `fix` must be derived from a named finding (`references/rubric.md`); a `fix`
with no finding does not count. Only `COUNCIL:` lines are authoritative.

## Hard laws

- No member edits, creates, or deletes files. No code. Ever.
- Trust the finish notification. Do not poll.
- No result ships without real verdicts; an invented debate is worth zero.
- The council debates the RESULT, not the person who made it.

## Receipt

Every session closes with one machine line:

```
RECEIPT: passed=<true|false>  evidence=<files + verdicts>  diff=<gap vs request>
```