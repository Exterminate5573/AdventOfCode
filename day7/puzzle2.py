total = 0

with open("day7/input.txt") as input:
    matrix = []
    for line in input.readlines():
        line = list(line.strip())
        matrix.append(line)
        
    beams = [matrix[0].index("S")]

    for i in range(matrix.__len__()):
        new_beams = beams.copy()
        for beam in beams:
            if matrix[i][beam] == "^":
                total += 1
                new_beams.remove(beam)
                if new_beams.count(beam - 1) == 0:
                    new_beams.append(beam - 1)
                if new_beams.count(beam + 1) == 0:
                    new_beams.append(beam + 1)


        beams = new_beams # Python moment

#total = total * 2