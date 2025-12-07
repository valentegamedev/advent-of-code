input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        input_data.append(i.strip().replace('\r', '').replace('\n', ''))

def do_part_1():
    beams = []
    start_index = input_data[0].index("S")
    print(start_index)

    beams.append((1, start_index)) #(row, column)

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


def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    print(do_part_1())
    #do_part_2()