'''def greet():
    print("hello")

greet()
greet()'''

'''def greet(name):
    msg="Hello "+name
    return msg

greetings=greet("Raju")
print(greetings)'''


'''def greet(name):
    print("Hello",name)
    
name=input()
greet(name)'''



'''def greet():
    return ("Hello Raju")
       
greet()'''



'''def greet():
    return "Hello Raju"

print(greet())'''

'''def greet(name):
    msg= "Hello "+name
    return msg

print(greet(name))'''


'''def sum_of_two_numbers(a,b):
    sum=a+b
    return(sum)

a=int(input())
b=int(input())

sum=(sum_of_two_numbers(a,b))
print(sum)'''

'''def comparision(a,b,):
    if a>b:
        return" A is greater"
    elif b>a:
        return"B  is greater"
    else:
        return"Both are equal"
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(comparision(a,b))'''

'''print the largest number in the given list using function'''

'''def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

num_list = [3, 5, 2, 8, 1]
print("The largest number is:", find_largest_number(num_list))'''

'''find the odd numbers using function'''
'''def find_odd_numbers(m,n):
    for num in range(m, n + 1):
        if num % 2==1:
            print(num)

m=int(input("Enter the starting number: "))
n=int(input("Enter the ending number: "))
find_odd_numbers(m, n)'''

'''def factors(n):
    for i in range(1, n+1):
        if (n % i == 0):
            print(i, end=' ')
            
n = int(input())
factors(n)'''

''''print the string tonyph to python using function'''

'''def convert_string(input_string):
    lower_string = input_string.lower()

    converted_string = lower_string.replace('tonyph', 'python')
    return converted_string
input_string = "TONYPH"
result = convert_string(input_string)
print(result)'''


'''def replaced_str(s,indexes):
    for i in indexes:
        print(s[j],end='')
        
s=input()
indexes = int(map(int, input().split()))'''


'''count the number off even nnumbers in a list using function'''

'''def even_count(n):
    count=0
    for i in n:
        if (i % 2 == 0):
            count += 1
    return count
n=list(map(int, input().split()))
even_count = even_count(n)
print(even_count)'''


'''def reverse(n):
    return n[::-1]
n=input()
print(reverse(n))'''