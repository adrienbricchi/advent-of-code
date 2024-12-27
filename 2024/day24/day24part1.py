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

values = {}
evaluations = {}

with (open('input.txt', newline='') as file):
    for line in file.readlines():
        for (key, value) in re.findall("^(.*?): (\d)$", line):
            print("parse key: " + key + "(" + value + ") = " + str(int(value == "1")))
            values[key] = value == "1"
        for (left, operation, right, target) in re.findall("^(.*?) (AND|OR|XOR) (.*?) -> (.*?)$", line):
            evaluations[target] = [left, operation, right]

    for value in values:
        print(value + ": " + str(int(values[value])))
    print(str(evaluations))

    while len(evaluations) > 0:
        for todo in list(evaluations):

            left = evaluations[todo][0]
            operation = evaluations[todo][1]
            right = evaluations[todo][2]

            if left in values and right in values:
                if operation == "AND":
                    values[todo] = values[left] and values[right]
                elif operation == "OR":
                    values[todo] = values[left] or values[right]
                else:
                    values[todo] = values[left] != values[right]

                print("evaluate " + todo + ": " + left + "(" + str(int(values[left])) + ") " + operation + " " + right + "(" + str(int(values[right])) + ") = " + str(int(values[todo])))
                del evaluations[todo]

    print("")

    for value in values:
        print(value + ": " + str(int(values[value])))

    print("")

    for x in reversed(range(0, 46)):
        print("z" + ('%02d' % x) + ": " + str(int(values["z" + '%02d' % x])))

    print("")

    for x in reversed(range(0, 46)):
        print(int(values["z" + '%02d' % x]), end='')
