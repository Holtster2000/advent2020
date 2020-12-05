import math
from typing import Tuple


def bsp(in_str: str, low: chr, up: chr, start: Tuple[int, int], n: int) -> int:
    """
    Finds the number using binary search partitioning.

    :param in_str: string to process.
    :param low: char that specifies to keep the lower half
    :param up: char that specifies to keep the upper half
    :param start: Tuple of (start, end) bounds
    :param n: int number of iterations.
    :return: int result of the BSP process.
    """

    lower = start[0]
    upper = start[1]
    for c in range(n):
        if in_str[c] == low:
            upper = math.floor((upper + lower) / 2)
        elif in_str[c] == up:
            lower = math.floor((upper + lower) / 2) + 1
        else:
            raise ValueError(f"bsp: Unexpected char '{in_str[c]}'. (Expected '{low}' or '{up}')")

    if lower != upper:
        raise ValueError(f"bsp: Bad result using given params ({lower} != {upper} at end of execution)")
    return lower


# Get input as list of strings
file = open("input.txt", "r")
data = file.read().splitlines()

max_seatID = 0
max_pass = ""

all_IDs = []
num_IDs = 0

for seat in data:

    # Find row number
    row = bsp(seat, 'F', 'B', (0, 127), 7)

    # Find column number
    col = bsp(seat[-3:], 'L', 'R', (0, 7), 3)

    # Calculate max seat ID
    seatID = row * 8 + col
    if seatID > max_seatID:
        max_seatID = seatID
        max_pass = seat

    # Add to master list
    all_IDs.append(seatID)
    num_IDs += 1

# Find our seat id (cant be first or last)
all_IDs.sort()
myseatID = 0
for i in range(1, num_IDs):
    # If the previous ID isn't one away, we found the missing ID
    if all_IDs[i - 1] + 1 != all_IDs[i]:
        myseatID = all_IDs[i - 1] + 1
        break

print(f"MaxID:{max_seatID} | PASS:{max_pass}")  # Part 1
print(f"My seat ID is {myseatID}")              # Part 2
