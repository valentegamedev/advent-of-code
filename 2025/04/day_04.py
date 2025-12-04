input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        input_data.append(list(i.strip().replace('\r', '').replace('\n', '').replace('.','0').replace('@', '1')))

def get_number(i, j):
    if i < 0 or i >= len(input_data):
        return 0
    if j < 0 or j >= len(input_data[i]):
        return 0
    return int(input_data[i][j])

def sum_adjacent_digits(i, j) -> int:
    total = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            total += get_number(i + di, j + dj)
    return total

#1602
def do_part_1():
    rows = len(input_data)
    cols = len(input_data[0]) if rows else 0

    removed_papers = []

    valid_papers = 0
    for r in range(rows):
        for c in range(cols):
            if get_number(r, c) != 1:
                continue
            neigh = sum_adjacent_digits(r, c)
            if neigh < 4:
                removed_papers.append((r, c))
                valid_papers += 1

    for r in removed_papers:
        input_data[r[0]][r[1]] = '0'

    return valid_papers

#9518
def do_part_2():
    total_removed_papers = 0
    removed_papers = do_part_1()
    total_removed_papers += removed_papers
    while removed_papers > 0:
        removed_papers = do_part_1()
        total_removed_papers += removed_papers

    return total_removed_papers

if __name__ == '__main__':
    read_input_data()
    #print(do_part_1())
    print(do_part_2())

