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
gears = {}
for row in range(rows):
    num_str = ""
    gear_coordinate = None
    adj_gear = False

    for col in range(cols):
        ch = data[row][col]

        if ch in symbols or ch == ".":
            if gear_coordinate not in gears:
                gears[gear_coordinate] = []
            gears[gear_coordinate].append(
                int(num_str) if num_str != "" and adj_gear else 0)
            num_str = ""
            adj_gear = False
            continue

        num_str += ch

        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row, new_col = row + i, col + j

                if not adj_gear and 0 <= new_row < rows and 0 <= new_col < cols and data[new_row][new_col] == "*":
                    adj_gear = True
                    gear_coordinate = (new_row, new_col)

    if gear_coordinate not in gears:
        gears[gear_coordinate] = []
    gears[gear_coordinate].append(
        int(num_str) if num_str != "" and adj_gear else 0)

for key, value in gears.items():
    gears[key] = [num for num in value if num != 0]

gears = {key: value for key, value in gears.items() if key is not None and len(value) > 1}

total = 0
for value in gears.values():
    product = 1
    for num in value:
        product *= num
    total += product

print(total)
