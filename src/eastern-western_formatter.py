#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This scritp adds spaces to eastern(Chinese, Japanese, Korean [^1])-western(Latin, Cyrillic, Greek), according to the [guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines).
# [1]: https://en.wikipedia.org/wiki/List_of_Unicode_characters#East_Asian_writing_systems

import functools
import sys

Space = (32)
Numerals = (48, 57)
Western = {
    'LatinUpper': (65, 90),
    'LatinLower': (97, 122),
    'LatinSupp': (192, 255)
}  # except 215, 247

NoSpaces = [i for i in '，。；「」：《》『』、[]（）*_']

# Latin Extended-A & -B, Esperanto ŭ et al in this blocks


def is_western(char: str) -> bool:
    '''
    Determine if char belongs to the western codes.
    '''
    codes = []
    for code_ranges in Western.values():
        for code in range(code_ranges[0], code_ranges[1]):
            codes.append(code)
    return ord(char) in codes
# test_western = ['a', 'ŭ', 'g', ',', 'β']
# for i in lis:
#    print(is_western(i))


def is_not_fullwidth(char: str) -> bool:
    '''
    Determine if char belongs to the fullwidth codes.
    '''
    return not char.isspace() and not (char in NoSpaces)

def apply_spaces(pre, ego):
    '''
    '''
    if len(pre) == 0:
        return ego

    if is_western(pre[-1]) != is_western(ego) and \
            is_not_fullwidth(ego) and is_not_fullwidth(pre[-1]):
        return ' '.join([pre, ego])
    else:
        return ''.join([pre, ego])

# TODO: auto-spacing between quantities and their units, e.g. `20TB` -> `20 TB`.

if __name__ == '__main__':
    # check for valid argument
    if len(sys.argv) < 2:
        print('At least one argument is required!')
        exit()
    
    # read from the given file
    with open(sys.argv[1], 'r') as f:
        input_str = f.read()
    
    # TODO: take options of new file
    # write the result
    output_str = functools.reduce(apply_spaces, input_str, '')
    with open(sys.argv[2 if len(sys.argv) > 2 else 1], 'w') as f:
        f.write(output_str)
