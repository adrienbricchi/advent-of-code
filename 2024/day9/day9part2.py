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
        return file.readlines()[0].replace("\n", "")


def convert_to_content(disk_map):
    result = []
    for i in range(0, len(disk_map)):
        block_size = int(disk_map[i])
        for j in range(0, block_size):
            result.append(int(i / 2) if (i % 2) == 0 else ".")
    return result


def get_subsequence_index(content, subsequence, limit):
    result = -1
    for i in range(0, limit - len(subsequence) + 1):
        pending_result = True
        for j in range(0, len(subsequence)):
            pending_result = pending_result and content[i + j] == subsequence[j]
            if not pending_result:
                break
        if pending_result:
            result = i
            break
    return result


def trim_trailing_dots(disk):
    index = len(disk) - 1
    while disk[index] == ".":
        del disk[index]
        index -= 1


def defragment(disk):
    block_values = []
    for block_value in disk:
        if block_value != "." and block_value not in block_values:
            block_values.append(block_value)
    block_values.reverse()
    for block_value in block_values:
        block_size = len([x for x in disk if x == block_value])
        blank_model = ["."] * block_size
        first_block_index = disk.index(block_value)
        first_blank_index = get_subsequence_index(disk, blank_model, first_block_index)
        if first_blank_index != -1:
            if first_blank_index < first_block_index:
                for i in range(0, len(disk)):
                    if disk[i] == block_value:
                        disk[i] = "."
                for i in range(first_blank_index, first_blank_index + block_size):
                    disk[i] = block_value
                # print(str(disk))
                trim_trailing_dots(disk)
    return disk


def checksum(disk):
    result = 0
    for i in range(0, len(disk)):
        if disk[i] != ".":
            value = int(disk[i])
            result += (value * i)
    return result


disk_map = parse_file()
print(disk_map)
content = convert_to_content(disk_map)
content = defragment(content)
print(content)
print("checksum: " + str(checksum(content)))
print("checksum: 6511178035564")
