#RECURSION
'''if function calling itself, it is called recursion.
Recursion is a process in which a function calls itself as a subroutine.'''

'''def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a number to find its factorial: "))
print(factorial(n))'''

'''write a program to find the sum of natural numbers ofusing recursion'''

'''def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
n = int(input("Enter a number to find the sum of natural numbers: "))
print("The sum of natural numbers up to", n, "is:", sum(n))'''

'''write a program to find the nth fibonacci number using recursion'''

'''def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input ())
print("The", n, "th Fibonacci number is:", fibonacci(n))'''


'''write a program to find power if two numbers using recursion'''

'''def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
print(power(base, exp))'''


'''write a program to count the number of digits in a number using recursion'''

'''def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

n = int(input())
print("The number of digits in", n, "is:", count_digits(n))'''

