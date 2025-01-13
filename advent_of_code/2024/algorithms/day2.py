'''
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
'''

from collections import Counter
def read_txt(filepath: str) -> list[list]:
    reports = []

    # Read the file line by line
    with open(filepath, 'r') as file:
        for line in file:
            # Split each line by whitespace
            levels = list(map(int, line.strip().split()))
            reports.append(levels)
    return reports


def main_logic_part1(report: list[list]) -> int:
    unsafe = 0
    safe = 0
    for row in report:
        direction = 1 if (row[1] - row[0]) > 0 else -1
        for i in range(1, len(row)):
            nextdirection = 1 if (row[i] - row[i-1]) > 0 else -1
            if not (1 <= abs(row[i] - row[i-1]) <= 3) or direction != nextdirection:
                unsafe += 1
        if unsafe == 0:
            safe += 1
        else:
            unsafe = 0

    return safe


def is_safe(row: list[int]) -> bool:
    """Helper function to check if a row is safe without any removals."""
    if len(row) < 2:
        return True  # A single level or empty row is trivially safe

    direction = 1 if (row[1] - row[0]) > 0 else -1
    for i in range(1, len(row)):
        next_direction = 1 if (row[i] - row[i - 1]) > 0 else -1
        if not (1 <= abs(row[i] - row[i - 1]) <= 3) or next_direction != direction:
            return False  # Found an unsafe transition
    return True  # Entire row is safe

# time: O(n*m) and space: O(1)
def main_logic_part2(report: list[list[int]]) -> int:
    safe_count = 0

    for row in report:
        if is_safe(row):
            safe_count += 1  # The row is safe without any removals
            continue

        # Try removing each level and check if it makes the row safe
        for i in range(len(row)):
            # Create a new sequence without the i-th level
            new_row = row[:i] + row[i + 1:]
            if is_safe(new_row):
                safe_count += 1
                break  # No need to try further removals for this row

    return safe_count


# Optimized: time: O(n*m) and space: O(m)
def is_safe_with_removal(row, remove_idx):
    """Check if the row becomes safe after removing the level at remove_idx."""
    n = len(row)
    if n < 2:
        return True  # Trivially safe if there's 1 or 0 levels

    # Check transitions around the removed index
    if remove_idx > 0 and remove_idx < n - 1:
        # Check transition: row[remove_idx - 1] -> row[remove_idx + 1]
        prev, next_ = row[remove_idx - 1], row[remove_idx + 1]
        if not (1 <= abs(next_ - prev) <= 3):
            return False
        # Check direction consistency
        prev_direction = 1 if (next_ - prev) > 0 else -1
        current_direction = 1 if (row[1] - row[0]) > 0 else -1
        return prev_direction == current_direction

    return True
def main_logic_part2optimized(report):
    safe_count = 0
    for row in report:
        if is_safe(row):
            safe_count += 1
            continue

        # Check if removing one level makes the row safe
        for i in range(len(row)):
            if is_safe_with_removal(row, i):
                safe_count += 1
                break

    return safe_count

if __name__ == '__main__':
    filepath = "/Users/jho/Documents/projects/leetcode-training/advent_of_code/2024/input_files/day2_input.txt"
    reports = read_txt(filepath=filepath)
    safe = main_logic_part1(reports)


    # # Part 2: Problem Dampener

    safe2 = main_logic_part2(reports)





