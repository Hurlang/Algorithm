chars = input().upper()
char_dict = {}

for char in chars:
    if not char_dict.get(char):
        char_dict[char] = 1
    else:
        char_dict[char] += 1

max_key = ''
max_value = 0
for key, value in char_dict.items():
    if max_value < value:
        max_key = key
        max_value = value
        
if list(char_dict.values()).count(max_value) >= 2:
    max_key ='?'
    
print(max_key)
        
    