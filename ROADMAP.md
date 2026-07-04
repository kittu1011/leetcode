# FAANG-Level LeetCode Prep Roadmap

## Per-Problem Methodology

Every problem, every time — this is what turns "I've seen 400 problems" into "I recognize patterns":

1. **Restate + clarify (30s)** — constraints, edge cases, input size (this tells you expected complexity: n≤20 → exponential ok, n≤10^5 → O(n log n), n≤10^7 → O(n))
2. **Brute force out loud** — always state it even if you skip coding it. It's your fallback and it seeds the optimization.
3. **Name the pattern before coding** — e.g. "this is sliding window because we want a contiguous subarray with a monotonic constraint." If you can't name it in one sentence, you don't understand it yet — go back to brute force.
4. **Code without running** — write the full solution, then trace one example by hand before executing. Highest-leverage interview habit; interviewers weight it more than the raw solve.
5. **Complexity + test edge cases** — empty input, single element, all duplicates, negative numbers.
6. **Post-mortem into `notes_template.md`** — not "here's the solution," but: what was the trigger phrase that identified the pattern, what mistake did I make, what's the generalized template. This is the compounding asset — a repo of trigger→pattern mappings is worth more than raw problem count.

## How Many Problems, and Which

Forget a magic number — it's pattern coverage, not count.

- **NeetCode 250** — fills gaps: advanced graphs (Dijkstra, Union-Find, topological sort variants), advanced DP (interval DP, digit DP, bitmask DP), harder backtracking.
- **Company-tagged sets (LeetCode Premium)** — filter by actual targets (Google, Amazon, Apple, Waymo). Do the **last 6 months** tagged list per company, ~30-40 problems each. Matters more than generic grinding once pattern-solid.
- **Target: 300-400 total lifetime, but re-solve, don't just consume new ones.** Take 30-40 problems done over a month ago and re-solve cold, timed. If the pattern isn't recognized in <2 min and clean code isn't done in 20-25 min, that pattern isn't internalized — more new problems won't fix it, repetition will.
- **Readiness signal:** on a fresh medium, pattern named within 60 seconds and clean code finished in under 25 minutes, 8/10 times.
- **Timeline:** ~8-10 weeks of daily practice (mostly new problems early, shifting toward re-solves) before mocks take over, given a Dec 2026 grad timeline.

## Daily Problem Count

**4-6 problems/day**, split as:

- **2-3 new problems** — untimed at first, transition to 25-min timed once past the "still learning basics" stage
- **1-2 re-solves** — old problems from the repo, cold and timed, to check retention
- **1 harder/company-tagged problem** — 2-3x/week, not daily (longer, more mentally taxing)

**Why not more:** Beyond ~6/day quality drops hard — pattern-matching from memory replaces actual reasoning, defeating the purpose. 5 problems with full methodology beats 15 done sloppily.

**Weekly shape:**
- Weekdays: 4-6/day as above
- One day/week: pure mock interview (1-2 problems, live, timed, out loud) instead of solo grinding
- One day/week: lighter — re-solves + updating notes only, no new problems (prevents burnout, keeps repo current)

That's ~25-35 problems/week → 300-400 lifetime over 8-10 weeks, without just chasing volume.

**Flag:** if a specific pattern (e.g. interval DP, Union-Find) keeps failing on re-solves, stop the mixed rotation and drill *only* that pattern for 2-3 days. Patchy patterns fail interviews, not raw count.

## Interview Environment Simulation

- **No IDE.** Practice in a blank Google Doc or plain text editor — no autocomplete, no syntax highlighting, no run button until done. Use Pramp, interviewing.io, or a friend for live mocks — at least weekly starting ~6 weeks out.
- **Talk the entire time**, including while stuck. Silence reads as failure even when the code is fine. Practice narrating brute force → optimization → tradeoffs out loud, alone, before real mocks.
- **Timebox strictly**: 5 min clarify/approach, 20-25 min code, 5-10 min test/complexity discussion. Use a timer in every practice session, not just mocks.
- **2-3 ready follow-ups memorized per pattern** ("what if the array doesn't fit in memory," "what if it's a stream") — interviewers commonly extend the base problem, and the response to that extension carries real weight.