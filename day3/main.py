from colorama import Fore
from copy import copy
from functools import reduce


file = open("input.txt", "r")
data = file.read().splitlines()
# data = [
#     "..##.......",
#     "#...#...#..",
#     ".#....#..#.",
#     "..#.#...#.#",
#     ".#...##..#.",
#     "..#.##.....",
#     ".#.#.#....#",
#     ".#........#",
#     "#.##...#...",
#     "#...##....#",
#     ".#..#...#.#"
# ]

width = len(data[0])
length = len(data)

x, y = 0, 0    # start in top left of map
slope_map = [copy(data)]
slope_map_page = 0
max_slope_map_page = 0
tree_count = 0

# Definition of all slopes to check
# (right, down, tree, free, color)
slopes = [
    (1, 1, 'A', 'B', Fore.RED),
    (3, 1, 'C', 'D', Fore.GREEN),
    (5, 1, 'E', 'F', Fore.BLUE),
    (7, 1, 'G', 'H', Fore.YELLOW),
    (1, 2, 'I', 'J', Fore.MAGENTA)
]

tree_chars = [s[2] for s in slopes]
results = []

for slope in slopes:
    x, y = 0, 0  # start in top left of map
    slope_map_page = 0
    tree_count = 0
    while y < length - 1:
        # Move 3 right and 1 down
        x += slope[0]
        y += slope[1]

        # Scroll right if needed
        slope_map_page = x // width
        if slope_map_page > len(slope_map) - 1:
            slope_map.append(copy(data))
        if slope_map_page > max_slope_map_page:
            max_slope_map_page = slope_map_page

        # Check for tree at new position
        s = slope_map[slope_map_page][y]
        if s[x - slope_map_page * width] == '#' or s[x - slope_map_page * width] in tree_chars:
            tree_count += 1
            slope_map[slope_map_page][y] = s[:x-slope_map_page * width] + slope[2] + s[(x-slope_map_page * width)+1:]
        else:
            slope_map[slope_map_page][y] = s[:x-slope_map_page * width] + slope[3] + s[(x-slope_map_page * width)+1:]
    results.append(tree_count)

# Print results
for i, s in enumerate(slopes):
    print(f"{s[4]}Slope: {s[0]} right, {s[1]} down -> {results[i]}{Fore.RESET}")
print(f"\nPart 2 result = {reduce((lambda a, b: a * b), results)}")

# Print slope map (pretty!)
for r in range(length):
    for p in range(max_slope_map_page + 1):
        for s in slopes:
            slope_map[p][r] = slope_map[p][r].replace(s[2], s[4] + "O" + Fore.RESET)
            slope_map[p][r] = slope_map[p][r].replace(s[3], s[4] + "X" + Fore.RESET)
        print(slope_map[p][r], end="")
    print("")
