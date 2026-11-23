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

Read `sev` from each lens's final-round `COUNCIL:` line, and validity from its
findings (the check below). Stage 1 lines count only when Stage 2 was
skipped, or for the writer, which is not re-run.

- Any valid `critical` or `major` from architect, reviewer, or researcher ⇒ `fix`.
- The writer caps at `minor`: it never blocks a structural pass.
- Only minor or nit findings ⇒ `pass`.

Validity check, run by the chairman right after Stage 1 and again on the
final round:

- **Quote.** Collapse every run of whitespace and newlines to one space, in
  both the quote and the input, then search. Not found voids the finding,
  whatever its severity. Files are hard-wrapped, so a literal line grep
  would void real quotes that cross a line break.
- **Named failure.** A `major` that does not say what breaks and when is
  read as `minor`.
- **Outside source.** A finding that rests on something outside the input
  ("the docs say 8k") must name the path or URL plus a quote from it. The
  chairman opens it and applies the quote rule there. If it cannot be
  opened, or names no source, the finding goes on the unverified list and
  does not block.

Retained actions: every distinct `critical` or `major` diff, none dropped.
Minor and nit diffs are listed as recommendations.

## Unverified list (every mode)

There is no confidence score. A number the chairman estimates for itself is
checked against nothing, and a threshold on it hides what was not checked.
Instead `council.md` lists what nobody verified, built from what the lenses
report, not from what the chairman believes:

- the union of every lens's `unchecked=` field
- a finding voided because its quote was not found
- a finding whose outside source could not be opened
- in `research` mode, every claim the verifier marked `unsourced` or `unreachable`
- a lens that omitted `unchecked=`: its whole verdict goes on the list

An empty list means no lens reported a gap. It is not proof of safety: lenses
on one model share blind spots, which is what strong mode is for. A non-empty
list is not a block; it tells Operator exactly where to look first.
