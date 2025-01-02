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

from utils import rotate_90

keys = []
locks = []


def read_file():
    with (open('input.txt', newline='') as file):
        file_content = file.read()
        for file_chunk in file_content.split("\n\n"):
            chunk = []
            for line in file_chunk.split("\n"):
                chunk.append(list(line))
            is_lock = chunk[0].count("#") == 5
            chunk.remove(["#", "#", "#", "#", "#"])
            chunk = rotate_90(chunk)
            chunk = [line.count("#") for line in chunk]
            if is_lock:
                locks.append(chunk)
            else:
                keys.append(chunk)


def overlap(lock, key):
    for i in range(0, len(lock)):
        if (key[i] + lock[i]) > 5:
            return True
    return False


if __name__ == '__main__':

    read_file()
    print("locks (" + str(len(locks)) + "): " + str(locks))
    print("keys (" + str(len(keys)) + "): " + str(keys))

    no_overlaps = 0
    for lock in locks:
        for key in keys:
            if not overlap(lock, key):
                no_overlaps += 1

    print("no_overlaps: " + str(no_overlaps))
