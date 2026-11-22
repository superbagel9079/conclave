# Tie-break: how the chairman decides

Two reasoning rounds max (Stage 1 and Stage 2), then one dissent pass, then
the chairman decides. These rules make the decision a calculation, not a mood.

## Precedence of lenses

When verdicts split, higher rows beat lower rows:

1. A named factual error (researcher or reviewer) beats every `pass`.
2. A missing dependency or wrong order (architect) beats every `pass` except
   a named factual error that proves otherwise.
3. A critical or major finding from reviewer, researcher, or architect beats a
   `pass` with no finding.
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
- On an advisor run the lines are `steer`, not `pass|fix`: a split of steers
  skips the dissent pass and the chairman decides directly from the steers.

## Tie-break rounds

1. Collect each lens's newest `COUNCIL:` line after Stage 2.
2. The plurality verdict is the one held by the most lenses; on a tie, the
   Precedence of lenses above names it. The dissenter set is every lens not
   holding the plurality verdict. The chairman spawns one fresh lens per
   dissenter (same role as its Stage 2 member, never a steer of the old
   session) and hands it every distinct opposing `reason` and `diff`, once; on
   a multi-way split each dissenter addresses the top-count opposing reason in
   its single line, and on a tied top count the higher-Precedence winning
   lens's reason and `diff`. Each dissenter ends that pass with one `COUNCIL:`
   line, which becomes its final-round vote and replaces its Stage 2 line for
   counting.
3. Still split after that pass ⇒ chairman decides with these rules and records
   the disagreement in `council.md`.

## What council.md must contain

A verdict-roster run records:

- Final verdict: `pass` or `fix`, with confidence from the rubric.
- The disagreements, in one line each ("reviewer said fix, writer said pass").
- The action retained: every distinct `critical` or `major` diff, in
  precedence order. Divergent major diffs are all retained, none dropped; a
  `minor` or `nit` diff is retained only as a recommendation.

An advisor-only run records instead:

- The direction, one line, the chairman's chosen `steer`.
- The disagreements, in one line each.

Ship on `council.md`, never on a lone lens.