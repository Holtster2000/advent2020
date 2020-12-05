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
    for i in range(n):
        if in_str[i] == low:
            upper = math.floor((upper + lower) / 2)
        elif in_str[i] == up:
            lower = math.floor((upper + lower) / 2) + 1

    if lower != upper: raise ArithmeticError("Bad result for bsp using given params")
    return lower


# Get input as list of strings
file = open("input.txt", "r")
data = file.read().splitlines()

all_IDs = []

max_seatID = 0
max_pass = ""

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

# Find our seat id
all_IDs.sort()
myseatID = sum(range(all_IDs[0], all_IDs[-1] + 1)) - sum(all_IDs)

print(f"MaxID:{max_seatID} | PASS:{max_pass}")
print(f"My seat ID is {myseatID}")
