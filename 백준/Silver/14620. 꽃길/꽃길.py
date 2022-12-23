def check(a, b):
    if abs(memo[a][0] - memo[b][0]) + abs(memo[a][1] - memo[b][1]) >= 3:
        return True
    return False


def cost_sum(i, j, k):
    if check(i, j) and check(j, k) and check(k, i):
        return memo[i][2] + memo[j][2] + memo[k][2]
    return 987654321

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

memo = []
for i in range(N):
    for j in range(N):
        if 0 < i < N-1 and 0 < j < N-1:
            costs = arr[i][j] + arr[i+1][j] + arr[i-1][j] + arr[i][j+1] + arr[i][j-1]
            memo.append((i, j, costs))
memo.sort(key=lambda x: x[2])

min_sum = 987654321
n = len(memo)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            csum = cost_sum(i, j, k)
            if min_sum > csum:
                min_sum = csum

print(min_sum)
