with open("day4/data.txt") as file:
    data = file.readlines()

data = [line[:-1] if line[-1] == "\n" else line for line in data]

num_instances = {card_num: 1 for card_num in range(1, len(data) + 1)}
card_num = 1
for line in data:
    split = line.split("|")

    winning_nums = [int(num) for num in split[0].split() if num.isdigit()]
    nums = [int(num) for num in split[1].split() if num.isdigit()]

    num_matches = 0
    for num in nums:
        if num in winning_nums:
            num_matches += 1
    
    for i in range(num_instances[card_num]):        
        for j in range(num_matches):
            num_instances[card_num + j + 1] += 1

    card_num += 1

total = 0
for value in num_instances.values():
    total += value

print("Total scratchcards:", total)
