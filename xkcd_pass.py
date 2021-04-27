#!/usr/bin/env python
from argparse import ArgumentParser
import secrets


def generate(n: int) -> str:
    with open('/usr/share/dict/words') as dict_file:
        words = [
            word
            for word in map(lambda x: x.strip(), dict_file)
            if word.isalpha()
        ]
    return ' '.join(secrets.choice(words) for _ in range(n))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('words', type=int)
    args = parser.parse_args()
    print(generate(args.words))

