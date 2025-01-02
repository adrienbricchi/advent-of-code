#
# Advent of Code
# Copyright (C) 2024 Adrien BRICCHI
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import copy
from tqdm import tqdm
import multiprocessing


def find_player_position(given_map):
    for i in range(0, len(given_map[0])):
        for j in range(0, len(given_map)):
            if given_map[j][i] in ["^", "v", "<", ">"]:
                return j, i
    return None


def get_forward_position(given_map, position):
    player_char = given_map[position[0]][position[1]]
    if player_char == "^": return position[0] - 1, position[1]
    elif player_char == "v": return position[0] + 1, position[1]
    elif player_char == "<": return position[0], position[1] - 1
    else: return position[0], position[1] + 1


def is_in_map_boundaries(given_map, position):
    return (position[0] >= 0) and (position[0] < len(given_map)) and (position[1] >= 0) and (position[1] < len(given_map[0]))


def run(given_map):

    bump_from_top = []
    bump_from_left = []
    bump_from_right = []
    bump_from_bottom = []
    current_position = find_player_position(given_map)
    if not current_position:
        return None
    ahead_position = get_forward_position(given_map, current_position)

    while True:
        # print("")
        # print_map()
        if not is_in_map_boundaries(given_map, ahead_position):
            given_map[current_position[0]][current_position[1]] = "x"
            break
        elif not given_map[ahead_position[0]][ahead_position[1]] in ("#", "O"):
            given_map[ahead_position[0]][ahead_position[1]] = given_map[current_position[0]][current_position[1]]
            given_map[current_position[0]][current_position[1]] = "x"
            current_position = ahead_position
            ahead_position = get_forward_position(given_map, current_position)
        else:
            player_char = given_map[current_position[0]][current_position[1]]
            if player_char == "^":
                if ahead_position in bump_from_bottom: return False
                bump_from_bottom.append(ahead_position)
                given_map[current_position[0]][current_position[1]] = ">"
            elif player_char == "v":
                if ahead_position in bump_from_top: return False
                bump_from_top.append(ahead_position)
                given_map[current_position[0]][current_position[1]] = "<"
            elif player_char == "<":
                if ahead_position in bump_from_right: return False
                bump_from_right.append(ahead_position)
                given_map[current_position[0]][current_position[1]] = "^"
            else:
                if ahead_position in bump_from_left: return False
                bump_from_left.append(ahead_position)
                given_map[current_position[0]][current_position[1]] = "v"
            current_position = current_position
            ahead_position = get_forward_position(given_map, current_position)
        # time.sleep(0.5)

    # print("")
    # print_map()
    return True


def get_x_positions(given_map):
    result = []
    for i in range(0, len(given_map[0])):
        for j in range(0, len(given_map)):
            if given_map[j][i] == "x":
                result.append((j, i))
    return result


def check_loop(init_map, obstacle, result, result_lock):
    current_map = copy.deepcopy(init_map)
    current_map[obstacle[0]][obstacle[1]] = "O"
    if run(current_map) is False:
        with result_lock:
            result.value += 1


if __name__ == '__main__':
    initial_map = []
    with (open('input.txt', newline='') as file):

        for line in file.readlines():
            line_parsed = []
            for char in line:
                if char != "\n":
                    line_parsed.append(char)
            initial_map.append(line_parsed)

    game_map = copy.deepcopy(initial_map)
    has_ended = run(game_map)

    print("?? " + str(has_ended))
    print(">> x (" + str(len(get_x_positions(game_map))) + ") : " + str(get_x_positions(game_map)))

    print("Number of cpu: ", multiprocessing.cpu_count())
    procs = []

    with multiprocessing.Manager() as manager:

        possible_loops_atomic = manager.Value('i', 0)
        lock = manager.Lock()

        for possible_obstacle in tqdm(get_x_positions(game_map)):
            proc = multiprocessing.Process(target=check_loop, args=(initial_map, possible_obstacle, possible_loops_atomic, lock))
            procs.append(proc)
            proc.start()

        for proc in procs:
            proc.join()

        print("possible_loops: " + str(possible_loops_atomic.value))