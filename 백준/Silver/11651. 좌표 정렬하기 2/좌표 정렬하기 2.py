# y 좌표 증가
N = int(input())
coordinate = {}
for i in range(N):
    x, y = map(int, input().split())
    
    if coordinate.get(y):
        coordinate[y].append(x)
    else:
        coordinate[y]=[x]
        
coordinate = sorted(coordinate.items())

for y, x_list in coordinate:
    for x in sorted(x_list):
        print(x,y)