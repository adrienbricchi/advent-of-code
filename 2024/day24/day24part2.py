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


def get_wires_before(z_key, wires):
    result = []
    sub_wires_to_get = [z_key]

    while len(sub_wires_to_get) > 0:
        for sub_wire in list(sub_wires_to_get):
            if sub_wire in wires:

                left = wires[sub_wire][0]
                right = wires[sub_wire][2]

                if not re.match("[xyz]\d{2}", left):
                    result.append(left)
                if not re.match("[xyz]\d{2}", left):
                    result.append(right)
                if not re.match("[xyz]\d{2}", left):
                    sub_wires_to_get.append(left)
                if not re.match("[xyz]\d{2}", right):
                    sub_wires_to_get.append(right)

            sub_wires_to_get.remove(sub_wire)

    return sorted(set(result))


def get_wires_for(z_key, wires):
    if z_key <= 0: return []
    z_minus_one = get_wires_before("z" + ('%02d' % (z_key - 1)), wires)
    return [x for x in get_wires_before("z" + ('%02d' % z_key), wires) if x not in z_minus_one]


def binary_sum(values, evaluations):
    proper_map = {}
    for i in range(0, 45):
        proper_map["x" + '%02d' % i] = ("x" + '%02d' % i)
        proper_map["y" + '%02d' % i] = ("y" + '%02d' % i)
        proper_map["z" + '%02d' % i] = ("z" + '%02d' % i)

    while len(evaluations) > 0:
        evaluation_done = False
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

                # print("evaluate " + todo + ": " + left + "(" + str(int(values[left])) + ") " + operation + " " + right + "(" + str(int(values[right])) + ") = " + str(int(values[todo])))

                evaluation_done = True
                del evaluations[todo]

        if not evaluation_done:
            return "??????????????????????????????????????????????"

    result = ""
    for z in reversed(range(0, 46)):
        result += str(int(values["z" + '%02d' % z]))

    return result


def assert_result_at_index(expected, test, index):
    result = True
    for i in range(0, index):
        result = result and (expected[::-1][i] == test[::-1][i])
    return result


def test_at_index(index, example_input, wires):
    result = True
    expected_00 = "0000000000000000000000000000000000000000000000"
    expected_11 = "1111111111111111111111111111111111111111111110"
    expected_01 = "0111111111111111111111111111111111111111111111"
    expected_ex = "1100111010011101110101100100000010111101011000"

    inputs = {"x44": 0, "y44": 0}
    for x in reversed(range(0, 44)): inputs["x" + '%02d' % x] = 0
    for y in reversed(range(0, 44)): inputs["y" + '%02d' % y] = 0
    result_00 = binary_sum(inputs, dict(wires))
    result = result and assert_result_at_index(expected_00, result_00, index)

    inputs = {"x44": 0, "y44": 0}
    for x in reversed(range(0, 44)): inputs["x" + '%02d' % x] = 0
    for y in reversed(range(0, 44)): inputs["y" + '%02d' % y] = 1
    result_01 = binary_sum(inputs, dict(wires))
    result = result and assert_result_at_index(expected_01, result_01, index)

    inputs = {"x44": 0, "y44": 0}
    for x in reversed(range(0, 44)): inputs["x" + '%02d' % x] = 1
    for y in reversed(range(0, 44)): inputs["y" + '%02d' % y] = 0
    result_10 = binary_sum(inputs, dict(wires))
    result = result and assert_result_at_index(expected_01, result_10, index)

    inputs = {"x44": 0, "y44": 0}
    for x in reversed(range(0, 44)): inputs["x" + '%02d' % x] = 1
    for y in reversed(range(0, 44)): inputs["y" + '%02d' % y] = 1
    result_11 = binary_sum(inputs, dict(wires))
    result = result and assert_result_at_index(expected_11, result_11, index)

    # print("? " + result_00)
    # print("> " + expected_00)
    # print("? " + result_01)
    # print("> " + expected_01)
    # print("? " + result_10)
    # print("> " + expected_01)
    # print("? " + result_11)
    # print("> " + expected_11)

    result = result and assert_result_at_index(expected_ex, binary_sum(example_input, dict(wires)), index)

    return result


with (open('input.txt', newline='') as file):
    inputs = {}
    input_wires = {}
    for line in file.readlines():
        for (key, value) in re.findall("^(.*?): (\d)$", line):
            inputs[key] = (value == "1")
        for (left, operation, right, target) in re.findall("^(.*?) (AND|OR|XOR) (.*?) -> (.*?)$", line):
            input_wires[target] = [left, operation, right]

    wires = dict(input_wires)
    for (left, right) in [["nbc", "svm"], ["kqk", "z15"], ["cgq", "z23"], ["fnr", "z39"]]:
        wires[left] = input_wires[right]
        wires[right] = input_wires[left]

    potential_bad_wires = []
    i = 0
    while test_at_index(i, inputs, wires):
        print("testing index: " + str(i))
        i = i + 1

    potential_bad_wires = get_wires_for(i, wires)

    print("potential_bad_wires index:" + str(i) + " " + str(potential_bad_wires))

    for wire1 in potential_bad_wires:
        for wire2 in wires:
            if wire1 < wire2:
                permuted_wires = dict(wires)
                permuted_wires[wire1] = wires[wire2]
                permuted_wires[wire2] = wires[wire1]
                if test_at_index(i, inputs, permuted_wires):
                    sub_index = i
                    while test_at_index(sub_index, inputs, permuted_wires): sub_index += 1
                    print("successful permutation: " + wire1 + "/" + wire2 + ", valid all the way through => " + str(sub_index))
