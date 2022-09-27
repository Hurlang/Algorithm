def perm(n, k):
    if n == k:
        print(*p)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k+1)
                visited[i] = 0


N = int(input())
a = [i+1 for i in range(N)]
p = [0] * N
visited = [0] * N
perm(N, 0)