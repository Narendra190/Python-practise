d=input()
n=int(input())
l=["sun","mon","tue" ,"wed", "thu", "fri", "sat"]
i =l.index(d)
days = (7-i)%7
count = 0
for i in range(days,n+1,7):
    count += 1
print(count)
