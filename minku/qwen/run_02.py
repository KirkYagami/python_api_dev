# Qwen Attempt 2: Simple DP (Fails on test case 3)
def solve(n, k, s, r):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    prev = [''] * (n + 1)
    s = list(s)
    
    for i in range(1, n + 1):
        # Try setting bit to 0 or 1
        for c in ['0', '1']:
            if s[i-1] != '?' and s[i-1] != c:
                continue
            # Check if valid
            valid = True
            if i >= k:
                if all(s[i-j-1] == c for j in range(k)):
                    valid = False
            if valid:
                cost = dp[i-1] + (1 if c != r[i-1] else 0)
                if cost < dp[i]:
                    dp[i] = cost
                    prev[i] = prev[i-1] + c
    
    return dp[n], prev[n]

# Input reading
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    r = input().strip()
    flips, result = solve(n, k, s, r)
    print(flips)
    print(result)