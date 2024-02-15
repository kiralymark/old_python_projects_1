#   FizzBuzz Task
# The task is to take an input 'n' and output the odd numbers from 1 to 'n'.
# For each multiple of 3, print "Fizz" instead 
# of the number. 
# For each multiple of 5, print "Buzz" instead 
# of the number. 
# For numbers which are multiples of both 3 and 5, 
# output "FizzBuzz".
# 
# Example Input:
# 16 
# 
# Expected Output:
# 1
# Fizz
# Buzz
# 7
# Fizz
# 11
# 13
# FizzBuzz

n = int(input())

for x in range(1, n):
    if x % 2 == 0:
        continue
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
        