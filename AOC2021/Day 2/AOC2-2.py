# FOR LOOPS BABYYYYY

distance = 0
depth = 0
aim = 0

with open("C:\\Users\\athompson\\Documents\\AOC2021\\Day 2\\AOC2-1input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    if "forward" in line:
        for word in line.split():
            if word.isdigit():
                distance+=int(word)
                depth+=(aim*int(word))
    elif "up" in line:
        for word in line.split():
            if word.isdigit():
                aim-=int(word)
    else:
        for word in line.split():
            if word.isdigit():
                aim+=int(word)

print(distance*depth)