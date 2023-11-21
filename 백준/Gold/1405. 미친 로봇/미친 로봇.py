dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(n, k, p):
    global p_sum, r, c
    if n == k:
        p_sum += p
        return
    else:
        for i in range(4): # 한 방향씩 체크 -> 중복X: 좌표변경, 중복체크, dfs(n, k+1, p*p_list[i]). 중복O: pass
            if not visit.get((r+dr[i], c+dc[i]), 0):
                visit[r + dr[i], c + dc[i]] = 1
                r, c = r+dr[i], c+dc[i]
                dfs(n, k+1, p*p_list[i])
                visit[r, c] = 0
                r, c = r-dr[i], c-dc[i]

n, E, W, S, N = map(int, input().split(' '))
p_list = list(map(lambda x: x/100, [E, W, S, N]))
# print(p_list)

# 방문체크
visit = dict()
# visit[1,2] = 1
# print(visit.get((1, 3), 0))

p_sum = 0
r, c = 0, 0
visit[r, c] = 1
dfs(n, 0, 1)
print(p_sum)