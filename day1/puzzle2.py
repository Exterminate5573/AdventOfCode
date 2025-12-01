dial = 50
zeros = 0

with open("day1/input.txt") as file:
    for line in file.readlines():
        direction = line[0]
        amount = int(line[1:])

        if direction == "R":
            for i in range(amount):
                dial += 1

                if dial == 100:
                    dial = 0

                if dial == 0:
                    zeros += 1
        elif direction == "L":
            for i in range(amount):
                dial -= 1

                if dial == -1:
                    dial = 99

                if dial == 0:
                    zeros += 1
        else:
            print("Error: " + direction)
        


print("Zeros: ", zeros)      