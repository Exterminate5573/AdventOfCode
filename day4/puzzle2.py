matrix = []

with open("day4/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        row = []
        for letter in line:
            if letter == "\n": continue
            row.append(letter)
        matrix.append(row)

total = 0

while True:
    changes = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            current = matrix[row][column]

            if current == ".":
                continue

            local_total = 0
            for next_row in [-1,0,1]:
                for next_column in [-1,0,1]:
                    x = row + next_row
                    y = column + next_column
                    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[row]) or (next_row == 0 and next_column == 0): 
                        continue
                    
                    check = matrix[x][y]

                    if check == "@":
                        local_total += 1

            if local_total < 4:
                total += 1
                matrix[row][column] = "."
                changes += 1

    if changes == 0:
        break

print("Total", total)