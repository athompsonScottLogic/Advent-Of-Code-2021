count = 0
a = 0
b = 0
x = None
y = None
z = None
with open("C:\\Users\\athompson\\Documents\\AOC2021\\Day 1\\AOC1-1input.txt", "r") as file:
    for num in file:
        if x == None:
            x = int(num)
        elif y == None:
            y = int(num)
        elif z == None:
            z = int(num)

        if x != None and y != None and z != None and b != None:
            a = x+y+z
            if a > b and a != 0 and b != 0:
                print(str(a) + " - " + str(b))
                count += 1

            b = x+y+z
            
            x = y
            y = z
            z = int(num)
        
print(count)