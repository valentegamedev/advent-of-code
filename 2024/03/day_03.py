import re

corrupted_memory = ""

def fill_memory():
    global corrupted_memory
    f = open("input/day_03.txt", "r")
    for x in f:
        corrupted_memory += x.strip()
    print(corrupted_memory)


def sum_valid_mul_instructions_part2(p_corrupted_memory):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    pattern = rf"{mul_pattern}|{do_pattern}|{dont_pattern}"

    enabled = True
    total_sum = 0

    for match in re.finditer(pattern, p_corrupted_memory):
        #print(match.groups())
        if match.group(1) and match.group(2):
            x, y = int(match.group(1)), int(match.group(2))
            if enabled:
                total_sum += x * y
        elif match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False

    print(total_sum)


def sum_valid_mul_instructions_part1(p_corrupted_memory):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, p_corrupted_memory)
    print(matches)
    total_sum = sum(int(x) * int(y) for x, y in matches)
    print(total_sum)


if __name__ == '__main__':
    fill_memory()
    #corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    #sum_valid_mul_instructions_part1(corrupted_memory)
    sum_valid_mul_instructions_part2(corrupted_memory)



