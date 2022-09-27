N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, 1<<N):
    ssum = 0
    for j in range(N):
        if i & (1<<j):
            ssum += arr[j]
    if ssum == S:
        ans += 1

print(ans)