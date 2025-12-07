total = 0

with open("day6/input.txt") as input:
    numbers = []

    i = 0
    for line in input.readlines():
        numbers.append([])
        split = line.split(" ")
        for num in split:
            if num == "":
                continue
            
            numbers[i].append(num.strip())
        i += 1

    length = numbers[0].__len__()
    for j in range(length):
        local_total = 0
        nums = []
        for k in range(numbers.__len__()):
            l = numbers[k][j]
            if l == "+":
                operator = lambda x, y: x + y
            elif l == "*":
                local_total = 1
                operator = lambda x, y: x * y
            else:
                nums.append(int(l))

        for num in nums:
            local_total = operator(local_total, num)

        total += local_total

print(total)