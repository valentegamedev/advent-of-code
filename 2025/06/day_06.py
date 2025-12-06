import re

input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        i = re.sub(r'\s+', ' ', i)
        i = i.strip().replace('\r', '').replace('\n', '')
        input_data.append(i.split(' '))

#4951502530386
def do_part_1():
    columns = len(input_data[0])
    rows = len(input_data)

    total = 0

    for col in range(0, columns):
        operation = input_data[rows - 1][col]
        total_operation = int(input_data[0][col])
        for row in range(1, rows-1):
            value = int(input_data[row][col])
            if operation == '*':
                total_operation *= value
            elif operation == '+':
                total_operation += value
        total += total_operation

    return total

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    print(do_part_1())
    #do_part_2()