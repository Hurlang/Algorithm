exchange = int(input())
dp = [987654321] * (exchange + 1)
dp[0] = 0
# for item in arr:
#     print(*item)
for i in range(1, exchange + 1):
    mininum = 987654321
    if i >= 2:
        mininum = min(mininum, dp[i-2] + 1)
    if i >= 5:
        mininum = min(mininum, dp[i-5] + 1)

    dp[i] = mininum

for i in range(exchange + 1):
    if dp[i] == 987654321:
        dp[i] = -1

print(dp[-1])
