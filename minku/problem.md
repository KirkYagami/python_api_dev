# Binary Signal Restoration

## Problem Statement

In a communication system, a binary signal is represented as a string of length **n** consisting of '0', '1', or '?' (unknown bit). Due to noise, some bits are marked as '?' and need to be restored to either '0' or '1'. You are given a reference signal (another binary string of length **n**) that the restored signal should resemble as closely as possible. However, the restored signal must satisfy a constraint: **no more than k consecutive bits can be identical** (either all 0s or all 1s).

Your task is to restore the signal by assigning '0' or '1' to each '?' in the original string, minimizing the number of positions where the restored signal differs from the reference signal (i.e., minimize the number of flips). Output the minimum number of flips and the restored signal.

## Input Format
- The first line contains an integer **t** (1 ≤ t ≤ 100), the number of test cases.
- For each test case:
  - The first line contains two integers **n** (1 ≤ n ≤ 1000) and **k** (1 ≤ k ≤ min(n, 10)), the length of the string and the maximum number of consecutive identical bits allowed.
  - The second line contains a string **s** of length **n**, consisting of '0', '1', or '?'.
  - The third line contains a string **r** of length **n**, consisting of '0' or '1' (the reference signal).

## Output Format
For each test case:
- Output two lines.
- The first line contains a single integer: the minimum number of positions where the restored signal differs from the reference signal.
- The second line contains the restored signal, a string of length **n** consisting of '0' or '1', with no more than **k** consecutive identical bits.

## Constraints
- 1 ≤ t ≤ 100
- 1 ≤ n ≤ 1000
- 1 ≤ k ≤ min(n, 10)
- **s** consists of '0', '1', or '?'
- **r** consists of '0' or '1'
- It is guaranteed that a valid restored signal exists.

## Examples

### Example 1
**Input**:
1
5 2
??1??
01100

**Output**:
1
00100

**Explanation**: 
The original signal is "??1??". We need to assign '0' or '1' to the '?' positions to minimize differences from the reference signal "01100", ensuring no more than 2 consecutive bits are identical. One optimal solution is "00100":
- Position 3 is fixed as '1'.
- Assigning "00100" requires 1 flip (position 2: '0' vs '1' in reference).
- The string "00100" has no more than 2 consecutive identical bits.

### Example 2
**Input**:
1
3 1
???
000

**Output**:
2
101


**Explanation**: 
With k=1, no two consecutive bits can be identical. The restored signal "101" requires 2 flips from "000" (positions 1 and 3) and satisfies the constraint (alternating bits).

### Example 3
**Input**:
1
6 3
1??0??
101011

**Output**:
0
101011

**Explanation**: 
Assigning "101011" to the '?' positions matches the reference signal exactly (0 flips) and satisfies the constraint (no more than 3 consecutive identical bits).

## Notes
- A valid solution always exists.
- Minimize the number of positions where the restored signal differs from the reference signal.

