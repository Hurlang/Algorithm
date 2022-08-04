N = int(input())
coordinate = {}
for i in range(N):
    x, y = map(int, input().split())
    
    if coordinate.get(x):
        coordinate[x].append(y)
    else:
        coordinate[x]=[y]
        
coordinate = sorted(coordinate.items())

for x, y_list in coordinate:
    for y in sorted(y_list):
        print(x,y)
