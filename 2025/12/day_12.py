pieces = []
containers = []

def read_input_data():
    f = open("input/data.txt", "r")
    piece = []
    for i in f:
        row = i.strip().replace('\r', '').replace('\n', '')
        if ':' in row and 'x' not in row:
            pass
        elif ':' in row and 'x' in row:
            row_split = row.split(':')
            multipliers = list(map(int,row_split[1][1:].split(' ')))
            size_split = row_split[0].split('x')
            size = (int(size_split[0]), int(size_split[1]))
            containers.append((size, multipliers))
        elif len(row) == 0:
            pieces.append(piece)
            piece = []
        else:
            piece.append(row)

def get_piece_area(piece):
    return len(piece) * len(piece[0])

def get_piece_pieces(piece):
    total = 0
    for row in piece:
        for col in row:
            if col == '#':
                total += 1
    return total

#1000 460
def do_part_1():
    pruned_containers = []

    for size, multipliers in containers:
        needed_size = 0
        for idx, multiplier in enumerate(multipliers):
            needed_size += multiplier * get_piece_pieces(pieces[idx])
        container_size = size[0] * size[1]
        if container_size >= needed_size:
            pruned_containers.append((size, multipliers))

    print(len(containers), len(pruned_containers))
    print(pieces)
    print(containers)

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    do_part_1()
    #do_part_2()