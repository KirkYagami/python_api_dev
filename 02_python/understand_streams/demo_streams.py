import sys

# Writing to stdout
sys.stdout.write("This goes to standard output\n")

# Writing to stderr
sys.stderr.write("This is an error message\n")

# Reading from stdin
print("Enter your name: ")
name = sys.stdin.readline().strip()
print(f"Hello, {name}!")