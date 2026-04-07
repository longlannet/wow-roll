---
name: wow-roll
description: Simulate World of Warcraft /roll command (1-100). Use when the user wants to roll a random number, test their luck, or use a WoW-style dice roll.
emoji: 🎲
requires:
  bins: [python3]
---

# WoW Roll

Simulate World of Warcraft `/roll` output with a random number from 1 to 100.

## Tools

### roll
Roll a random number from 1 to 100 and print a short comment.

**Parameters:**
- `user`: (optional) Name of the roller. Default: `User`.

**Command:**
```bash
python3 {baseDir}/scripts/roll.py "{{user}}"
```

## When to use

Use this skill when the user:
- says `/roll`
- asks to roll a number or dice
- wants a WoW-style random roll
- wants to test their luck with a quick 1-100 result

## Output

The script prints:
- one WoW-style roll line
- one short reaction/comment based on the score

Example shape:
```text
Lanny 掷出 57 (1-100)

👌 及格以上，希望能Roll过别人。
```

## Notes

- Range is fixed at `1-100`.
- This is a lightweight fun skill; do not overcomplicate the workflow.
- If the user does not provide a name, it is fine to pass `User` or the current display name.
