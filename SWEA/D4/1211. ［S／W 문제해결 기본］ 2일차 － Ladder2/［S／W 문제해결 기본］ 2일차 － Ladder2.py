#import sys; sys.stdin=open('Ladder2.txt')
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for __ in range(100)]



    # 최단 거리
    min_distance = 100 * 100 # 충분히 큰 수
    min_start = 0

    # 출발점 찾기
    for start in range(100):
        i = 0
        j = 0
        distance = 0
        if arr[0][start] == 1 :
            j = start
            x = start
            while i != 99:
                # 1-1 좌 탐색
                flag = True
                while 0 < j < 100 and arr[i][j-1] == 1:
                    j -= 1 # 좌로 이동
                    distance += 1
                    flag = False

                # 1-2 우 탐색
                while flag and 0 <= j < 99 and arr[i][j+1] == 1:
                    j += 1 # 우로 이동
                    distance += 1


                # 2 아래로 이동
                i += 1
                distance += 1

            if distance <= min_distance :
                min_distance = distance
                min_start = x

    print(f'#{tc} {min_start}')


