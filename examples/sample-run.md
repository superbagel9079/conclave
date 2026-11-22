# Sample run

Golden example. Match this shape when you write `council.md`.

## Input

Prompt: "We plan to ship the new payment flow with a single cron backup of the
database at 03:00. Good to go?"

Context: production, one dev, no on-call.

Result under debate: the plan as stated. Roster: `verdict`.

## Stage 1: first opinions (abridged)

**architect**
```
COUNCIL: fix  sev=major  reason=backup runs at 03:00 but the deploy window is 02:00, no step verifies the backup finished before traffic resumes  diff=move backup to 02:05 and add a 'backup verified' acceptance check before release
```

**reviewer**
```
COUNCIL: fix  sev=major  reason=single cron backup means one point of failure and no verify step, first error at 03:05 is silent  diff=add a post-backup restore test and an alert on exit code != 0
```

**writer**
```
COUNCIL: pass  sev=none  reason=plan is clear and the steps read in order  diff=none
```

**researcher**
```
COUNCIL: fix  sev=major  reason=claim 'backup suffices' is unsupported, no retention or restore target named  diff=state retention window and a restore target
```

## Stage 2: review (anonymized, abridged)

Member A ranked Member C's structural point above the two `fix` details, but
restated:

```
COUNCIL: fix  sev=major  reason=no verify step after backup, silent failure at 03:05  diff=post-backup restore test plus alert on nonzero exit
```

The researcher held:

```
COUNCIL: fix  sev=major  reason=no retention or restore target named  diff=state retention window and restore target in the plan
```

## council.md

- Verdict: `fix`, confidence 0.85.
- Disagreements: writer passed on clarity; architect, reviewer, researcher
  fixed on the missing verify step and unnamed retention.
- Retained action: add a post-backup restore test, an alert on nonzero exit,
  and named retention plus restore target. Ship after that.

## Receipt

```
RECEIPT: passed=false  evidence=references/../sample-run.md + 4 verdicts
diff=plan shipped without verify step, retention, or restore target
```