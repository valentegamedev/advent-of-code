import numpy

reports = []
safe_reports = []

def generate_every_combination_list(input_list):
    result = []

    for i in range(len(input_list)):
        result.append([x for j, x in enumerate(input_list) if j != i])

    result.append(input_list)
    return result


def is_any_safe(input_list):
    lists = generate_every_combination_list(input_list)
    while len(lists) > 0:
        list = lists[0]
        lists.remove(list)

        list = [int(item) for item in list]
        report_range = range(len(list) - 1)
        is_safe = True
        sign_value = 0
        for i in report_range:
            difference = list[i] - list[i+1]
            if abs(difference) >= 4 or difference == 0:
                is_safe = False
                break

            if sign_value == 0:
                sign_value = numpy.sign(difference)

            if sign_value != numpy.sign(difference):
                is_safe = False
                break

        if is_safe:
            return True
    return False


def check_safety_part2():
    while len(reports) > 0:
        report = reports[0]
        reports.remove(report)

        has_any_safe = is_any_safe(report)
        if has_any_safe:
            safe_reports.append(report)

    print(safe_reports)
    print(len(safe_reports))

def check_safety_part1():
    while len(reports) > 0:
        report = reports[0]
        reports.remove(report)

        report = [int(item) for item in report]
        report_range = range(len(report) - 1)
        is_safe = True
        sign_value = 0
        for i in report_range:
            difference = report[i] - report[i+1]
            if abs(difference) >= 4 or difference == 0:
                is_safe = False
                break

            if sign_value == 0:
                sign_value = numpy.sign(difference)

            if sign_value != numpy.sign(difference):
                is_safe = False
                break

        if is_safe:
            safe_reports.append(report)

    print(safe_reports)
    print(len(safe_reports))


def fill_reports():
    f = open("input/day_02.txt", "r")
    for x in f:
        split = x.strip().split(" ")

        reports.append(split)

    print(reports)


if __name__ == '__main__':
    fill_reports()
    #check_safety_part1()
    check_safety_part2()

