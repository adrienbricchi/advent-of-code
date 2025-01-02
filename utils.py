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


def rotate_90(matrix):
    """
    Rotates a matrix, 90 degrees clockwise
    :param matrix:
    :return:
    """
    rotated_matrix = []
    for j in range(0, len(matrix[0])):
        rotated_matrix.append([])
        for i in reversed(range(0, len(matrix))):
            rotated_matrix[j] += matrix[i][j]
    return rotated_matrix


def print_matrix(matrix):
    """
    Pretty print an array of arrays
    :param matrix:
    :return:
    """
    for line in matrix:
        print("".join([str(x) for x in line]))
