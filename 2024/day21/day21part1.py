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


def parse_file():
    with (open('input.txt', newline='') as file):
        content = file.read()
        return content.split("\n")


numeric_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

directional_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]


#    +---+---+---+
#    | 7 | 8 | 9 |
#    +---+---+---+        +---+---+
#    | 4 | 5 | 6 |        | ^ | A |
#    +---+---+---+    +---+---+---+
#    | 1 | 2 | 3 |    | < | v | > |
#    +---+---+---+    +---+---+---+
#        | 0 | A |
#        +---+---+


def get_x(key, keypad):
    for line in keypad:
        for i in range(0, len(keypad[0])):
            if key == line[i]:
                return i
    return -1


def get_y(key, keypad):
    for i in range(0, len(keypad)):
        if key in keypad[i]:
            return i
    return -1


def compute_path(origin, target, keypad):
    origin_coordinates = (get_x(origin, keypad), get_y(origin, keypad))
    target_coordinates = (get_x(target, keypad), get_y(target, keypad))
    result = ""
    while not origin_coordinates == target_coordinates:
        if origin_coordinates[0] < target_coordinates[0]:
            upcoming_coordinates = (origin_coordinates[0] + 1, origin_coordinates[1])
            if keypad[upcoming_coordinates[1]][upcoming_coordinates[0]] is not None:
                result += ">"
                origin_coordinates = upcoming_coordinates
        if origin_coordinates[0] > target_coordinates[0]:
            upcoming_coordinates = (origin_coordinates[0] - 1, origin_coordinates[1])
            if keypad[upcoming_coordinates[1]][upcoming_coordinates[0]] is not None:
                result += "<"
                origin_coordinates = upcoming_coordinates
        if origin_coordinates[1] > target_coordinates[1]:
            upcoming_coordinates = (origin_coordinates[0], origin_coordinates[1] - 1)
            if keypad[upcoming_coordinates[1]][upcoming_coordinates[0]] is not None:
                result += "^"
                origin_coordinates = upcoming_coordinates
        if origin_coordinates[1] < target_coordinates[1]:
            upcoming_coordinates = (origin_coordinates[0], origin_coordinates[1] + 1)
            if keypad[upcoming_coordinates[1]][upcoming_coordinates[0]] is not None:
                result += "v"
                origin_coordinates = upcoming_coordinates

    return result


def compute_optimized_path(entry, keypad):
    previous_char = "A"
    path = ""
    for char in entry:
        sub_path = compute_path(previous_char, char, keypad)
        # TODO: Optimize the arrow order along the current position, to shorten the next step
        optimized_sub_path = ""
        if keypad is numeric_keypad:
            optimized_sub_path += "".join([x for x in sub_path if x == "^"])
            optimized_sub_path += "".join([x for x in sub_path if x == ">"])
            optimized_sub_path += "".join([x for x in sub_path if x == "v"])
            optimized_sub_path += "".join([x for x in sub_path if x == "<"])
        if keypad is directional_keypad:
            optimized_sub_path += "".join([x for x in sub_path if x == ">"])
            optimized_sub_path += "".join([x for x in sub_path if x == "v"])
            optimized_sub_path += "".join([x for x in sub_path if x == "^"])
            optimized_sub_path += "".join([x for x in sub_path if x == "<"])
        path += optimized_sub_path
        path += "A"
        previous_char = char
    return path


if __name__ == "__main__":

    codes = parse_file()

    results = {
        "029A": "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
        "980A": "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
        "179A": "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
        "456A": "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
        "379A": "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    }

    complexity_sum = 0
    for initial_code in codes:
        numeric_part_of_code = "".join([x for x in initial_code if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]])
        code = initial_code
        result = results[initial_code]
        for keypad in [numeric_keypad, directional_keypad, directional_keypad]:
            code = compute_optimized_path(code, keypad)
        complexity = len(code) * int(numeric_part_of_code)
        complexity_sum += complexity
        result_complexity = len(result) * int(numeric_part_of_code)
        print(initial_code + ": " + code + " length:" + str(len(code)) + " numeric:" + numeric_part_of_code + " complexity:" + str(complexity))
        print("      " + result + " length:" + str(len(result)) + " numeric:" + numeric_part_of_code + " complexity:" + str(result_complexity))
    print("sum: " + str(complexity_sum))
    print("     " + str(126384))
