#!/usr/bin/env python
from argparse import ArgumentParser
import secrets
from string import ascii_uppercase, digits, punctuation


def generate(
    n: int,
    charsets_to_insert: list[list[str]],
    spaces: bool = True,
) -> str:
    words = load_dict()
    separator = ' ' if spaces else ''
    password = separator.join(secrets.choice(words) for _ in range(n))
    for charset in charsets_to_insert:
        password = insert_char(password, charset)
    return password


def insert_char(password: str, chars: list[str]):
    insert_at = secrets.randbelow(len(password))
    char = secrets.choice(chars)
    return password[:insert_at] + char + password[insert_at:]


def load_dict() -> list[str]:
    with open('/usr/share/dict/words') as dict_file:
        return [
            word
            for word in map(lambda x: x.strip(), dict_file)
            if word.isalpha()
        ]


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('words', type=int)
    parser.add_argument('--no-spaces', action='store_true')
    parser.add_argument('--special', action='store_true')
    parser.add_argument('--number', action='store_true')
    parser.add_argument('--capital', action='store_true')
    args = parser.parse_args()

    charsets = []
    if args.special:
        charsets.append(list(punctuation))
    if args.capital:
        charsets.append(list(ascii_uppercase))
    if args.number:
        charsets.append(list(digits))

    print(generate(
        args.words, 
        charsets_to_insert=charsets,
        spaces=not args.no_spaces,
    ))

