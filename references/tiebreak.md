# Tie-break: how the chairman decides

Two debate rounds max, then the chairman decides. These rules make the decision
a calculation, not a mood.

## Precedence of lenses

When verdicts split, higher rows beat lower rows:

1. A named factual error (researcher or reviewer) beats every `pass`.
2. A missing dependency or wrong order (architect) beats every `pass` except
   a named factual error that proves otherwise.
3. A critical or major finding (rubric) beats a `pass` with no finding.
4. Style-only fixes (writer) never beat a structural `pass` from the architect.

## Rules

- A `fix` with `sev=critical|major` and a named finding beats `pass` + no
  finding. A `fix` that only carries `minor` or `nit` never beats a `pass`; two
  or more lenses naming the same `diff` record a recommendation, not a block.
- Two lenses with the same `diff` beat one lens with a different `diff`.
- 50/50 with equally strong findings ⇒ conservative: `fix`, and the retained
  action is the smallest change that clears all named findings.
- Advisor roster: contrarian (what fails) and executor (first action) outrank
  expansionist (upside) when the ask was about risk; first-principles outranks
  all when the ask was "right problem?"; outsider outranks all when the ask was
  "clear to a newcomer?".
- A lens that produced no finding cannot veto; only `COUNCIL:` lines count.

## Tie-break rounds

1. Collect Stage 2 verdicts.
2. If two lenses disagree, pass each dissenter the other's `reason` and `diff`,
   once.
3. Still split after a second pass ⇒ chairman decides with these rules and
   records the disagreement in `council.md`.

## What council.md must contain

- Final verdict: `pass` or `fix`, with confidence from the rubric.
- The disagreements, in one line each ("reviewer said fix, writer said pass").
- The one action retained, quoted as a `diff`, with its finding.

Ship on `council.md`, never on a lone lens.