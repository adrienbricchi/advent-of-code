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
    if i < len(map):
        if j < len(map[i]):
            if map[i][j] == ".":
                map[i][j] = "#"


def find_antinodes(antenna_coords):
    results = []
    for i in range(0, len(antenna_coords)):
        current_antenna = antenna_coords[i]
        for j in range(i + 1, len(antenna_coords)):
            next_antenna = antenna_coords[j]
            diff_i = next_antenna[0] - current_antenna[0]
            diff_j = next_antenna[1] - current_antenna[1]
            back_antinode = (current_antenna[0] - diff_i, current_antenna[1] - diff_j)
            forward_antinode = (next_antenna[0] + diff_i, next_antenna[1] + diff_j)
            if back_antinode not in results:
                results.append(back_antinode)
            if forward_antinode not in results:
                results.append(forward_antinode)
    return results


map = parse_matrix('input.txt')
print_matrix(map)

antennas = find_chars_coordinates(map)
antinodes = []
for antenna in antennas:
    antenna_coords = find_char_coordinates(map, antenna)
    print(antenna + ": " + str(antenna_coords))
    pending_antinodes = find_antinodes(antenna_coords)
    print("   #: " + str(antinodes))
    for pending_antinode in pending_antinodes:
        if pending_antinode not in antinodes:
            if 0 <= pending_antinode[0] < len(map):
                if 0 <= pending_antinode[1] < len(map[0]):
                    antinodes.append(pending_antinode)

for antinode in antinodes:
    write_antinode(map, antinode)
print_matrix(map)

print("#: " + str(len(antinodes)))
