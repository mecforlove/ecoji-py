# coding: utf-8
"""usage: ecoji [OPTIONS]... [FILE]

Encode or decode data as Unicode emojis. 😁

Options:
    -d, --decode          decode data
    -w, --wrap=COLS       wrap encoded lines after COLS character (default 76).
                          Use 0 to disable line wrapping
    -h, --help            Print this message
    -v, --version         Print version information.
"""
import sys
import argparse
from . import encode, decode, __version__, _DEFAULT_WRAP_COLS

_VERSION_MSG = """Ecoji-py version 1.0.0
    Copyright   : (C) 2018 mecforlove
    License     : Apache 2.0
    Source code : https://github.com/mecforlove/ecoji-py
"""


def main():
    parser = argparse.ArgumentParser()
    parser.usage = __doc__
    parser.add_argument(
        '-v',
        '--version',
        help='print version information',
        action='store_true')
    parser.add_argument(
        '-w', '--wrap', help='cols to wrap encoded lines', type=int)
    parser.add_argument(
        'filename', nargs='?', help='filename to encode', action='store')
    parser.add_argument(
        '-d', '--decode', help='decode data', action='store_true')
    args = parser.parse_args()
    if args.version:
        print(_VERSION_MSG)
    if args.decode:
        if args.filename:
            decode(open(args.filename[0], 'r'), sys.stdout.buffer)
        else:
            decode(sys.stdin, sys.stdout.buffer)
    if args.wrap is not None:
        wrap = wrap
    else:
        wrap = _DEFAULT_WRAP_COLS
    if args.filename:
        encode(open(args.filename[0], 'rb'), sys.stdout, wrap)
    else:
        encode(sys.stdin.buffer, sys.stdout, wrap)


if __name__ == '__main__':
    main()
