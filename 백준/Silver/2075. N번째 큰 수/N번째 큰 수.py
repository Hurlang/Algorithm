# N * N 크기의 배열에서 N번째 큰 수를 찾는 문제

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_row = []
for i in range(N):
    max_row.append([N-1, i])

Nth_Max_Value = 0
for i in range(N):
    max_idx = 0
    for j in range(1, N):
        if arr[max_row[max_idx][0]][max_row[max_idx][1]] < arr[max_row[j][0]][max_row[j][1]]:
            max_idx = j
    Nth_Max_Value = arr[max_row[max_idx][0]][max_row[max_idx][1]]
    max_row[max_idx][0] -= 1
    
print(Nth_Max_Value)