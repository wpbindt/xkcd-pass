#!/usr/bin/env python
from argparse import ArgumentParser
import secrets


def generate(n: int, spaces: bool = True) -> str:
    with open('/usr/share/dict/words') as dict_file:
        words = [
            word
            for word in map(lambda x: x.strip(), dict_file)
            if word.isalpha()
        ]
    separator = ' ' if spaces else ''
    return separator.join(secrets.choice(words) for _ in range(n))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('words', type=int)
    parser.add_argument('--no-spaces', action='store_true')
    args = parser.parse_args()
    print(generate(
        args.words, 
        not args.no_spaces
    ))

