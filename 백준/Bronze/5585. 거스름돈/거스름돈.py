v = int(input())
ex = 1000 - v

dp = [0] * (ex + 1)
for i in range(1, ex + 1):
    Min = 987654321
    if i >= 1:
        Min = min(Min, dp[i-1]+1)
    if i >= 5:
        Min = min(Min, dp[i-5]+1)
    if i >= 10:
        Min = min(Min, dp[i-10]+1)
    if i >= 50:
        Min = min(Min, dp[i-50]+1)
    if i >= 100:
        Min = min(Min, dp[i-100]+1)
    if i >= 500:
        Min = min(Min, dp[i-500]+1)

    dp[i] = Min

print(dp[ex])