# Qwen Attempt 3: Incorrect Bit Manipulation (Fails on test case 2)
def solve(n, k, s, r):
    # Try to use bit manipulation for states
    s = list(s)
    flips = 0
    for i in range(n):
        if s[i] == '?':
            # Choose bit based on reference
            s[i] = r[i]
        # Check last k bits using bit manipulation
        if i >= k:
            mask = 0
            for j in range(k):
                mask = (mask << 1) | (1 if s[i-j] == '1' else 0)
            if mask == (1 << k) - 1 or mask == 0:  # All 1s or 0s
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