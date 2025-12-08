from functools import cache

input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        input_data.append(i.strip().replace('\r', '').replace('\n', ''))

#1573
def do_part_1(start):
    beams = []

    beams.append(start) #(row, column)

    splits = 0
    beams_trail = set()

    while len(beams) > 0:
        beam = beams.pop(0)
        new_beam = (beam[0]+1, beam[1])

        if new_beam[0] >= len(input_data):
            break
        value = input_data[new_beam[0]][new_beam[1]]
        if value == "^":
            splits+=1
            left_index = new_beam[1]-1
            right_index = new_beam[1]+1
            if left_index >= 0 and new_beam not in beams_trail:
                beams.append((new_beam[0], new_beam[1]-1))
            if right_index < len(input_data) and new_beam not in beams_trail:
                beams.append((new_beam[0], new_beam[1]+1))
        elif new_beam not in beams_trail:
            beams.append(new_beam)

        beams_trail.add(new_beam)

    return splits

def in_bounds(pos):
    return 0 <= pos[0] < len(input_data) and 0 <= pos[1] < len(input_data[0])

#15093663987272
@cache
def do_part_2(start):
    row, column = start

    while in_bounds((row, column)) and input_data[row][column] != '^':
        row += 1

    if not in_bounds((row, column)):
        return 1

    left = (row, column - 1)
    right = (row, column + 1)
    return do_part_2(left) + do_part_2(right)

if __name__ == '__main__':
    read_input_data()
    start_index = input_data[0].index("S")
    start = (1, start_index)

    #print(do_part_1(start))
    print(do_part_2(start))