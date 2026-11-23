# Sample run

Golden example of `result` mode. Match this shape when you write `council.md`.

## Input

Prompt: "We plan to ship the new payment flow with a single cron backup of the
database at 03:00, the deploy window opens at 02:00. Good to go?"

Context: production, one dev, no on-call.

Result under debate: `plan.md`. Mode: `result`. Not prose, so no writer.

## Stage 1 (abridged)

**architect**
```
- Backup runs an hour after deploy; nothing checks it finished before traffic resumes.
  Quote: plan.md:3 "cron backup at 03:00, deploy window 02:00"
  Change: back up at 01:55, gate the deploy on a 'backup verified' check.
COUNCIL: fix  sev=major  loc=plan.md:3  reason=deploy at 02:00 runs before the 03:00 backup, a bad migration has no restore point  diff=back up before deploy and gate release on 'backup verified'  unchecked=none
```

**reviewer**
```
- A failed cron exits silently; nobody is on call to notice.
  Quote: plan.md:3 "single cron backup"
  Change: alert on nonzero exit, run a restore test after the backup.
COUNCIL: fix  sev=major  loc=plan.md:3  reason=a failed backup at 03:00 goes unnoticed with no on-call  diff=alert on nonzero exit and add a post-backup restore test  unchecked=whether the backup tool exits nonzero on partial failure
```

**researcher**
```
- No retention or restore target, so "backup suffices" cannot be checked.
  Quote: plan.md:4 "backup suffices"
  Change: state retention window and restore time target.
COUNCIL: fix  sev=major  loc=plan.md:4  reason=no retention or restore target named  diff=state retention window and restore target  unchecked=none
```

## Quote check and early stop

All three quotes grep true in `plan.md`. Every structural lens blocks, on
different findings: no split, Stage 2 skipped. 3 agents spent.

## council.md

- Verdict: `fix`.
- Retained actions, none dropped:
  1. Back up before the deploy and gate release on 'backup verified'.
  2. Alert on nonzero exit; run a restore test after the backup.
  3. State a retention window and a restore target.
- Disagreements: none.
- Unverified (union of `unchecked=`): whether the backup tool exits nonzero
  on partial failure (reviewer).

## Receipt

```
RECEIPT: passed=false  model=<id>  evidence=plan.md + 3 verdicts  unverified=backup tool exit code on partial failure  diff=deploy precedes backup, no alert, no retention or restore target
```
