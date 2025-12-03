total = 0

with open("day2/input.txt") as input:
    line = input.readline()
    ids = line.split(",")
    for id in ids:
        id.replace(",", "")

        split = id.split("-")
        first_id = split[0].replace("-", "")
        last_id = split[1].replace("-", "")

        for i in range(first_id.__len__()).__reversed__():
            sequence = first_id[0:-i]
            next_seq = first_id[i:]

            print(sequence)

            if (i != 0 and last_id.__contains__(sequence)) or (next_seq.startswith(sequence)):
                total += int(sequence)
                break

print("Total: ", total)