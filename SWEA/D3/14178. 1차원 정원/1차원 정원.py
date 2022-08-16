#import sys; sys.stdin=open('1차원 정원.txt')
import math

T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())

    bounds = D * 2 + 1

    min_cnt = int(math.ceil(N/bounds))

    print(f'#{tc} {min_cnt}')