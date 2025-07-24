'''n=int(input()))
for i in range(n):
    print("*"*n)'''
    
'''n=int(input())
for i in range(1, n + 1):
    print("* "*i)  # Print increasing number of stars in each row'''

'''n=int(input())
for i in range(n, 0, -1):
    print("* "*i)''' 
    
'''
n=int(input())
for i in range(n):
    print("* "*(n-i))  # Print decreasing number of stars in each row
    
     
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
    #print a program to print a pattern of stars in pyramid shape
n=int(input())
for i in range(1, n + 1): 
    print((n-i)*" "+((2*i)-1)*("*")) 

n=int(input())
for i in range(1, n + 1):  
    print(" "*(n-i),end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n=int(input())
for i in range(1, n + 1):
    print(" "*(n-i),end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(i,end=" ")
    print()  # Print a pyramid pattern with numbers in each row
    
    
n=int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(num,end=" ") 
        num+=1
    print()'''
    
    
    #write a program to print hollow square pattern of stars
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()