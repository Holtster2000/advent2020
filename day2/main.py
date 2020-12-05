file = open("input.txt", "r")
lines = file.read().splitlines()
#lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

valid_count = 0
valid_count2 = 0
for line in lines:
    dash = line.find('-')
    s1 = line.find(' ')
    s2 = line.find(' ', s1 + 1)

    min_num = int(line[:dash])
    max_num = int(line[dash + 1:s1])
    char = line[s1 + 1]
    password = line[s2 + 1:]

    # Part one
    if password.count(char) in range(min_num, max_num + 1):
        valid_count += 1

    # Part two
    if (password[min_num - 1] == char) != (password[max_num - 1] == char):
        valid_count2 += 1

print(f"[Part 1] - There are {valid_count} valid passwords")
print(f"[Part 2] - There are {valid_count2} valid passwords")
