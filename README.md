# conclave

A debate bench that spawns lens agents in parallel, then converges on one
output. Never ship on one agent's guess.

## Modes

| mode | use it for | you get | agents |
|------|-----------|---------|--------|
| `plan` | an action plan before you commit | a ranked change list | 5 |
| `result` | a finished result: ship or not | `pass` / `fix` with every blocking diff | 3 or 4, up to 7 on a split |
| `research` | a question that needs a checked answer | answer, sources, what stayed unverified | 4 |

Instead of a confidence score, every run lists what nobody verified. That
list, not a number, tells you where to look.

## Models

Run lenses on a high-reasoning model at high effort. For results that matter,
strong mode runs the same mode on two different models and keeps the union of
findings: two models do not share every blind spot.

## Install

Link the skills directory to your clone, so every `git pull` updates the
installed skill. Run from the clone:

```bash
ln -s "$PWD" ~/.agents/skills/conclave
```

On Windows (a junction needs no admin rights):

```powershell
New-Item -ItemType Junction -Path "$HOME\.agents\skills\conclave" -Target (Get-Location)
```

The chairman runs `scripts/quotecheck.py`, so Python 3 must be on the path.
Then reload, or force-load it:

```text
/skill:conclave
```

## Use

Say "conclave" or "debate this", then hand it a file or paste a result:

```text
conclave plan: critique plan.md
conclave result: is report.md ready to ship?
conclave research: what is the rate limit of API X?
```

The skill reads `references/` as it goes and never rebuilds: it debates, it
does not do the work.

## Files

```
SKILL.md                        # the spine: modes, flow, hard laws
AGENTS.md                       # originating spec, the council laws
references/lenses.md            # full playbook per lens + prompt templates
references/rubric.md            # severity, mechanical verdict, unverified list
references/tiebreak.md          # chairman decision rules
examples/sample-run.md          # golden run to imitate
scripts/quotecheck.py           # quote check, whitespace collapsed
scripts/test_quotecheck.py      # its self-test: python scripts/test_quotecheck.py
```

## License

MIT.