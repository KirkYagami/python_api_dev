# Brute-force solution for validation (tries all possible assignments)
def is_valid(s, k):
    for i in range(len(s) - k + 1):
        if all(s[i + j] == s[i] for j in range(k)):
            return False
    return True

def solve_bf(n, k, s, r):
    s = list(s)
    min_flips = float('inf')
    best_s = ""
    
    def backtrack(i, curr_s, flips):
        nonlocal min_flips, best_s
        if i == n:
            if is_valid(curr_s, k):
                if flips < min_flips:
                    min_flips = flips
                    best_s = ''.join(curr_s)
            return
        if s[i] != '?':
            backtrack(i + 1, curr_s + [s[i]], flips + (1 if s[i] != r[i] else 0))
        else:
            for c in ['0', '1']:
                backtrack(i + 1, curr_s + [c], flips + (1 if c != r[i] else 0))
    
    backtrack(0, [], 0)
    return min_flips, best_s

# Input reading
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    r = input().strip()
    flips, result = solve_bf(n, k, s, r)
    print(flips)
    print(result)