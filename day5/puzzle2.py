total = 0

with open("day5/input.txt") as input:
    fresh_ranges = []

    for line in input.readlines():
        line = line.strip()
        if line.find("-") != -1:
            split = line.split("-")
            
            start = int(split[0])
            end = int(split[1])

            fresh_ranges.append((start, end))
        else:
            break

    changed = True
    while changed:
        changed = False
        for j in range(fresh_ranges.__len__()):
            if changed:
                break
            start, end = fresh_ranges[j]
            for i in range(fresh_ranges.__len__()):
                lstart, lend = fresh_ranges[i]
                if j == i:
                    continue
                elif start >= lstart and end <= lend:
                    fresh_ranges.remove((start, end))
                    changed = True
                    break
                elif start >= lstart and start <= lend and end >= lend:
                    fresh_ranges[i] = (lstart, end)
                    changed = True
                    break
                elif start <= lstart and end <= lend and end >= lstart:
                    fresh_ranges[i] = (start, lend)
                    changed = True
                    break
                elif start <= lstart and end >= lend:
                    fresh_ranges[i] = (start, end)
                    changed = True
                    break

    for start, end in fresh_ranges:
        count = end - start + 1
        total += count

print("Total: ", total)
