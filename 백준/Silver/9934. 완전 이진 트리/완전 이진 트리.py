def f(arr, k):
    mid = len(arr)//2
    if mid == 0:
        if memo[k]:
            memo[k].append(arr[mid])
        else:
            memo[k] = [arr[mid]]
    else:
        if memo[k]:
            memo[k].append(arr[mid])
        else:
            memo[k] = [arr[mid]]
        f(arr[:mid], k+1)
        f(arr[mid+1:], k+1)



K = int(input())
arr = list(map(int, input().split()))
memo = [ 0 for i in range(K)]
f(arr, 0)
for i in range(K):
    print(*memo[i])
