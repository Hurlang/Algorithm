def f(n):
    global cnt
    if n == N:
        cnt += 1
    elif n > N:
        return

    for x in [n+1, n+2, n+3]:
        f(x)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    f(0)
    print(cnt)