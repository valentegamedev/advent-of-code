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
        joltage = list(map(int, line_split[-1][1:-1].split(',')))

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

def parity_vec(target):
    return [t % 2 for t in target]

def find_parity_patterns_bool(buttons, parity_target):
    n = len(buttons)
    m = len(parity_target)
    patterns = []
    # enumerate all boolean combinations for n buttons
    for combo in product([False, True], repeat=n):
        res = [0] * m
        for j, pressed in enumerate(combo):
            if pressed:
                for idx in buttons[j]:
                    # toggle parity for that counter
                    res[idx] ^= 1
        if res == parity_target:
            patterns.append(combo)
    return patterns

# memoization keyed by tuple(target)
def min_presses_joltage(buttons, target, memo):
    # target: list of nonnegative ints
    key = tuple(target)
    if key in memo:
        return memo[key]
    # base

    if all(t == 0 for t in target):
        memo[key] = 0
        return 0

    p = parity_vec(target)

    parity_patterns = find_parity_patterns_bool(buttons, p)
    if not parity_patterns:
        memo[key] = float('inf')
        return float('inf')

    best = float('inf')
    n = len(buttons)

    for pattern in parity_patterns:
        mlen = len(target)
        contribution = [0] * mlen
        for j in range(n):
            if pattern[j] % 2 == 1:
                for idx in buttons[j]:
                    contribution[idx] += 1

        possible = True
        residual = [0] * mlen

        for i in range(mlen):
            rem = target[i] - contribution[i]
            if rem < 0 or (rem % 2) != 0:
                possible = False
                break
            residual[i] = rem // 2
        if not possible:
            continue

        sub = min_presses_joltage(buttons, residual, memo)
        if sub >= float('inf'):
            continue

        presses = sum(pattern) + 2 * sub
        if presses < best:
            best = presses

    memo[key] = best
    return best

def do_part_2():
    total = 0
    memo_global = {}
    for lights, buttons, joltage in machines:
        m = len(joltage)

        res = min_presses_joltage(buttons, joltage, memo_global)
        if res >= float('inf'):
            continue
        print(joltage, res)
        total += res
    return total

if __name__ == '__main__':
    read_input_data()
    #print(do_part_1())
    do_part_2()