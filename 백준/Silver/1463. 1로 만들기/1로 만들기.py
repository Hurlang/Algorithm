def f(n, k):
    global min_cnt

    if k > min_cnt:
        return

    if n == 1:
        min_cnt = min_cnt if min_cnt < k else k

    if n % 3 == 0:
        f(n//3, k+1)

    if n % 2 == 0:
        f(n//2, k+1)

    f(n-1, k+1)


N = int(input())
min_cnt = 987654321
f(N, 0)
print(min_cnt)