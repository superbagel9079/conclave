# Rubric: severity, confidence, mechanical verdict

The chairman does not decide the verdict by feel. The verdict is computed from
the findings, so it can never disagree with the evidence.

## Severity

| level | meaning | consequence |
|-------|---------|-------------|
| critical | false claim, wrong number that breaks the result, unsafe step, missing dependency that halts it | `fix`, blocks ship |
| major | a hole the result paperes over, a weak instruction that will derail it in real conditions | `fix` |
| minor | phrasing, order, a nit that does not change the outcome | `pass` unless three lenses flag it |
| nit | style only | never blocks |

## Mechanical verdict

- Any **critical** finding ⇒ `fix`, no discussion.
- Any **major** finding from the reviewer, researcher, or architect ⇒ `fix`.
- Only minor/nit findings ⇒ `pass`.
- Two or more lenses naming the same `diff` independently ⇒ that is the action
  retained, even if each called it minor.

A `fix` without a named finding does not count. The verdict cannot contradict
the evidence: if the findings are critical, the verdict is `fix`.

## Confidence

Confidence is the chairman's estimate that the retained action is correct,
from 0 to 1. Raise it when:

- multiple lenses name the same finding independently (+)
- the finding is quoted from a source or a specific line (+)
- a lens changes `pass` to `fix` after Stage 2 review (+)

Lower it when:

- the lenses split and the chairman had to break the tie (-)
- the deciding finding comes from a single lens with no source (-)

Report confidence with the verdict in `council.md`. Low confidence with a
`fix` verdict means the action is "get one more look", never "pretend it is
settled".