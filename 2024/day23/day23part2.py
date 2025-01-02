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
from copy import copy

from tqdm import tqdm

links = {}


def open_file():
    with (open('input.txt', newline='') as file):
        content = file.read()
        for line in content.split("\n"):
            link = line.split("-")
            if not link[0] in links: links[link[0]] = []
            links[link[0]].append(link[1])
            if not link[1] in links: links[link[1]] = []
            links[link[1]].append(link[0])


if __name__ == "__main__":
    open_file()
    print("links (" + str(len(links)) + "): " + str(links))

    tuples = []
    for key1 in tqdm(links):
        for key2 in links[key1]:
            for key3 in links[key1]:
                if key3 in links[key2]:
                    element = sorted((key1, key2, key3))
                    if element not in tuples: tuples.append(element)

    print("triples: " + str(len(tuples)))

    i = 4
    while True:
        pending_tuples = []
        for existing_tuple in tqdm(tuples):
            for new_key in links:
                if new_key not in existing_tuple:
                    is_subset = True
                    for existing_key in existing_tuple:
                        if not new_key in links[existing_key]:
                            is_subset = False
                            break
                    if is_subset:
                        copied_tuple = copy(existing_tuple)
                        copied_tuple.append(new_key)
                        copied_tuple.sort()
                        if copied_tuple not in pending_tuples:
                            pending_tuples.append(copied_tuple)

        print(str(i) + "-uples: " + str(len(pending_tuples)))

        if len(pending_tuples) > 0:
            tuples = pending_tuples
            i += 1
        else:
            break

    print(str(tuples[0]))
