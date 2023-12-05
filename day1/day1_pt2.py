with open("day1/data.txt") as file:
        data = file.readlines()

data = [line[:-1] if line[-1] == "\n" else line for line in data]

sum = 0
for line in data:
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")

    i = 0
    while i < len(line) - 1 and not line[i].isdigit():
        i += 1
    sum += int(line[i]) * 10

    j = len(line) - 2
    while j >= 0 and not line[j].isdigit():
        j -= 1
    sum += int(line[j])

print(sum)
