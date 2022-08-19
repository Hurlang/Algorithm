day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
T = int(input())
for tc in range(1, T+1):
    S = input()
    for i in range(len(day)):
        if S == day[i]:
            if 6-i:
                print(f'#{tc} {6-i}')
            else:
                print(f'#{tc} {7}')