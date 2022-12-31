N, L = map(int, input().split())                            # N: 한 변의 길이, L: 경사로의 길이
arr = [list(map(int, input().split())) for _ in range(N)]   # 입력 배열

ans = 0
for i in range(N):
                                                            ## 가로 검사
    j = 1                                                   # j: 열 번호
    height = arr[i][0]                                      # height: 이전 열의 높이
    flag = False                                            # flag: 부적합 판정
    cnt = L - 1                                             # cnt: 경사로를 설치하려면 cnt개 더 필요

    while j != N:                                           # 종료 조건: j == N
        if height == arr[i][j]:                                 # if 이전 높이 == 현재 높이
            cnt -= 1                                                # 경사로 길이 측정 -= 1 -> 적합에 가까워짐

        elif abs(height - arr[i][j]) <= 1:                      # 이전 높이와 현재 높이의 차이가 1 이하이면

            if height > arr[i][j]:                                # elif 이전 높이 > 현재 높이
                height = arr[i][j]                                      # 높이 변경
                for k in range(1, L):
                    if j + 1 < N and height == arr[i][j+1]:             # 다음 열이 인덱스 내에 있고, 이전 높이와 같으면
                        j += 1                                              # 열을 한 칸 이동
                    else:                                               # 조건에 어긋나면
                        flag = True                                         # 부적합 판정 ON
                        break                                               # for문 탈출
                if flag:                                                # 부적합 판정 ON이면
                    break                                               # while문 탈출
                cnt = L

            elif height < arr[i][j]:                                # elif 이전 높이 < 현재 높이
                if cnt <= 0:                                            # 경사로 길이 측정에 통과하면 (cnt <= 0 이면)
                    height = arr[i][j]                                      # 높이 변경
                    cnt = L-1                                               # cnt 초기화
                else:                                                   # 조건에 어긋나면
                    flag = True                                             # 부적합 판정 ON
                    break                                                   # while문 탈출

        else:                                                    # 이전 높이와 현재 높이가 2 이상 차이나면
            flag = True                                             # 부적합판정 ON
            break                                                   # while문 탈출

        j += 1

                                                            # 한 변을 검사 했을 때
    if not flag:                                            # 적합 판정이라면
        ans += 1

                                                        ## 세로 검사
    j = 1                                                   # j: 행 번호
    height = arr[0][i]                                      # height: 이전 행의 높이
    flag = False                                            # flag: 부적합 판정
    cnt = L - 1                                             # cnt: 경사로를 설치하려면 cnt개 더 필요

    while j != N:                                           # 종료 조건: j == N
        if height == arr[j][i]:                                 # if 이전 높이 == 현재 높이
            cnt -= 1                                                # 경사로 길이 측정 -= 1 -> 적합에 가까워짐

        elif abs(height - arr[j][i]) <= 1:                      # 이전 높이와 현재 높이의 차이가 1 이하이면

            if height > arr[j][i]:                                # elif 이전 높이 > 현재 높이
                height = arr[j][i]                                      # 높이 변경
                for k in range(1, L):
                    if j + 1 < N and height == arr[j+1][i]:             # 다음 행이 인덱스 내에 있고, 이전 높이와 같으면
                        j += 1                                              # 행을 한 칸 이동
                    else:                                               # 조건에 어긋나면
                        flag = True                                         # 부적합 판정 ON
                        break                                               # for문 탈출
                if flag:                                                # 부적합 판정 ON이면
                    break                                               # while문 탈출
                cnt = L

            elif height < arr[j][i]:                                # elif 이전 높이 < 현재 높이
                if cnt <= 0:                                            # 경사로 길이 측정에 통과하면 (cnt <= 0 이면)
                    height = arr[j][i]                                      # 높이 변경
                    cnt = L-1                                               # cnt 초기화
                else:                                                   # 조건에 어긋나면
                    flag = True                                             # 부적합 판정 ON
                    break                                                   # while문 탈출

        else:                                                    # 이전 높이와 현재 높이가 2 이상 차이나면
            flag = True                                             # 부적합판정 ON
            break                                                   # while문 탈출

        j += 1

                                                            # 한 변을 검사 했을 때
    if not flag:                                            # 적합 판정이라면
        ans += 1

print(ans)