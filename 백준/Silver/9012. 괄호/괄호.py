class Stack:
    stack = []
    
    @classmethod
    def push(cls, X):
        cls.stack.append(X)
    
    @classmethod
    def pop(cls):
        cls.stack.pop(len(cls.stack)-1)
        
    @classmethod
    def clear(cls):
        cls.stack.clear()
        
stack = Stack()

T = int(input())
for test_case in range(T):
    ans = ''
    parenthesis_string = input()
    for parenthesis in parenthesis_string:
        if parenthesis == '(':
            stack.push('(')
            
        else:
            if stack.stack:
                stack.pop()
            else:
                ans = 'NO'
                break
                
    if not stack.stack and ans == '':
        ans = 'YES'
        
    else:
        ans = 'NO'
        
    print(ans)
    stack.clear()
    