import re

input_data = []

def read_input_data_day_1():
    f = open("input/data.txt", "r")
    for i in f:
        i = re.sub(r'\s+', ' ', i)
        i = i.strip().replace('\r', '').replace('\n', '')
        input_data.append(i.split(' '))

def read_input_data_day_2():
    f = open("input/data.txt", "r")
    temp_input_data = []
    for i in f:
        i = i.replace('\r', '').replace('\n', '')
        temp_input_data.append(i)

    maxlen = max(len(l) for l in temp_input_data)
    for l in temp_input_data:
        input_data.append(l.ljust(maxlen, ' '))

#4951502530386
def do_part_1():
    read_input_data_day_1()
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

def get_operations():
    starts_and_sizes = []
    rows = len(input_data)
    operations = input_data[rows - 1]
    current_operation = operations[0]
    current_operation_s = 0

    for idx, i in enumerate(operations[1:]):
        idx = idx + 1
        if i == '*' or i == '+':
            starts_and_sizes.append((current_operation, current_operation_s, idx - current_operation_s - 1))
            current_operation_s = idx
            current_operation = i
    starts_and_sizes.append((current_operation, current_operation_s, len(operations) - current_operation_s))
    return starts_and_sizes

def get_numbers_from_operation(operation):
    horizontal_numbers = []
    columns = operation[2]
    for row in input_data[:-1]:
        horizontal_numbers.append(row[operation[1]:operation[1]+columns])

    vertical_numbers = []
    rows = len(horizontal_numbers)
    for col in range(0, columns):
        number = ''
        for row in horizontal_numbers:
            number += row[col]
        vertical_numbers.append(int(number))

    return vertical_numbers

#8486156119946
def do_part_2():
    read_input_data_day_2()
    operations = get_operations()

    total = 0
    for operation in operations:
        #print(operation)
        numbers = get_numbers_from_operation(operation)
        #print(numbers)
        total_operation = numbers[0]
        for number in numbers[1:]:
            if operation[0] == '*':
                total_operation *= number
            elif operation[0] == '+':
                total_operation += number
        total += total_operation

    return total


if __name__ == '__main__':
    #print(do_part_1())
    print(do_part_2())