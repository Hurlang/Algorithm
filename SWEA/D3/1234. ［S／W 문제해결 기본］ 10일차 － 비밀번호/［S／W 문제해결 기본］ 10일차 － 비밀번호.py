#import sys; sys.stdin = open('비밀번호.txt')
for tc in range(1, 11):
    N, datas = input().split()
    stack = []
    for data in datas:
        if stack:
            if stack[-1] != data:
                stack.append(data)
            else:
                stack.pop()
        else:
            stack.append(data)

    print(f'#{tc} {"".join(stack)}')