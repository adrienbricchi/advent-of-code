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

mul_regex = r'mul\((?<left>\d{1,3}),(?<right>\d{1,3})\)'
result = 0

with (open('input.txt', newline='') as file):
    content = file.read()
    filtered_content = content

    for (filter_out) in re.findall("don't\(\)(.*?)(?:do\(\)|$)", filtered_content):
        print("filter out: " + filter_out)
        filtered_content = filtered_content.replace(filter_out, "")
        print(" size? " + str(len(filtered_content)))

    print(filtered_content)
    for (left, right) in re.findall("mul\((\d{1,3}),(\d{1,3})\)", filtered_content):
        result += int(left) * int(right)

print(" result: " + str(result))