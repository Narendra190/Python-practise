'''def countOddEvenDifference(n, arr):
    odd_count = 0
    even_count = 0
    for num in arr:  
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return abs(odd_count - even_count)  

n = int(input())
arr = list(map(int, input().split()))

result = countOddEvenDifference(n, arr)
print(result) '''


'''def findTotalSum(n,arr,p):
    Sum=0
    for i in range(p-1,n-1):
        diff=abs(arr[i]-arr[i+1])
        Sum+=diff

    return Sum
n=int(input())
arr=list(map(int,input().split()))
p=int(input())
result=findTotalSum(n,arr,p)
print(result)'''

'''def choclate(n,arr):
    for i in arr:
        if(i==0):
            arr.remove(0)
            arr.append(0)
    return arr
n=int(input())
arr=list(map(int, input().split()))
result=choclate(n,arr)
print(result)'''


'''d=input()
n=int(input())
l=["sun","mon","tue" ,"wed", "thu", "fri", "sat"]
i =l.index(d)
days = (7-i)%7
count = 0
for i in range(days,n+1,7):
    count += 1
print(count)'''


n=int(input())
l=list(map(str, input().split()))
l.sort()
print(1)
print(" ".join(l))