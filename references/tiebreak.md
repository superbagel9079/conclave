# Tie-break: how the chairman decides

The chairman decides once, after the last round its mode allows. These rules
make the decision a calculation, not a mood.

## `result` mode: ordering the retained diffs

The verdict comes from `references/rubric.md` alone: any valid critical or
major is `fix`. A `pass` never outvotes it; a refutation removes a finding
only through the validity check (quote not found, source contradicts it).
Precedence only orders the retained diffs in `council.md`:

1. A diff two or more lenses named independently.
2. A named factual error (researcher or reviewer).
3. A missing dependency or wrong order (architect).
4. Any other valid critical or major.
5. Recommendations (minor, nit, writer) last.

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
| `plan` | direction, one line; ranked change list; disagreements, one line each; unverified list |
| `research` | answer; sources; disagreements; unverified list |

Ship on `council.md`, never on a lone lens.
