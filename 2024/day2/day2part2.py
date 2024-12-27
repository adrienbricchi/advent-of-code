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

import csv

with (open('input.csv', newline='') as csvfile):
    spam_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    valid_lines = 0

    for row in spam_reader:
        row = [int(x) for x in row]

        if len(row) == 1:
            valid_lines += 1
        else:
            is_valid = False
            for i in range(0, len(row)):
                filtered_row = [x for x in row]
                filtered_row.pop(i)
                asc = filtered_row[0] < filtered_row[1]

                is_filter_valid = True
                for j in range(1, len(filtered_row)):
                    diff = filtered_row[j] - filtered_row[j - 1] if asc else filtered_row[j - 1] - filtered_row[j]
                    if diff < 1 or diff > 3:
                        is_filter_valid = False

                is_valid = is_valid or is_filter_valid

            if is_valid:
                valid_lines += 1

    print('valid_lines: ' + str(valid_lines))
