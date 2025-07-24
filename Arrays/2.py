def findTotalSum(n,arr,p):
    Sum=0
    for i in range(p-1,n-1):
        diff=abs(arr[i]-arr[i+1])
        Sum+=diff

    return Sum
n=int(input())
arr=list(map(int,input().split()))
p=int(input())
result=findTotalSum(n,arr,p)
print(result)