
T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    A = W * P # W리터 * P원
    B = Q if W < R else Q + (W - R) * S

    print(f'#{tc} {A if A < B else B}')
