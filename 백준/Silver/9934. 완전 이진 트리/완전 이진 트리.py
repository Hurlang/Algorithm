def f(arr, k):
    mid = len(arr)//2
    if mid != 0:
        f(arr[:mid], k+1)
        f(arr[mid+1:], k+1)
    if memo[k]:
        memo[k].append(arr[mid])
    else:
        memo[k] = [arr[mid]]


K = int(input())
arr = list(map(int, input().split()))
memo = [ 0 for i in range(K)]
f(arr, 0)
for i in range(K):
    print(*memo[i])
