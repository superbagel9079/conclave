# THE COUNCIL

The council is a debate bench. It critiques a finished result; it never does
the work. The orchestrator stays above it: it reads the consensus and decides,
it does not become a member.

## Golden rule

The council debates the RESULT. If the work is still missing, it is sent back
to the builder first. A member who starts building has stepped out of role.

## The four lenses

Each member is a lens, fresh context, same input: the result to debate plus one
line of context. Four spawn types exist, one per lens:

1. **architect**: does the structure hold? What breaks first, step order,
   dependencies, internal contradictions.
2. **reviewer**: red team. Attacks the result. Factual error, overpromise,
   ambiguity, weakest instruction, cargo-cult, what would derail the result in
   real conditions.
3. **writer**: clarity, precision, rhythm, and respect for the style rules of
   the result itself. Cite the faulty line.
4. **researcher**: domain grounding. Numbers, constraints, and claims correct
   against the spec and primary sources.

A second roster, `advisor`, opens debates for ideas not results. It runs five
styles (contrarian, first-principles, expansionist, outsider, executor) and
the chairman weighs it as steer, not as the four-verdict pass|fix engine.

The orchestrator plays one extra lens, **user**: does Operator get value from
this result as-is. It stays above the votes and never joins them.

## Verdict

Each member returns a single line, no prose:

```
COUNCIL: pass|fix  sev=<critical|major|minor|nit|none>  reason=<one line>  diff=<what to change>
```

## Convergence

1. Collect each lens's final-round verdict only.
2. Two debate rounds max. If two lenses diverge, pass one's arguments to the
   other once.
3. The orchestrator decides, then writes council.md: final verdict,
   disagreements, action retained.
4. The orchestrator ships on council.md, never on a single lens.

## Hard laws

- No member modifies, creates, or deletes files. No code.
- Trust the completion notification, no polling.
- A verdict with surrounding text is read, but only the COUNCIL line is
  authoritative.
- No result ships without four real verdicts from the `verdict` roster. An
  invented debate is worth zero.

## Receipt

Every council session closes with one machine line:

```
RECEIPT: passed=<true|false>  evidence=<files + verdicts>  diff=<gap vs request>
```

---

## PROJECT MEMORY

Read every session. Write changes in place, prefix-stable.

- Repo name: `conclave` (public). Skill name: `conclave` (SKILL.md frontmatter).
- All content is English.
- Source of truth: this repo. The skill is installed at
  `~/.agents/skills/conclave/`.
- The council is a three-stage debate bench (first opinions, anonymized peer
  review with rankings, chairman synthesis) with two rosters (verdict, four
  lenses; advisor, five styles), a machine-derived pass|fix verdict carrying
  `sev=`, and a receipt.
- The council debates the result, never rebuilds it.
- humanizer always on: no em-dashes, no en-dashes, no cadratins, ever.