class Stack:
    stack = []
    
    @classmethod
    def push(cls,X):
        cls.stack.append(X)
    
    @classmethod
    def pop(cls):
        return cls.stack.pop(len(cls.stack)-1) if cls.stack else ''
    
        

T = int(input())
stack = Stack()

for i in range(T):
    sentence = input()
    new_sentence = ''
    for idx, char in enumerate(sentence):
        if char == ' ':
            while stack.stack:
                new_sentence += stack.pop()
            new_sentence += ' '
        else:
            stack.push(char)
            
        if idx == len(sentence)-1:
            while stack.stack:
                new_sentence += stack.pop()
    print(new_sentence)
            