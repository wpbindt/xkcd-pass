#!/usr/bin/env python
from argparse import ArgumentParser
import secrets


def load_dict() -> list[str]:
    with open('/usr/share/dict/words') as dict_file:
        return [
            word
            for word in map(lambda x: x.strip(), dict_file)
            if word.isalpha()
        ]


def generate(
    n: int, 
    spaces: bool = True,
    capital: bool = False,
    special: bool = False,
    number: bool = False,
) -> str:
    words = load_dict()
    separator = ' ' if spaces else ''
    prefix = compute_prefix(
        capital=capital,
        special=special,
        number=number,
    )
    return prefix + separator.join(secrets.choice(words) for _ in range(n))


def compute_prefix(
    capital: bool,
    special: bool,
    number: bool
) -> str:
    prefix = ''
    if capital:
        prefix += 'A'
    if special:
        prefix += '&'
    if number:
        prefix += '1'
    return prefix


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('words', type=int)
    parser.add_argument('--no-spaces', action='store_true')
    parser.add_argument('--special', action='store_true')
    parser.add_argument('--number', action='store_true')
    parser.add_argument('--capital', action='store_true')
    args = parser.parse_args()
    print(generate(
        args.words, 
        spaces=not args.no_spaces,
        capital=args.capital,
        number=args.number,
        special=args.special,
    ))

