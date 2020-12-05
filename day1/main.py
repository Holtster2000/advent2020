file = open("input.txt", "r")
data = [int(x) for x in file.read().splitlines()]

data.sort()
result = (0, 0)
result2 = (0, 0, 0)

# Need to find numbers that add up to 2020 in data
for i in range(len(data)):
    num = data[i]
    target_num = 2020 - num

    for j in range(len(data)):
        num2 = data[-1 - j]

        # Part 1
        if target_num == num2:
            result = num, num2

        # Part 2
        if result2 == (0, 0, 0):
            target_num2 = target_num - num2
            if target_num2 in data[i:j]:
                result2 = num, target_num2, num2

        # Continue iterating if no solution found
        if target_num < num2 or result2 == (0, 0, 0):
            continue
        break

    if result != (0, 0) and result2 != (0, 0, 0):
        break

print(f"{result[0]} * {result[1]} = {result[0] * result[1]}")   # Part 1
print(f"{result2[0]} * {result2[1]} * {result2[2]} = {result2[0] * result2[1] * result2[2]}")   # Part 2
