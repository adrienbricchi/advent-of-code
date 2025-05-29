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


def find_chars_coordinates(map):
    results = []
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            current_char = map[i][j]
            if current_char != '.':
                if current_char not in results:
                    results.append(current_char)
    return results


def find_char_coordinates(map, char):
    results = []
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == char:
                results.append((i, j))
    return results


def write_antinode(map, coord):
    i = coord[0]
    j = coord[1]
    if is_in_map_range(map, coord):
        if map[i][j] == ".":
            map[i][j] = "#"


def is_in_map_range(map, coord):
    i = coord[0]
    j = coord[1]
    return 0 <= i < len(map) and 0 <= j < len(map[i])


def find_antinodes(map, antenna_coords):
    results = []
    for i in range(0, len(antenna_coords)):
        current_antenna = antenna_coords[i]
        for j in range(i + 1, len(antenna_coords)):
            next_antenna = antenna_coords[j]
            diff_i = next_antenna[0] - current_antenna[0]
            diff_j = next_antenna[1] - current_antenna[1]
            back_antinode = (current_antenna[0] - diff_i, current_antenna[1] - diff_j)
            while is_in_map_range(map, back_antinode):
                results.append(back_antinode)
                back_antinode = (back_antinode[0] - diff_i, back_antinode[1] - diff_j)
            forward_antinode = (next_antenna[0] + diff_i, next_antenna[1] + diff_j)
            while is_in_map_range(map, forward_antinode):
                results.append(forward_antinode)
                forward_antinode = (forward_antinode[0] + diff_i, forward_antinode[1] + diff_j)
    return results


map = parse_matrix('input.txt')
print_matrix(map)

antennas = find_chars_coordinates(map)
antinodes = []
for antenna in antennas:
    antenna_coords = find_char_coordinates(map, antenna)
    print(antenna + ": " + str(antenna_coords))
    pending_antinodes = find_antinodes(map, antenna_coords)
    print("   #: " + str(pending_antinodes))
    # temp_map = parse_matrix('input.txt')
    # for antinode in pending_antinodes:
    #     write_antinode(temp_map, antinode)
    # print_matrix(temp_map)
    for pending_antinode in pending_antinodes:
        antinodes.append(pending_antinode)

for antinode in antinodes:
    write_antinode(map, antinode)
print_matrix(map)

total = 0
for line in map:
    for dot in line:
        total += 1 if dot != "." else 0

print("#: " + str(total))
