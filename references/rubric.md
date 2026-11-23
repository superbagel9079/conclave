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
Stage 1 lines count only when Stage 2 was skipped.

- Any valid `critical` or `major` from architect, reviewer, or researcher ⇒ `fix`.
- The writer caps at `minor`: it never blocks a structural pass.
- Only minor or nit findings ⇒ `pass`.
- A `fix` without a verbatim quote does not count.

Retained actions: every distinct `critical` or `major` diff, none dropped.
Minor and nit diffs are listed as recommendations.

## Unverified list (every mode)

There is no confidence score. A self-estimated number is not calibrated, and
a threshold on it only hides what was not checked. Instead `council.md` lists
what nobody verified:

- a claim no lens checked against a source or a line
- a finding only one lens raised, with no quote or source behind it
- a split the chairman broke by precedence, not by evidence
- in `research` mode, every claim the verifier marked `unsourced`

An empty list is the ship signal. A non-empty list is not a block; it tells
Operator exactly where to look before relying on the result.
