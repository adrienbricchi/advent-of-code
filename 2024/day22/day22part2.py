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


def is_valid_code(code, cache):
    if (code[0] + code[1] + code[2] + code[3]) > 9: return False
    if (code[0] + code[1] + code[2]) > 9: return False
    if (code[1] + code[2] + code[3]) > 9: return False
    if (code[0] + code[1]) > 9: return False
    if (code[1] + code[2]) > 9: return False
    if (code[2] + code[3]) > 9: return False
    if (code[0] + code[1] + code[2] + code[3]) <= -9: return False
    if (code[0] + code[1] + code[2]) < -9: return False
    if (code[1] + code[2] + code[3]) <= -9: return False
    if (code[0] + code[1]) < -9: return False
    if (code[1] + code[2]) < -9: return False
    if (code[2] + code[3]) <= -9: return False
    if code[3] == -9: return False
    for cache_key in cache:
        if code in cache[cache_key]:
            return True
    return False


def get_sum(code, initial_secrets, cache):
    sum = 0
    for initial_secret in initial_secrets:
        if code in cache[initial_secret]:
            sum += cache[initial_secret][code]

    return sum


if __name__ == "__main__":

    initial_secrets = parse_file()
    print("initial secrets (" + str(len(initial_secrets)) + "): " + str(initial_secrets))

    cache = {}
    for initial_secret in tqdm(initial_secrets):

        secret = initial_secret
        current_cache = {}
        previous_4 = (99, 99, 99, 99)
        previous_result = initial_secret % 10

        for i in range(0, 2000):

            secret = sequence(secret)
            new_result = secret % 10
            previous_4 = (previous_4[1], previous_4[2], previous_4[3], new_result - previous_result)
            previous_result = new_result

            if not previous_4 in current_cache:
                current_cache[previous_4] = new_result

        cache[initial_secret] = current_cache

    possible_codes = []
    max = 0
    for a in tqdm(range(-9, 10)):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-8, 10):
                    code = (a, b, c, d)
                    if is_valid_code(code, cache):
                        possible_codes.append(code)

    max_sum = 0

    for code in tqdm(possible_codes):
        current_sum = get_sum(code, initial_secrets, cache)

        if current_sum > max_sum:
            max_sum = current_sum
            print(str(code) + ": " + str(current_sum))
