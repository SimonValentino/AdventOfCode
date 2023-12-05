with open("day4/data.txt") as file:
    data = file.readlines()

data = [line[:-1] if line[-1] == "\n" else line for line in data]

total = 0
for line in data:
    sum = 0

    split = line.split("|")

    winning_nums = [int(num) for num in split[0].split() if num.isdigit()]
    nums = [int(num) for num in split[1].split() if num.isdigit()]

    for num in nums:
        if num in winning_nums:
            sum = 1 if sum == 0 else sum * 2

    total += sum

print("Total points:", total)
