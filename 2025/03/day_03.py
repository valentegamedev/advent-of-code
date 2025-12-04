input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        input_data.append(i)

def get_largest_jolt(bank):
    largest_jolt = 0
    for i in range(0, len(bank)-1):
        left = bank[i]
        for j in range(i+1, len(bank)):
            right = bank[j]
            jolt = int(left + right)
            if jolt > largest_jolt:
                largest_jolt = jolt
    #print(largest_jolt)
    return largest_jolt

#17109
def do_part_1():
    jolt_sum = 0
    for bank in input_data:
        jolt = get_largest_jolt(bank)
        jolt_sum += jolt
    print(jolt_sum)

#169347417057382
def get_largest_jolt_part_2(bank, size):
    bank_length = len(bank)
    extra_numbers_count = bank_length - size

    biggest_jolt = []

    for c in bank:
        while extra_numbers_count > 0 and len(biggest_jolt) > 0 and biggest_jolt[len(biggest_jolt) - 1] < c:
            biggest_jolt.pop(len(biggest_jolt) - 1)
            extra_numbers_count -= 1
        biggest_jolt.append(c)

    if len(biggest_jolt) > size:
        biggest_jolt = biggest_jolt[:size]

    return int(''.join(biggest_jolt))


def do_part_2():
    jolt_sum = 0
    for bank in input_data:
        jolt = get_largest_jolt_part_2(bank.replace('\r', '').replace('\n', ''), 12)
        #print(jolt)
        jolt_sum += jolt
    print(jolt_sum)

if __name__ == '__main__':
    read_input_data()
    #do_part_1()
    do_part_2()