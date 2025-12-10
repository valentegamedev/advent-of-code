import igraph as ig
import re
import sys
from itertools import product

machines = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        line_split = i.strip().replace('\r', '').replace('\n', '').split(' ')
        lights = line_split[0][1:-1]
        joltage = line_split[-1][1:-1].split(',')

        buttons = []
        buttons_list = line_split[1:-1]
        for button in buttons_list:
            button_string = button[1:-1]
            buttons.append(list(map(int, button_string.split(','))))

        machines.append((lights, buttons, joltage))

    for machine in machines:
        print(machine)


def emulate_presses(light_state, buttons):
    buttons_list = list(buttons)
    light_state_list = list(light_state)

    #print(buttons_list)
    #print(light_state_list)

    for i in buttons:
        light_state_list[i] = not light_state_list[i]
    return tuple(light_state_list)

def get_button_presses(machine):
    lights, buttons, _ = machine

    n = len(lights)

    start = tuple([False] * len(lights))
    target = tuple(c == '#' for c in lights)

    lights_states = list(product([False, True], repeat=n))
    lights_states_to_idx_dic = {s: i for i, s in enumerate(lights_states)}
    print(lights_states_to_idx_dic)

    g = ig.Graph(n=len(lights_states), directed=False)
    edges = []

    for light_state in lights_states:
        light_state_idx = lights_states_to_idx_dic[light_state]
        for button in buttons:
            new_light_state = emulate_presses(light_state, button)
            new_light_state_idx = lights_states_to_idx_dic[new_light_state]
            edges.append((light_state_idx, new_light_state_idx))

    g.add_edges(edges)

    start_id = lights_states_to_idx_dic[start]
    target_id = lights_states_to_idx_dic[target]

    presses = g.distances(start_id, target_id)[0][0]

    return presses


def do_part_1():
    sum = 0

    for machine in machines:
        sum+= get_button_presses(machine)

    return sum

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    print(do_part_1())
    #do_part_2()