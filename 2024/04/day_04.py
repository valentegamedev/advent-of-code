letter_grid = []

def read_letter_grid():
    f = open("input/day_04.txt", "r")
    for x in f:
        letter_grid.append(x.strip())
    print(letter_grid)

def is_within_bounds(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def matches_word(start_r, start_c, direction, grid, word):
    r, c = start_r, start_c
    dr, dc = direction
    for i in range(len(word)):
        if not is_within_bounds(r, c, grid) or grid[r][c] != word[i]:
            return False
        r += dr
        c += dc
    return True


def find_xmas_occurrences_part1(grid):
    word = "XMAS"

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (0, 1),   #Right
        (0, -1),  #Left
        (1, 0),   #Down
        (-1, 0),  #Up
        (1, 1),   #Down-Right
        (1, -1),  #Down-Left
        (-1, 1),  #Up-Right
        (-1, -1)  #Up-Left
    ]

    for r in range(rows):
        for c in range(cols):
            for direction in directions:
                if matches_word(r, c, direction, grid, word):
                    count += 1
    print(count)


def is_valid_xmas(center_r, center_c, grid, mas_patterns):
    for i_mas in mas_patterns:
        for j_mas in mas_patterns:
            if (
                grid[center_r - 1][center_c - 1] == i_mas[0]
                and grid[center_r][center_c] == i_mas[1]
                and grid[center_r + 1][center_c + 1] == i_mas[2]
            ):
                if (
                    grid[center_r - 1][center_c + 1] == j_mas[0]
                    and grid[center_r][center_c] == j_mas[1]
                    and grid[center_r + 1][center_c - 1] == j_mas[2]
                ):
                    return True
    return False


def find_xmas_pattern_part2(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    mas_patterns = [("M", "A", "S"), ("S", "A", "M")]

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                if is_valid_xmas(r, c, grid, mas_patterns):
                    count += 1

    print(count)


if __name__ == '__main__':
    read_letter_grid()
    #find_xmas_occurrences_part1(letter_grid)
    find_xmas_pattern_part2(letter_grid)




