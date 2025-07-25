def choclate(n,arr):
    for i in arr:
        if(i==0):
            arr.remove(0)
            arr.append(0)
    return arr
n=int(input())
arr=list(map(int, input().split()))
reuslt=choclate(n,arr)
print(result)