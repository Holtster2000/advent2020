file = open("input.txt", "r")
groups = [string.split() for string in file.read().split(sep="\n\n")]

total = 0
total2 = 0

for group in groups:
    # Create a dict of all questions and start the count at zero
    question_dict = {}
    for i in range(26):
        question_dict[chr(ord('a')+i)] = 0

    # For each person's response, add one to that question's count
    for person in group:
        for yes in person:
            question_dict[yes] += 1

    # Check the criteria for part 1 and 2 of the prompt
    for q, count in question_dict.items():
        if count != 0:  # If anyone answered yes
            total += 1
        if count == len(group):  # If ALL answered yes
            total2 += 1

print(f"Part1: {total}")
print(f"Part2: {total2}")
