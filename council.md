# council.md: conclave, self-review

Verdict: fix, confidence 0.88.

## Findings (severity per references/rubric.md)

- major: the `COUNCIL:` line carries no severity, yet `references/rubric.md`
  and `references/tiebreak.md` compute the verdict from severity tiers, so the
  headline "machine-derived pass|fix verdict" is not derivable from the
  produced output. Named independently by architect and researcher.
- major: `references/tiebreak.md` says "`fix` + named finding beats `pass` +
  no finding. Always.", which contradicts `rubric.md` ("nit ... never blocks",
  "Only minor/nit findings => pass"). A fix backed only by a style nit would
  wrongly block a clean pass. Named by reviewer, writer, architect, researcher.
- minor: "always a fifth lens" is a miscount in `SKILL.md:42` and
  `AGENTS.md:27`; the advisor roster has five lenses, so the user lens is the
  sixth there. Named by writer.
- minor: frontmatter field `user-invocable: true` is not in the Agent Skills
  spec (agentskills.io/specification lists name, description, license,
  compatibility, metadata, allowed-tools). Named by researcher; ranked last by
  the other three as un-actionable from the repo alone.

## Disagreements

- No lens voted pass. All four voted fix; they split on which fix leads, not on
  whether to fix.
- reviewer, writer, architect, and researcher all ratified the tiebreak-vs-rubric
  contradiction after Stage 2 (same diff named by four members).
- architect and researcher also held the severity-field gap as the
  deeper fracture; reviewer and writer ranked it second, focusing on the
  tiebreak rule first.
- researcher's `user-invocable` finding was downgraded to minor by the other
  lenses as unverifiable from the repo; researcher conceded "drop it" is the
  clean path.

## Retained action

1. Add a severity field to the verdict contract: change the COUNCIL line in
   `SKILL.md`, `references/lenses.md`, `AGENTS.md`, and `examples/sample-run.md`
   to `COUNCIL: pass|fix sev=<critical|major|minor|nit> reason=<one line>
   diff=<what to change>`.
2. Tighten the tie-break rule in `references/tiebreak.md`: replace "`fix` +
   named finding beats `pass` + no finding. Always." with "a critical or major
   finding beats `pass` + no finding; minor stays pass unless two or more
   lenses name the same diff."
3. (minor) Fix the lens count: "always a fifth, extra lens" in `SKILL.md:42`
   and "the fifth lens" in `AGENTS.md:27` -> "an extra lens".

Ship on this file, never on a lone lens.

RECEIPT: passed=false  evidence=council.md + 8 verdicts (4 stage-1, 4 stage-2)  diff=severity missing from verdict contract and tiebreak rule overrides the rubric on minor/nit findings