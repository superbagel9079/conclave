# Tie-break: how the chairman decides

The chairman decides once, after the last round its mode allows. These rules
make the decision a calculation, not a mood.

## `result` mode: precedence of lenses

When final-round verdicts still split, higher rows beat lower rows:

1. A named factual error (researcher or reviewer) beats every `pass`.
2. A missing dependency or wrong order (architect) beats every `pass` except
   a named factual error that proves otherwise.
3. A valid critical or major finding beats a `pass` with no finding.
4. Style-only findings (writer) never beat a structural `pass`.

Two lenses with the same `diff` beat one lens with a different `diff`. On a
50/50 split with equally strong findings, the verdict is `fix` and the
retained action is the smallest change that clears every named finding. Any
split broken by precedence goes on the unverified list.

## `plan` mode: ranking the change list

1. A finding two or more advisors raised independently ranks first.
2. Then by the ask: contrarian and executor lead when the ask is about risk
   or getting started; first-principles leads when the ask is "right
   problem?"; outsider leads when the ask is "clear to a newcomer?";
   expansionist leads only when the ask is about upside.
3. A finding that contradicts another is kept, both sides, as a disagreement.

## `research` mode: conflicting answers

1. A claim the verifier `confirmed` beats any claim it did not.
2. Two researchers agreeing with confirmed sources beat one.
3. A `contradicted` claim is dropped from the answer and named in
   disagreements.
4. Still unsettled: the answer states both positions and the claim goes on
   the unverified list. Never pick one silently.

## What council.md must contain

| mode | contents |
|------|----------|
| `result` | verdict; every retained critical/major diff in precedence order; recommendations; disagreements, one line each; unverified list |
| `plan` | direction, one line; ranked change list; disagreements, one line each |
| `research` | answer; sources; disagreements; unverified list |

Ship on `council.md`, never on a lone lens.
