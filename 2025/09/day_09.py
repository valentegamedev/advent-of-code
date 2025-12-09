from collections import deque
from itertools import combinations
import pyrect
import numpy as np

tiles = []
input_data = []
input_data_original = []
visited = set()

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        tiles_string = i.strip().replace('\r', '').replace('\n', '').split(',')
        input_data.append((int(int(tiles_string[0])/100), int(int(tiles_string[1])/100)))
        input_data_original.append((int(int(tiles_string[0]) / 1), int(int(tiles_string[1]) / 1)))

    wall_area = pyrect.Rect(input_data[0][0], input_data[0][1], 1, 1)
    for tile in input_data:
        wall_area.union(pyrect.Rect(tile[0], tile[1], 1, 1))

    for i in range(0, (wall_area.height+wall_area.y)):
        row = ['.'] * (wall_area.width + wall_area.x)
        tiles.append(row)

    for tile in input_data:
        tiles[tile[1]][tile[0]] = '#'

#4749929916
def do_part_1():
    biggest_area = 0
    for i, j in combinations(input_data_original, 2):
        x1, y1 = i
        x2, y2 = j
        w = abs(x2 - x1)
        h = abs(y2 - y1)
        area = (w + 1) * (h + 1)
        if area > biggest_area:
            biggest_area = area

    return biggest_area

def fill_line(start, end):
    sx, sy = start
    ex, ey = end

    if sy == ey:
        y = sy
        x1, x2 = sorted((sx, ex))
        for x in range(x1, x2 + 1):
            if (x, y) not in (start, end):
                tiles[y][x] = 'O'
    elif sx == ex:
        x = sx
        y1, y2 = sorted((sy, ey))
        for y in range(y1, y2 + 1):
            if (x, y) not in (start, end):
                tiles[y][x] = 'O'

def flood_fill_outside_corners():
    H = len(tiles)
    W = len(tiles[0]) if H else 0
    if H == 0 or W == 0:
        return

    q = deque()
    corners = [(0, 0), (W-1, 0), (0, H-1), (W-1, H-1)]
    for x, y in corners:
        if 0 <= x < W and 0 <= y < H and tiles[y][x] == '.':
            tiles[y][x] = 'X'
            q.append((x, y))

    dirs = ((1,0), (-1,0), (0,1), (0,-1))
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and tiles[ny][nx] == '.':
                tiles[ny][nx] = 'X'
                q.append((nx, ny))

def rect_is_allowed(x1, y1, x2, y2):
    c0, c1 = min(x1, x2), max(x1, x2)
    r0, r1 = min(y1, y2), max(y1, y2)
    for y in range(r0, r1+1):
        # early skip if any outside 'X' appears
        row = tiles[y]
        for x in range(c0, c1+1):
            if row[x] not in ('#', 'O','.'):
                return False
    return True

#1572047142
def do_part_2():
    fill_line(input_data[-1], input_data[0])
    for i in range(0, len(input_data)-1):
        fill_line(input_data[i], input_data[i+1])
    flood_fill_outside_corners()

    biggest_area = 0
    biggest_i = 0
    biggest_j = 0

    N = len(input_data)
    for a in range(N):
        x1, y1 = input_data[a]
        for b in range(a + 1, N):
            x2, y2 = input_data[b]
            w = abs(x2 - x1)
            h = abs(y2 - y1)
            area = (w + 1) * (h + 1)
            if area <= biggest_area:
                continue
            if rect_is_allowed(x1, y1, x2, y2):
                biggest_area = area
                biggest_i = a
                biggest_j = b

    x1, y1 = input_data_original[biggest_i]
    x2, y2 = input_data_original[biggest_j]
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    area = (w + 1) * (h + 1)

    return area

if __name__ == '__main__':
    read_input_data()
    #print(do_part_1())
    print(do_part_2())
