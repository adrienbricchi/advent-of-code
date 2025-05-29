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

from utils import print_matrix, parse_matrix


map = []


def find_player_position():
    for i in range(0, len(map[0])):
        for j in range(0, len(map)):
            if map[j][i] in ["^", "v", "<", ">"]:
                return j, i
    return None


def get_forward_position():
    position = find_player_position()
    char = map[position[0]][position[1]]
    if char == "^": return position[0] - 1, position[1]
    elif char == "v": return position[0] + 1, position[1]
    elif char == "<": return position[0], position[1] - 1
    else: return position[0], position[1] + 1


def is_in_map_boundaries(position):
    return (position[0] >= 0) and (position[0] < len(map)) and (position[1] >= 0) and (position[1] < len(map[0]))


def run():
    while True:
        print("")
        print_matrix(map)
        current_position = find_player_position()
        ahead_position = get_forward_position()
        if not is_in_map_boundaries(ahead_position):
            map[current_position[0]][current_position[1]] = "x"
            break
        elif map[ahead_position[0]][ahead_position[1]] != "#":
            map[ahead_position[0]][ahead_position[1]] = map[current_position[0]][current_position[1]]
            map[current_position[0]][current_position[1]] = "x"
        else:
            char = map[current_position[0]][current_position[1]]
            if char == "^": map[current_position[0]][current_position[1]] = ">"
            elif char == "v": map[current_position[0]][current_position[1]] = "<"
            elif char == "<": map[current_position[0]][current_position[1]] = "^"
            else: map[current_position[0]][current_position[1]] = "v"
        # time.sleep(0.5)

    print("")
    print_matrix(map)


def count_x():
    sum = 0
    for i in range(0, len(map[0])):
        for j in range(0, len(map)):
            if map[j][i] == "x":
                sum += 1
    return sum


map = parse_matrix('input.txt')
run()
print("")
print(">> x:" + str(count_x()))
