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

import math

from tqdm import tqdm


def parse_file():
    results = []
    with (open('input.txt', newline='') as file):
        content = file.read()
        for line in content.split("\n"):
            results.append(int(line))
    return results


def mix(secret, number):
    return secret ^ number


def prune(number):
    return number % 16777216


def sequence(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, math.floor(secret / 32)))
    return prune(mix(secret, secret * 2048))


if __name__ == "__main__":

    initial_secrets = parse_file()
    print("initial secrets (" + str(len(initial_secrets)) + "): " + str(initial_secrets))

    sum = 0
    for initial_secret in tqdm(initial_secrets):
        for i in range (0, 2000):
            initial_secret = sequence(initial_secret)
        sum += initial_secret

    print("sum: " + str(sum))
