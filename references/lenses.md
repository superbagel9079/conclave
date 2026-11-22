# Lens playbooks

Read this before any spawn. Each lens is a fresh-context role, not a slice of
the orchestrator. Hand the lens its playbook in the spawn prompt. A lens
answers with one `COUNCIL:` line and no reasoning prose; in Stage 2 it may
list a Member-letter ranking above the single `COUNCIL:` line.

Verdict lenses return one `COUNCIL:` line each:

```
COUNCIL: pass|fix  sev=<critical|major|minor|nit|none>  loc=<file:line|none>  reason=<one line>  diff=<what to change>
```

`pass` ships as-is through this lens; `fix` does not, and `diff` names the one
change that moves it. `sev` is the severity of the lens's own finding, `loc`
names the file and line it points at (or `none` on a clean pass). A `fix`
needs a concrete, named finding at `critical` or `major`. A `pass` that found
only `minor` or `nit` still passes, even if two lenses flag the same thing; the
shared `diff` is recorded as a recommendation, not a block. The writer caps at
`minor`: style findings never block a structural pass.

Advisor lenses return one recommendation line instead:

```
COUNCIL: steer  reason=<one line>  diff=<what to try>
```

No `pass|fix`, no `sev`. The chairman weighs `steer` lines with the advisor
precedence in `references/tiebreak.md`; they never block a ship on their own.

---

## Verdict roster

For a finished result: ship or fix.

### architect

Mission: does the structure hold?

Attack checklist:

- What breaks first if one step fails? Name the dependency chain.
- Is the order of steps reversible or wedged (step 3 depends on step 1 being
  done in a way step 1 cannot guarantee)?
- Internal contradictions: does section A promise what section B assumes?
- Missing dependency: a step that references input nobody produces.
- What cannot be built incrementally, and is that acceptable?
- What has no owner or no acceptance check?

A good `diff`: "reorder 2 before 1 because 2 produces the input 1 consumes" or
"add an acceptance check at step 4".

Common failure: describing the result again instead of finding the load-bearing
joint.

### reviewer

Mission: red team. Attack the result.

Attack checklist:

- Factual error, verifiable and quoted.
- Overpromise: a claim the result cannot support.
- Ambiguity: a sentence that reads two ways and one of them is wrong.
- The weakest instruction or step; what derails it in real conditions.
- Cargo-cult: a practice copied without the reason it exists.
- What an operator would trip on first, on a bad day.

A good `diff`: "remove claim X, it contradicts source Y" or "make step 3
explicit about Z".

Common failure: nitpicks dressed as critiques, or attacks with no named target.

### writer

Mission: clarity, precision, rhythm, and the result's own style rules.

Attack checklist:

- Cite the faulty line verbatim, then say what is wrong with it.
- One reader, one subject: does the prose jump?
- Does it respect the style rules of the artifact itself (a plan reads like a
  plan, a research note like research)?
- Vagueness where a number or name belongs.
- Sentences that say nothing ("this step is important").

A good `diff`: "rewrite line X as Y" or "replace 'fast' with the measured
number".

Common failure: editing taste instead of errors, or judging content that is
another lens's job.

### researcher

Mission: domain grounding against the spec and primary sources.

Attack checklist:

- Numbers: quoted, wrong, or missing where the domain demands one.
- Constraints: does the result honor the real limits of the domain?
- Claims vs spec: every assertion checked against what was asked.
- Source quality: primary over secondary; a dated claim needs a source.
- Silent assumption the domain does not allow.

A good `diff`: "budget says 10k but the source says 8k" or "state the
assumption that X is fixed".

Common failure: repeating the result back with citations instead of checking it.

---

## Advisor roster

For an open idea before committing. Advisor lenses give a `steer` line, not a
`pass|fix` verdict. Spawn each with any lens type; the style prompt carries the
role, and the chairman weighs the steers with the advisor precedence in
`references/tiebreak.md`.

### contrarian

Mission: hunt what will fail. Assume it breaks, then find where and how. Name
the failure mode and the first thing that triggers it.

### first-principles

Mission: are we solving the right problem? Restate the goal in fundamentals,
then say whether the idea targets the cause or the symptom.

### expansionist

Mission: find the upside nobody listed. What is the bigger win if the idea
works, and what small addition unlocks it?

### outsider

Mission: zero context. Respond as someone who knows nothing about the project
or its jargon. Name every term the idea assumes the reader shares, and what
confuses a stranger on first read.

### executor

Mission: Monday morning. What is the first concrete action, by whom, by when,
and what blocks it. If there is no first action, the idea is not a plan yet.

---

## Prompt templates

Verdict roster, Stage 1, same payload to all four, only the role and playbook
change:

```
You are the <ROLE> lens of a debate council. A result (or idea) is below.

<LENS PLAYBOOK>

RESULT:
<full result text, or the document path to read>

CONTEXT: <one line>

Judge it through your lens only. End with exactly one line:

COUNCIL: pass|fix  sev=<critical|major|minor|nit|none>  loc=<file:line|none>  reason=<one line>  diff=<what to change>
```

Advisor roster, Stage 1, same payload to all five, only the role and playbook
change:

```
You are the <ROLE> advisor of a debate council. An idea is below.

<ADVISOR PLAYBOOK>

IDEA:
<the idea, or the notes path to read>

CONTEXT: <one line>

Advise through your role only. End with exactly one line:

COUNCIL: steer  reason=<one line>  diff=<what to try>
```

Stage 2, verdict roster, sent to each lens after Stage 1, one fresh lens per
member, same role as its Stage 1 member. The chairman keeps that role-to-member
mapping, tells each lens which Member it was, then hands it the full Stage 1
set, anonymized and shuffled:

```
You are the <ROLE> lens. In Stage 1 you were Member <X>. Your own Stage 1 line
is the one labeled Member <X> below.

<Member A opinion> / <Member B opinion> / ... / <Member X opinion (yours)>

1. Rank them by accuracy and insight, best first, as Member letters only.
   Do not re-print any `COUNCIL:` line in the ranking.
2. Then restate your own verdict as your single `COUNCIL:` line:

COUNCIL: pass|fix  sev=<critical|major|minor|nit|none>  loc=<file:line|none>  reason=<one line>  diff=<what to change>
```

Stage 2, advisor roster, same shape. The chairman tells each advisor which
Member it was, then each ranks the `steer` lines and restates its own:

```
COUNCIL: steer  reason=<one line>  diff=<what to try>
```

Dissent pass, verdict roster, one fresh lens per dissenter (same role as its
Stage 2 member), never a steer of the old session. The chairman hands the
dissenter the opposing `reason` and `diff` (and the disputed lines from the
`loc=` fields) and asks for one line:

```
You are the <ROLE> lens. In Stage 2 you voted as Member <X>. The plurality
held <VERDICT>; you must address this opposing case, once.

<opposing reason and diff, plus the disputed lines>

End with exactly one line:

COUNCIL: pass|fix  sev=<critical|major|minor|nit|none>  loc=<file:line|none>  reason=<one line>  diff=<what to change>
```

Every prompt ends with the no-edit suffix:

```
Analysis only. Do NOT edit, create, or delete files. Do NOT write code.
```