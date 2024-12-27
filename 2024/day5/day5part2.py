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
import math


def bubble_sort(list, orders):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (list[j] in orders) and (list[j + 1] in orders[list[j]]):
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def sum_centers(list):
    sum = 0
    for line in list:
        middle_index = math.floor(len(line) / 2)
        middle = line[middle_index]
        sum += middle
    return sum


orders = {}
inputs = []

with (open('input.txt', newline='') as file):
    for line in file.readlines():
        for (left, right) in re.findall("^(\d+)\|(\d+)$", line):
            left = int(left)
            right = int(right)
            if left not in orders: orders[left] = []
            orders[left].append(right)
        for parsed_line in re.findall("^(\d+(?:,\d+)*)$", line):
            line_input = parsed_line.split(",")
            inputs.append([int(x) for x in line_input])

    unordered_lines = []
    for input in inputs:
        is_ordered = True
        for i in range(0, len(input)):
            current_value = input[i]

            for j in range(0, i):
                previous_value = input[j]
                if (current_value in orders) and (previous_value in orders[current_value]):
                    is_ordered = False
                    break
            if not is_ordered:
                unordered_lines.append(input)
                break

    for line in unordered_lines:
        print("> " + str(line))
        print("= " + str(bubble_sort(line, orders)))

    print("sum: " + str(sum_centers(unordered_lines)))
