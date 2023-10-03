N = int(input())
dp = [0] * (N+1)
for i in range(1, N+1):
    Min = 987654321

    if i >= 3:
        Min = min(Min, dp[i-3]+1)

    if i >= 5:
        Min = min(Min, dp[i-5]+1)

    dp[i] = Min

# print(dp)
if dp[N] == 987654321:
    print(-1)
else:
    print(dp[N])