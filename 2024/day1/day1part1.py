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
    left_row = []
    right_row = []
    for row in spam_reader:
        filtered_row = [i for i in row if i != '']
        left_row.append(filtered_row[0])
        right_row.append(filtered_row[1])
    left_row.sort()
    right_row.sort()
    print('left_row: ' + str(left_row))
    print('right_row: ' + str(right_row))
    similarity = 0
    for i in range(0, len(left_row)):
        right_array = [j for j in right_row if j == left_row[i]]
        right_count = len(right_array)
        row_similarity = int(left_row[i]) * right_count
        similarity += row_similarity
        print("similarity... " + left_row[i] + " = " + str(row_similarity))
    print('similarity: ' + str(similarity))