with open("day2/data.txt") as file:
        data = file.readlines()

data = [line[:-1] if line[-1] == "\n" else line for line in data]

r_max = 12
b_max = 14
g_max = 13

games = [line.split(": ")[1].split("; ") for line in data]
powers = []

for i in range(len(games)):
    mins = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for drawing in games[i]:
        freqs = {
            "red": 0,
            "blue": 0,
            "green": 0
        }

        colors = drawing.split(", ")
        for color in colors:
            sections = color.split(" ")
            freqs[sections[-1]] += int(sections[0])

        if freqs["red"] > mins["red"]:
            mins["red"] = freqs["red"]
        if freqs["green"] > mins["green"]:
            mins["green"] = freqs["green"]
        if freqs["blue"] > mins["blue"]:
            mins["blue"] = freqs["blue"]

    power = mins["red"] * mins["green"] * mins["blue"]
    powers.append(power)

print(sum(powers))
