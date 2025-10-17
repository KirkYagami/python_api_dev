# Qwen Attempt 1: Greedy Approach (Fails on test case 4)
def solve(n, k, s, r):
    # Convert string to list for easier manipulation
    s = list(s)
    flips = 0
    # Greedily flip bits to satisfy k consecutive identical bits
    for i in range(n):
        if s[i] == '?':
            s[i] = r[i]  # Prefer reference string bit
        if i >= k:
            # Check if last k bits are identical
            if all(s[i-j] == s[i] for j in range(k)):
                # Flip current bit to break sequence
                s[i] = '1' if s[i] == '0' else '0'
                flips += 1 if s[i] != r[i] else 0
    return flips, ''.join(s)

# Input reading
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    r = input().strip()
    flips, result = solve(n, k, s, r)
    print(flips)
    print(result)