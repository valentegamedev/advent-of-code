input_data = []

value = 50

#1089
def turn_safe(rotation):
    global value
    direction = -1 if rotation[0] == "L" else 1
    number = int(rotation[1:])

    value += number * direction
    value = value % 100

    print("D:" + str(direction) + " N:" + str(number) + " V:" + str(value))

    if value == 0:
        return 1
    else:
        return 0

#6530
def turn_safe_part2(rotation):
    global value
    direction = -1 if rotation[0] == "L" else 1
    number = int(rotation[1:])

    hits_on_0 = number // 100

    if direction == -1:
        left_to_0 = value
    else:
        left_to_0 = (100 - value) % 100

    if left_to_0 != 0:
        remainder = number % 100
        if left_to_0 <= remainder:
            hits_on_0 += 1

    value = (value + number * direction) % 100

    return hits_on_0

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        input_data.append(i)

def do_part_1():
    global input_data
    total_0s = 0

    for data in input_data:
        total_0s+=turn_safe(data)
    print("Total 0s:" + str(total_0s))

def do_part_2():
    global input_data
    total_0s = 0

    for data in input_data:
        total_0s += turn_safe_part2(data)
    print("Total 0s:" + str(total_0s))

if __name__ == '__main__':
    read_input_data()
    #do_part_1()
    do_part_2()