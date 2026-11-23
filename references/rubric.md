# Rubric: severity, mechanical verdict, unverified list

The chairman does not decide the `result` verdict by feel. It is computed from
the findings, so it can never disagree with the evidence.

## Severity

| level | meaning | consequence |
|-------|---------|-------------|
| none | no finding | `pass` |
| critical | false claim, wrong number that breaks the result, unsafe step, missing dependency that halts it | `fix` |
| major | a concrete failure in real conditions: the lens names what breaks and when | `fix` |
| minor | phrasing, order, a gap that does not change the outcome | recommendation, never blocks |
| nit | style only | recommendation, never blocks |

A `major` with no named failure ("could be clearer", "might not scale") is
read as `minor`. Critics always find something; the failure scenario is what
separates a real block from a reflex.

## Mechanical verdict (`result` mode)

Read `sev` from each lens's final-round `COUNCIL:` line, never from prose.
Stage 1 lines count only when Stage 2 was skipped, or for the writer, which
is not re-run.

- Any valid `critical` or `major` from architect, reviewer, or researcher ⇒ `fix`.
- The writer caps at `minor`: it never blocks a structural pass.
- Only minor or nit findings ⇒ `pass`.

A finding is valid when its verbatim quote is found in the input (the
chairman greps it) and, for a `major`, it names what breaks and when. A quote
the grep does not find voids the finding, whatever its severity.

Retained actions: every distinct `critical` or `major` diff, none dropped.
Minor and nit diffs are listed as recommendations.

## Unverified list (every mode)

There is no confidence score. A number the chairman estimates for itself is
checked against nothing, and a threshold on it hides what was not checked.
Instead `council.md` lists what nobody verified, built from what the lenses
report, not from what the chairman believes:

- the union of every lens's `unchecked=` field
- a finding voided because its quote was not found
- a split the chairman broke by precedence, not by evidence
- in `research` mode, every claim the verifier marked `unsourced` or `unreachable`
- a lens that omitted `unchecked=`: its whole verdict goes on the list

An empty list means no lens reported a gap. It is not proof of safety: lenses
on one model share blind spots, which is what strong mode is for. A non-empty
list is not a block; it tells Operator exactly where to look first.
