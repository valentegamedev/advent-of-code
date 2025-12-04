list_left = []
list_right = []
distances = []
similarity_score = []

def find_similarity_part2():
    while len(list_left) > 0:
        value = list_left[0]
        list_left.remove(value)
        occurrences = list_right.count(value)
        similarity_score.append(int(value) * occurrences)

    print(sum(similarity_score))

def find_distances_part1():
    while len(list_left) > 0:
        smallest_left = min(list_left)
        list_left.remove(smallest_left)

        smallest_right = min(list_right)
        list_right.remove(smallest_right)
        distance = abs(int(smallest_left)-int(smallest_right))
        distances.append(distance)
        print(str(distance))

    print(sum(distances))

def fill_lists():
    f = open("input/day_01.txt", "r")
    for x in f:
        split = x.strip().split("   ")
        list_left.append(split[0])
        list_right.append(split[1])

if __name__ == '__main__':
    fill_lists()
    #find_distances_part1()
    find_similarity_part2()

