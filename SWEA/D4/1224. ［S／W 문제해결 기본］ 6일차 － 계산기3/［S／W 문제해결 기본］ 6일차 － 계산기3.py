def postfix(datas):
    stack = []
    expression = []

    isp = {'+': 1,
           '-': 1,
           '*': 2,
           '/': 2,
           '(': 0
           }
    icp = {'+': 1,
           '-': 1,
           '*': 2,
           '/': 2,
           '(': 3
           }

    for data in datas:
        if data in '+-/*()':
            if data == '(':
                stack.append('(')
            else:
                if data == ')':
                    while stack[-1] != '(':
                        expression.append(stack.pop())
                    stack.pop()
                else:
                    while stack and isp[stack[-1]] >= icp[data]:
                        expression.append(stack.pop())
                    stack.append(data)
        else:
            expression.append(data)

    while stack:
        expression.append(stack.pop())

    return expression

def calculator(expression):
    stack = []
    for data in expression:
        if data in '+-*/':
            if data == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif data == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif data == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 // num2)
        else:
            stack.append(int(data))

    return stack.pop()

for tc in range(1, 11):
    N = int(input())
    datas = input()
    
    print(f'#{tc} {calculator(postfix(datas))}')

