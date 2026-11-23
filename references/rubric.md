# Rubric: severity, confidence, mechanical verdict

The chairman does not decide the verdict by feel. The verdict is computed from
the findings, so it can never disagree with the evidence.

## Severity

| level | meaning | consequence |
|-------|---------|-------------|
| none | no finding | `pass`, never blocks |
| critical | false claim, wrong number that breaks the result, unsafe step, missing dependency that halts it | `fix`, blocks ship |
| major | a hole the result papers over, a weak instruction that will derail it in real conditions | `fix` |
| minor | phrasing, order, a nit that does not change the outcome | `pass`; two lenses agreeing record a recommendation, never a block |
| nit | style only | never blocks |

## Mechanical verdict

Severity is read from each `COUNCIL:` line's `sev` field, never inferred from
the `reason` prose. Count each lens once, from its final-round `COUNCIL:`
line; Stage 1 lines are context for the review, not votes.

- Any **critical** finding from the reviewer, researcher, or architect ⇒
  `fix`, no discussion.
- Any **major** finding from the reviewer, researcher, or architect ⇒ `fix`.
- The writer caps at `minor`: a writer finding never blocks a structural pass.
- Only minor/nit findings ⇒ `pass`.
- Two or more lenses naming the same `diff` independently ⇒ that is the action
  retained. If the shared finding is only minor, it is recorded as a
  recommendation, not a block.

A `fix` without a named finding does not count. The verdict cannot contradict
the evidence: if the findings are critical, the verdict is `fix`.

## Confidence

Confidence is the chairman's estimate that the retained action is correct,
from 0 to 1. Raise it when:

- multiple lenses name the same finding independently (+)
- the finding is quoted from a source or a specific line (+)
- a lens changes `pass` to `fix` after Stage 2 review (+)
- Stage 2 rankings put the same finding first (+)
- a second, different model names the same finding (strong mode) (+)

Lower it when:

- the lenses split and the chairman had to break the tie (-)
- the deciding finding comes from a single lens with no source (-)

Report confidence with the verdict in `council.md`. The ship gate is 0.98:
at or above it the skill stops after Stage 2; below it a `fix` means "get one
more look", never "pretend it is settled".