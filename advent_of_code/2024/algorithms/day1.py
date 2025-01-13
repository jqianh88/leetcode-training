from collections import Counter
def read_txt(filepath: str) -> tuple[list, list]:
    list1 = []
    list2 = []

    # Read the file line by line
    with open(filepath, 'r') as file:
        for line in file:
            # Split each line by whitespace
            col1, col2 = line.strip().split()
            list1.append(int(col1))
            list2.append(int(col2))
    return list1, list2


def main_logic_part1(list1: list, list2: list) -> int:
    total_diff = 0
    sortedl1 = sorted(list1)
    sortedl2 = sorted(list2)
    for (i, j) in zip(sortedl1, sortedl2):
        total_diff += abs(i-j)
    return total_diff

def main_logic_part2(list1: list, list2: list) -> int:
    total = 0
    list2counts = Counter(list2)
    for i in list1:
        if i in list2counts:
            total += list2counts[i] * i

    return total

if __name__ == '__main__':
    filepath = "/Users/jho/Documents/projects/leetcode-training/advent_of_code/2024/input_files/day1_input.txt"
    list1, list2 = read_txt(filepath=filepath)
    total = main_logic_part1(list1, list2)


    # Part 2: Similarity

    similarity_total = main_logic_part2(list1, list2)
    print(similarity_total)


