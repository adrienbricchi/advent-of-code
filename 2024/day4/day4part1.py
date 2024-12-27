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

import re

def parse_matrix_file(file):
    matrix = []
    for line in file.readlines():
        matrix_line = []
        for char in line:
            if char != '\n':
                matrix_line += char
        matrix.append(matrix_line)
    return matrix


def print_matrix(matrix):
    for line in matrix:
        print(str(line))


def inline_row(matrix):
    result = []
    for line in matrix:
        print_line = ""
        for char in line:
            print_line += char
        result.append(print_line)
    return result


def rotate_90(matrix):
    rotated_matrix = []
    for j in range(0, len(matrix[0])):
        rotated_matrix.append([])
        for i in reversed(range(0, len(matrix))):
            rotated_matrix[j] += matrix[i][j]
    return rotated_matrix


def rotate_45(matrix):
    # Counter Variable
    result = []
    size = len(matrix)
    ctr = 0
    while ctr < 2 * size - 1:
        lst = []
        for i in range(size):
            for j in range(size):
                if i + j == ctr:
                    lst.append(matrix[i][j])
        lst.reverse()
        result.append(lst)
        ctr += 1
    return result


def count_xmas(matrix):
    result = 0
    for line in inline_row(matrix):
        result += len(re.findall("XMAS", line))
    return result


with (open('input.txt', newline='') as file):

    matrix = parse_matrix_file(file)
    result = 0

    for rotation in range(0, 4):
        result += count_xmas(matrix)
        matrix_angled = rotate_45(matrix)
        result += count_xmas(matrix_angled)
        matrix = rotate_90(matrix)

    print(str(result))