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
        is_valid = True

        if len(row) == 1:
            valid_lines += 1
        else:
            asc = row[0] < row[1]

            for i in range(1, len(row)):
                diff = row[i] - row[i - 1] if asc else row[i - 1] - row[i]
                if diff < 1 or diff > 3:
                    is_valid = False

            if is_valid:
                valid_lines += 1

    print('similarity: ' + str(valid_lines))
