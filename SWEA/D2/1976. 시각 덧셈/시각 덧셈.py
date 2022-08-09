T = int(input())

for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    
    h = (h1 + h2 + (m1 + m2) // 60 ) % 13 + (h1 + h2 + (m1 + m2) // 60 ) // 13
    m = (m1 + m2) % 60
    
    print(f'#{tc} {h} {m}')