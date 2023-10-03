N, K = map(int, input().split())
W = [0] * (N+1)
V = [0] * (N+1)
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    a, b = map(int, input().split())
    W[i+1] = a
    V[i+1] = b

for i in range(1, N+1):
    for j in range(K+1):
        if W[i] <= j:
            dp[i][j] = max(dp[i-1][j-W[i]] + V[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
# for item in dp:
#     print(*item)

print(dp[-1][-1])