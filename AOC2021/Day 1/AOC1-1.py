count = 0
x = None
y = None
with open("C:\\Users\\athompson\\Documents\\AOC2021\\Day 1\\AOC1-1input.txt", "r") as file:
    for num in file:
        x = int(num)
        if (y != None) and x > y:
            count+=1
        y = int(num)
print(count)