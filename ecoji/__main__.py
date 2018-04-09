# coding: utf-8
from . import encode


def main():
    from io import BytesIO

    r = BytesIO(b'aaaaa')
    f = open('yy', 'w')
    encode(r, f)


if __name__ == '__main__':
    main()