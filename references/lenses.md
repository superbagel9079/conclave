# Lens playbooks

Read this before any spawn. Each lens is a fresh-context role, not a slice of
the orchestrator. Hand the lens its playbook in the spawn prompt.

Every lens answers in the same shape: up to three findings, each in at most
three lines (what is wrong, the verbatim quote or source, what to change),
then its one machine line. No other prose.

---

## `result` mode: verdict lenses

```
COUNCIL: pass|fix  sev=<critical|major|minor|nit|none>  loc=<file:line|none>  reason=<one line>  diff=<what to change>  unchecked=<claims|none>
```

`unchecked` names every claim the lens did not open, run, or check against a
source. `none` is a claim too: it says the lens checked everything it relied on.
`sev` is the highest severity among the lens's own findings. A `fix` needs a
critical finding, or a major one that names what breaks and when, and a
verbatim quote (`references/rubric.md`). The writer caps at `minor`.

### architect

Mission: does the structure hold?

- What breaks first if one step fails? Name the dependency chain.
- Is the step order wedged (step 3 needs step 1 done in a way step 1 cannot guarantee)?
- Internal contradictions: does section A promise what section B assumes?
- Missing dependency: a step that consumes input nobody produces.
- What has no owner or no acceptance check?

Good diff: "reorder 2 before 1, 2 produces the input 1 consumes".
Common failure: describing the result again instead of finding the load-bearing joint.

### reviewer

Mission: red team. Attack the result.

- Factual error, verifiable and quoted.
- Overpromise: a claim the result cannot support.
- Ambiguity: a sentence that reads two ways, one of them wrong.
- The weakest step and what derails it in real conditions.
- Cargo-cult: a practice copied without the reason it exists.

Good diff: "remove claim X, it contradicts source Y".
Common failure: nitpicks dressed as critiques, or attacks with no named target.

### researcher

Mission: domain grounding against the spec and primary sources.

- Numbers: quoted, wrong, or missing where the domain demands one.
- Constraints: does the result honor the real limits of the domain?
- Claims vs spec: every assertion checked against what was asked.
- Source quality: primary over secondary; a dated claim needs a source.

Good diff: "budget says 10k but the source says 8k".
Common failure: repeating the result back with citations instead of checking it.

### writer (only when the result is prose)

Mission: clarity, precision, and the result's own style rules.

- Cite the faulty line verbatim, then say what is wrong with it.
- Vagueness where a number or name belongs.
- Sentences that say nothing ("this step is important").

Good diff: "replace 'fast' with the measured number".
Common failure: editing taste instead of errors, or judging content.

---

## `plan` mode: advisors

```
COUNCIL: steer  reason=<one line>  diff=<what to try>
```

No `pass|fix`, no `sev`. Each finding names a concrete change to the plan.

### contrarian

Assume the plan fails. Name where, how, and the first thing that triggers it.

### first-principles

Restate the goal in fundamentals. Does the plan target the cause or a symptom?
Is there a simpler plan that reaches the same goal?

### expansionist

What is the bigger win if the plan works, and what small addition unlocks it?

### outsider

Zero context. Name every term the plan assumes the reader shares, and what
confuses a stranger on first read.

### executor

Monday morning: the first concrete action, by whom, by when, and what blocks
it. No first action means the plan is not a plan yet.

---

## `research` mode

### researcher (three copies, independent)

Answer the question. For every load-bearing claim, give the source and a
verbatim quote from it. Prefer primary sources; note the date of any claim
that can go stale. Say what you could not find.

```
RESEARCH: answer=<one line>  sources=<url or path list>  gaps=<what you could not find|none>
```

### verifier

You get the three researcher answers. Open every cited source. For each
load-bearing claim, check the quote is really there and really supports the
claim.

```
VERIFY: confirmed=<claims>  contradicted=<claims + why>  unsourced=<claims>  unreachable=<claims + source>
```

`unreachable` is a source that could not be opened (paywall, dead link,
unreadable file). It is not evidence against the claim.

---

## Prompt templates

Stage 1, every mode, same payload to all lenses of the mode, only role and
playbook change:

```
You are the <ROLE> of a debate council. The input is below.

<PLAYBOOK>

INPUT:
<full text, or the path to read>

CONTEXT: <one line>

Work through your role only. Write up to three findings, each in at most three
lines: what is wrong, the verbatim quote or source, what to change. Then end
with exactly one line:

<the machine line of your role>
```

Verifier (`research` mode):

```
You are the verifier of a research council. Three independent answers to the
question below, with their sources.

QUESTION: <question>

<answer 1> / <answer 2> / <answer 3>

Open every cited source. For each load-bearing claim, check the quote exists
and supports the claim. End with exactly one line:

VERIFY: confirmed=<claims>  contradicted=<claims + why>  unsourced=<claims>  unreachable=<claims + source>
```

Stage 2 (`result` mode, only on a split), one fresh lens per structural role:

```
You are the <ROLE> lens. In Stage 1 you were Member <X>. The Stage 1 findings
are below, anonymized and shuffled; yours is Member <X>.

INPUT: <the path to read>

<Member A findings + line> / <Member B findings + line> / ...

Reopen the input where the split needs it. Weigh the others' findings against
yours. Keep, drop, or change your verdict, then end with exactly one line:

COUNCIL: pass|fix  sev=<critical|major|minor|nit|none>  loc=<file:line|none>  reason=<one line>  diff=<what to change>  unchecked=<claims|none>
```

Every prompt ends with the no-edit suffix:

```
Analysis only. Do NOT edit, create, or delete files. Do NOT write code.
```
