total = 0

with open("day5/input.txt") as input:
    fresh_ranges = []

    for line in input.readlines():
        line = line.strip()
        if line.find("-") != -1:
            split = line.split("-")
            fresh_ranges.append((int(split[0]), int(split[1])))
        else:
            if line == "":
                continue

            is_fresh = False

            product = int(line)
            for start, end in fresh_ranges:
                if product >= start and product <= end:
                    is_fresh = True

            if is_fresh:
                total += 1

print("Total: ", total)