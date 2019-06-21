#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
# This scritp adds spaces to eastern(Chinese, Japanese, Korean [^1])-western(Latin, Cyrillic, Greek), according to the [guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines).
# [1]: https://en.wikipedia.org/wiki/List_of_Unicode_characters#East_Asian_writing_systems

import functools
import sys

Space = (32)
Numerals = (48, 57)

Western_ranges = {
    'LatinUpper': (65, 90),
    'LatinLower': (97, 122),
    'LatinSupplement': (192, 255)
}
# Latin Extended-A & -B, Esperanto ŭ et al in this blocks
Western_codes = []
for i, j in Western_ranges.values():
    Western_codes += (list(range(i, j + 1)))
Western_codes = [i for i in Western_codes if i not in [215, 247]]  # which are maths symbols
Western_chars = [chr(code) for code in Western_codes]

NonSpacing = {
    'Fullwidth': [i for i in '，。；「」：《》『』、[]（）*_'],
    'MathsExpression': []
}


def is_western(char: str) -> bool:
    '''
    Determine if char belongs to the western codes.
    '''
    return char in Western_chars


# for i in lis:
#    print(is_western(i))


def is_nonspacing_class(char: str) -> bool:
    '''
    Determine if char belongs to the fullwidth codes.
    '''
    return not char.isspace() and \
            not (char in [codes for codes in NonSpacing.values()])


def apply_rules(pre, post):
    '''
    Apply (given local) rule to the pre- and post- elements given by functools.reduce from a string.
    '''
    # check validity
    if len(pre) == 0:
        return post

    # set rule
    # explained: if the pre-word is ended in a western char, while the post-word is not in accordance with the pre-word, then apply space.
    rule = is_western(pre[-1]) != is_western(post) and \
            is_nonspacing_class(post) and is_nonspacing_class(pre[-1])

    if rule:
        return ' '.join([pre, post])
    else:
        return ''.join([pre, post])


# TODO: Greek and Cyrillic.
# TODO: Kana and Hangul (optional), should provide options.
# TODO: Maths, e.g. `數學式為f:=x+1` -> `數學式為 f := x + 1`. So `:` and `=` should belongs to the same class from fullwidth.
# TODO: auto-spacing between quantities and their units, e.g. `20TB` -> `20 TB`, with exception `°`.
# TODO: strip unwanted spaces (anti-rule char spacings)
# TODO: Better module managemen.

if __name__ == '__main__':
    # check for valid argument
    if len(sys.argv) < 2:
        print('At least one argument is required!')
        exit()

    # read from the given file
    with open(sys.argv[1], 'r') as f:
        input_str = f.read()

    # TODO: take options of new file
    # TODO: take options of kana, hangul (later)
    # write the result
    output_str = functools.reduce(apply_rules, input_str, '')
    with open(sys.argv[2 if len(sys.argv) > 2 else 1], 'w') as f:
        f.write(output_str)

    # test = 'A紐幣的BAa as和s，沒想到 「a」無用'
