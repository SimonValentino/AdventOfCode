with open("day3/data.txt") as file:
        data = file.readlines()

data = [line[:-1] if line[-1] == "\n" else line for line in data]

symbols = set({})

for row in data:
    for ch in row:
        if ch != "." and not ch.isdigit():
            symbols.add(ch)

rows, cols = len(data), len(data[0])
total_sum = 0
for row in range(rows):
    num_str = ""
    
    adj = False
    
    for col in range(cols):
        ch = data[row][col]
        
        if ch in symbols or ch == ".":
            total_sum += int(num_str) if num_str != "" and adj else 0
            num_str = ""
            adj = False
            continue
            
        num_str += ch
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row, new_col = row + i, col + j

                if not adj and 0 <= new_row < rows and 0 <= new_col < cols and data[new_row][new_col] in symbols:
                    adj = True
        
    total_sum += int(num_str) if num_str != "" and adj else 0

print(total_sum)
