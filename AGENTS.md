# THE COUNCIL

The council is a debate bench. It critiques a plan, a finished result, or an
answer to a research question; it never does the work. The orchestrator stays
above it: it reads the findings and decides, it does not become a member.

## Golden rule

The council debates what it is given. If the work is still missing, it is
sent back to the builder first. A member who starts building has stepped out
of role.

## Three modes

1. **plan**: five advisor styles (contrarian, first-principles, expansionist,
   outsider, executor) critique an action plan. The chairman returns a ranked
   change list and a direction. The builder rewrites the plan.
2. **result**: verdict lenses (architect, reviewer, researcher, plus writer
   when the result is prose) judge a finished result. The verdict is
   machine-derived `pass|fix`.
3. **research**: three independent researchers answer a question with
   sources; one verifier checks every citation. The answer keeps confirmed
   claims only.

The orchestrator plays one extra lens, **user**: does Operator get value from
this as-is. It stays above the findings and never joins them.

## Output

Each member writes up to three short findings (what is wrong, the quote or
source, what to change), then one machine line. The machine line is
authoritative for counting. Formats live in `references/lenses.md`.

## Convergence

1. `result` mode: Stage 2 runs only when lenses split on a blocking finding.
   No extra round after it; the chairman applies `references/tiebreak.md`.
2. `plan` mode: no Stage 2; the chairman merges and ranks.
3. `research` mode: the verifier pass replaces Stage 2.
4. There is no confidence score. `council.md` lists what stayed unverified
   (`references/rubric.md`).
5. The orchestrator ships on council.md, never on a single lens.

## Hard laws

- No member modifies, creates, or deletes files. No code.
- Trust the completion notification, no polling.
- A `fix` quotes the faulty line verbatim; a research claim cites a source.
- No result ships without real verdicts. An invented debate is worth zero.

## Receipt

Every session closes with one machine line, per mode, defined in `SKILL.md`.

---

## PROJECT MEMORY

Read every session. Write changes in place, prefix-stable.

- Repo name: `conclave` (public). Skill name: `conclave` (SKILL.md frontmatter).
- All content is English.
- Source of truth: this repo. The skill is installed at
  `~/.agents/skills/conclave/`.
- The council is a debate bench with three modes (plan, result, research),
  short findings plus one machine line per member, a machine-derived pass|fix
  in result mode, an unverified list instead of a confidence score, and a
  receipt.
- The council debates the result, never rebuilds it.
- humanizer always on: no em-dashes, no en-dashes, no cadratins, ever.
