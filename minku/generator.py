# Test case generator
import random

def generate_test_case(n, k, num_questions):
    s = ['0'] * n
    r = ['0'] * n
    questions = random.sample(range(n), num_questions)
    for i in questions:
        s[i] = '?'
    for i in range(n):
        r[i] = str(random.randint(0, 1))
    return n, k, ''.join(s), ''.join(r)

# Generate 5 test cases
for i in range(1, 6):
    if i == 1:
        n, k = 5, 2
        s, r = "??1??", "01100"
    elif i == 2:
        n, k = 3, 1
        s, r = "???", "000"
    elif i == 3:
        n, k = 10, 3
        s, r = "??????1111", "0000000000"
    elif i == 4:
        n, k = 8, 4
        s, r = "??0?????", "11111111"
    else:
        n, k = random.randint(5, 10), random.randint(1, 3)
        s, r = generate_test_case(n, k, random.randint(2, n-2))
    
    with open(f"test_cases/{i}.in", "w") as f:
        f.write("1\n")
        f.write(f"{n} {k}\n")
        f.write(f"{s}\n")
        f.write(f"{r}\n")