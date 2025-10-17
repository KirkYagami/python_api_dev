# stdin is like a QUEUE - read from it line by line

import sys

# Read first line
name = sys.stdin.readline().strip()

# Read second line  
age = sys.stdin.readline().strip()

# Read third line
city = sys.stdin.readline().strip()

print(f"{name} is {age} years old and lives in {city}.")



# $ python script.py
# Nik          # You type this, press Enter (readline #1 gets it)
# 24            # You type this, press Enter (readline #2 gets it)
# Goa      # You type this, press Enter (readline #3 gets it)
# Nik is 24 years old and lives in Goa.