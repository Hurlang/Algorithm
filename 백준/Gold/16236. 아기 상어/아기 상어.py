from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]                                                           # 방향벡터

def bfs(i, j):                                                                                  # bfs 함수
    q = deque()                                                                               
    q.append((i, j))                                                                            # 현재 상어의 위치를 q에 append
    while q:                                                                                    # q에 원소가 있는 동안
        x, y = q.popleft()                                                                      # q의 첫번째 원소를 뽑아내 x, y에 대입
        for k in range(4):                                                                      # 4방향으로 탐색
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] <= level:   # 벽체크 + 방문체크 + 물고기의 크기가 작거나 같은 경우
                q.append((nx, ny))                                                              # q에 append (이동가능하다고 간주)
                visited[nx][ny] = visited[x][y] + 1                                             # 방문체크 + 상어와 물고기간의 거리 표시
                if 0 < arr[nx][ny] < level:                                                     # 먹을 수 있는 물고기라면
                    can_eat.append([visited[nx][ny], nx, ny])                                   # can_eat에 append (거리, 좌표)
                    

N = int(input())                                            # 공간의 크기
arr = [list(map(int, input().split())) for _ in range(N)]   # 입력 배열
level = exp = 2                                             # level: 상어의 크기, exp: 진화에 필요한 경험치
# for item in arr:
#     print(*item)


# 상어의 위치 찾기
shark = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark = [i, j]

# print(shark)
# 상어로부터 물고기의 거리와, 물고기의 좌표를 파악
time = 0                                                    # 시간(초)
while True:
    visited = [[0] * N for _ in range(N)]
    visited[shark[0]][shark[1]] = 1                         # 상어의 현재 위치를 방문체크 
    can_eat = []                                            # 먹을 수 있는 물고기를 저장하는 배열 초기화
    bfs(shark[0], shark[1])                                 # 현재 상어의 위치에서 bfs함수 실행
    if can_eat:                                             # 먹을 수 있는 물고기가 있다면
        arr[shark[0]][shark[1]] = 0                             # 현재 상어의 위치를 0으로 변경
        can_eat.sort()                                          # 먹을 수 있는 물고기를 거리순, 좌표순으로 정렬
        # print(can_eat)                                        
        shark = can_eat[0][1:]                                  # 상어의 위치를 가장 가까운 먹을 수 있는 물고기의 위치로 변경
        arr[shark[0]][shark[1]] = 9                             # 그 좌표를 9로 바꿈 (사실 필요x)
        exp -= 1                                                # 물고기를 한 마리 먹었으므로 진화에 필요한 경험치 -1
        if exp == 0:                                            # 만약 진화에 필요한 경험치가 0이라면
            level += 1                                              # level += 1
            exp = level                                             # exp는 level 만큼 채움
    else:                                                   # 먹을 수 있는 물고기가 없다면
        break                                                   # 종료
    time += can_eat[0][0] - 1                               # 물고기를 먹기 위해 움직인 거리만큼 time에 더해줌

print(time)