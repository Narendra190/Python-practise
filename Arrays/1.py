def countOddEvenDifference(n, arr):
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
print(result)
