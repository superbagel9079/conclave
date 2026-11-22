# conclave

A debate bench that spawns lens agents in parallel to judge a result or an
idea, then converges on one verdict. Three stages: independent first opinions,
anonymized peer review, chairman synthesis.

Never ship on one agent's guess. Several lenses attack the result, rank each
other's work anonymously, and a chairman ships one machine-derived verdict
(`pass` / `fix`) with the exact finding behind it.

## What it does

- Stage 1: every lens gives a first opinion in parallel, no cross-talk.
- Stage 2: each lens reviews the others' opinions, anonymized as
  `Member A/B/C` in shuffled order, and ranks them by accuracy and insight.
- Stage 3: the chairman reads all of it, applies the user lens, and writes
  `council.md`: final verdict, the disagreements, the one action retained.

Two rosters:

- `verdict`: architect, reviewer, writer, researcher. For a finished result:
  ship or fix.
- `advisor`: contrarian, first-principles, expansionist, outsider, executor.
  For an open idea before you commit.

## Install

Copy the skill into your skills directory:

```bash
cp -r . ~/.agents/skills/conclave/
```

Then reload, or force-load it:

```text
/skill:conclave
```

## Use

Say "conclave" or "debate this", then hand it a file or paste a result:

```text
conclave: critique plan.md
```

The skill reads `references/` as it goes and never rebuilds: it debates the
result, it does not do the work.

## Files

```
SKILL.md                        # the spine: stages, verdict, hard laws
AGENTS.md                       # originating spec, the council laws
references/lenses.md            # full playbook per lens + prompt templates
references/rubric.md            # severity, confidence, mechanical verdict
references/tiebreak.md          # chairman decision rules
examples/sample-run.md          # golden run to imitate
```

## License

MIT.