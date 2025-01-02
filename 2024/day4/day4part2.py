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


def inline_row(matrix):
    result = []
    for line in matrix:
        print_line = "".join(line)
        result.append(print_line)
    return result


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
    for i in range(1, len(matrix[0]) - 1):
        for j in range(1, len(matrix) - 1):
            if matrix[i][j] == "A":
                diag_1 = "" + matrix[i - 1][j - 1] + matrix[i + 1][j + 1]
                diag_2 = "" + matrix[i + 1][j - 1] + matrix[i - 1][j + 1]
                if ''.join(sorted(diag_1)) == "MS" and ''.join(sorted(diag_2)) == "MS":
                    result += 1

    print(">> " + str(result))
