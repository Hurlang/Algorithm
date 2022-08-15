#import sys; sys.stdin=open('공과잡초.txt')
def tnp(t, p):
    N = len(t)
    M = len(p)

    cnt = 0
    i = 0
    j = 0
    while i != N:
        if t[i] == p[j]:
            j += 1
        else:
            j = 0

        if j == M:
            cnt += 1
            j = 0
        i += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    t = input()
    p = '()'

    ball_shpae = 0
    for shape in t:
        if shape == '(' or shape == ')':
            ball_shpae += 1

    print(f'#{tc} {ball_shpae - tnp(t, p)}')