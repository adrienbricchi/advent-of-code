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

    sum = 0
    for input in inputs:
        is_ordered = True
        for i in range(0, len(input)):
            current_value = input[i]

            for j in range(0, i):
                previous_value = input[j]
                if (current_value in orders) and (previous_value in orders[current_value]):
                    print(str(input) + " => bad match: " + str(current_value) + "|" + str(previous_value))
                    is_ordered = False
                    break
            if not is_ordered:
                break

        if is_ordered:
            middle_index = math.floor(len(input) / 2)
            middle = input[middle_index]
            sum += middle
            print(str(input) + " => sum+" + str(middle) + "=" + str(sum))

    print(">> " + str(sum))