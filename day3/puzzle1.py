total_joltage = 0

with open("day3/input.txt") as input:
    for bank in input.readlines():
        largest_1 = 0
        for battery in bank:
            battery = battery.strip()
            if battery == "":
                continue

            joltage = int(battery)

            if joltage > largest_1:
                largest_1 = joltage

        find = bank.find(str(largest_1))
        next = bank[find+1:]
        prev = bank[0:find]

        largest_2 = 0
        for battery in next:
            battery = battery.strip()
            if battery == "":
                continue

            joltage = int(battery)

            if joltage > largest_2:
                largest_2 = joltage
                
        if largest_2 == 0:
            for battery in prev:
                battery = battery.strip()
                if battery == "":
                    continue

                joltage = int(battery)

                if joltage > largest_2:
                    largest_2 = joltage
            
            num = int(str(largest_2) + str(largest_1))
        else:
            num = int(str(largest_1) + str(largest_2))        

        #print(num)

        total_joltage += num

print(total_joltage)