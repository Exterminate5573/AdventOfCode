total_joltage = 0

def find_largest(bank):
    largest = 0

    for battery in bank:
        battery = battery.strip()
        if battery == "":
            continue

        joltage = int(battery)

        if joltage > largest:
            largest = joltage

    find = bank.find(str(largest))
    next = bank[find+1:]
    prev = bank[0:find]

    return largest, next, prev

with open("day3/input.txt") as input:
    for bank in input.readlines():
        largest, next, prev = find_largest(bank)
        
        size_store = str(largest)

        remaining = 11
        while remaining > 0:
            if next.__len__() > 0:
                largest, next, prev = find_largest(next)
                size_store = size_store.join(str(largest))
                remaining -= 1
            elif prev.__len__() > 0:
                largest, next, prev = find_largest(prev)
                size_store = size_store.join(str(largest))
                remaining -= 1
            else:
                print("Issue")
            
        print(size_store)

        total_joltage += int(size_store)
            

            
