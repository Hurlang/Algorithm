
T = int(input())

for tc in range(1, T+1):
    time = int(input())

    velocity = 0
    distance = 0
    for t in range(time):
        commands = input()
        command, var = int(commands[0]), int(commands[-1])

        if command == 0 :
            distance += velocity

        elif command == 1 :
            velocity += var
            distance += velocity

        else :
            velocity = velocity - var if velocity - var > 0 else 0
            distance += velocity

    print(f'#{tc} {distance}')

