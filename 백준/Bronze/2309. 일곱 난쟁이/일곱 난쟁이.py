def cal(heights):
    total_heights = sum(heights)
    for i in range(8):
        for j in range(i+1,9):
            if total_heights - heights[i] - heights[j] == 100:
                heights.remove(heights[j])
                heights.remove(heights[i])
                return heights

heights = []
for i in range(9):
    heights.append(int(input()))
    
heights = cal(heights)

      
for height in sorted(heights):
    print(height)