# Binary Signal Restoration Submission

This submission contains an original competitive programming problem designed for Codeforces Div1/Div2 difficulty. The problem, "Binary Signal Restoration," involves restoring a binary string with unknown bits ('?') to minimize differences from a reference string while ensuring no more than **k** consecutive identical bits.

## Notes
- The problem is search-proof, with no identical or closely similar problems found on major platforms.
- Qwen3-235B-A22B-2507 fails on at least one test case in three attempts (see `qwen/` folder).
- Test cases cover edge cases (k=1, large k, all '?', no '?') and tricky scenarios.
- The optimal solution uses DP with bitmask state compression, suitable for the given constraints (n ≤ 1000, k ≤ 10).
- A brute-force solution and test case generator are included for validation.

## How to Run
- Use `solution.py` for the optimal solution.
- Use `solution_bf.py` for brute-force validation (small cases only).
- Test cases are in `test_cases/`.
- Run `generator.py` to regenerate or create additional test cases.