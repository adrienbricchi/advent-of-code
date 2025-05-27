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


def parse_file():
    result = []
    with (open('input.txt', newline='') as file):
        for line in file.readlines():
            for (computing_result, computing_values) in re.findall("^(\d+):((?:\s\d+)*)$", line):
                key = int(computing_result)
                values = computing_values.split(" ")
                values = [int(x) for x in values if x != ""]
                result.append((key, values))
    return result


def compute(table):
    match_sum = 0
    for entry in table:
        key = entry[0]
        values = entry[1]
        possible_results = [values[0]]
        for i in range(1, len(values)):
            value = values[i]
            temp_possible_results = []
            # print("    " + str(possible_results) + " +*|| " + str(value))
            for possible_result in possible_results:
                temp_possible_results.append(possible_result + value)
                temp_possible_results.append(possible_result * value)
                temp_possible_results.append(int(str(possible_result) + str(value)))
            possible_results = temp_possible_results
        if key in possible_results:
            print(">> " + str(key) + ": " + str(values) + " found!")
            match_sum += key
        else:
            print(">> " + str(key) + ": " + str(values))
    return match_sum


calculations = parse_file()
print("sum : " + str(compute(calculations)))
