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


def defragment(disk):
    first_dot_index = disk.index(".")
    last_number_index = len(disk) - 1
    if first_dot_index >=0 and last_number_index >= 0:
        last_number = disk[last_number_index]
        disk[first_dot_index] = last_number
        disk = disk[:-1]
    # print(disk)
    return disk


def checksum(disk):
    result = 0
    for i in range(0, len(disk)):
        value = int(disk[i])
        result += (value * i)
    return result


disk_map = parse_file()
print(disk_map)
content = convert_to_content(disk_map)
while "." in content:
    content = defragment(content)
print(content)
print("checksum: " + str(checksum(content)))
