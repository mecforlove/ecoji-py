# coding: utf-8
from .mapping import EMOJIS, PADDING, PADDING40, PADDING41, PADDING42, PADDING43, EMOJI2BYTE

__version__ = '0.1.0'
__all__ = ('encode', 'decode')

_DEFAULT_WRAP_COLS = 76


class EcojiError(Exception):
    pass


class DecodeError(EcojiError):
    pass


def encode(reader, writer, wrap=_DEFAULT_WRAP_COLS):
    read_bytes = reader.read(5)
    num_read = len(read_bytes)
    written_len = 0
    while num_read:
        data = [0] * 5
        for index, byte in enumerate(read_bytes):
            data[index] = byte

        if num_read == 1:
            writer.write(EMOJIS[data[0] << 2 | data[1] >> 6])
            writer.write(PADDING)
            writer.write(PADDING)
            writer.write(PADDING)
        elif num_read == 2:
            writer.write(EMOJIS[data[0] << 2 | data[1] >> 6])
            writer.write(EMOJIS[(data[1] & 0x3f) << 4 | data[2] >> 4])
            writer.write(PADDING)
            writer.write(PADDING)
        elif num_read == 3:
            writer.write(EMOJIS[data[0] << 2 | data[1] >> 6])
            writer.write(EMOJIS[(data[1] & 0x3f) << 4 | data[2] >> 4])
            writer.write(EMOJIS[(data[2] & 0x0f) << 6 | data[3] >> 2])
            writer.write(PADDING)
        elif num_read == 4:
            writer.write(EMOJIS[data[0] << 2 | data[1] >> 6])
            writer.write(EMOJIS[(data[1] & 0x3f) << 4 | data[2] >> 4])
            writer.write(EMOJIS[(data[2] & 0x0f) << 6 | data[3] >> 2])
            t = data[3] & 0x03
            if t == 0:
                writer.write(PADDING40)
            if t == 1:
                writer.write(PADDING41)
            if t == 2:
                writer.write(PADDING42)
            if t == 3:
                writer.write(PADDING43)
        else:
            writer.write(EMOJIS[data[0] << 2 | data[1] >> 6])
            writer.write(EMOJIS[(data[1] & 0x3f) << 4 | data[2] >> 4])
            writer.write(EMOJIS[(data[2] & 0x0f) << 6 | data[3] >> 2])
            writer.write(EMOJIS[(data[3] & 0x03) << 8 | data[4]])
        written_len += 4
        if wrap > 0:
            if written_len >= wrap:
                writer.write('\n')
                written_len = 0
        read_bytes = reader.read(5)
        num_read = len(read_bytes)
    if written_len:
        writer.write('\n')


def decode(reader, writer):
    char0 = _read_emoji(reader)
    while len(char0):
        char1 = _read_emoji(reader)
        char2 = _read_emoji(reader)
        char3 = _read_emoji(reader)

        bits0 = EMOJI2BYTE.get(char0) or 0
        bits1 = EMOJI2BYTE.get(char1) or 0
        bits2 = EMOJI2BYTE.get(char2) or 0
        if char3 == PADDING40:
            bits3 = 0
        if char3 == PADDING41:
            bits3 = 1 << 8
        if char3 == PADDING42:
            bits3 = 2 << 8
        if char3 == PADDING43:
            bits3 = 3 << 8
        else:
            bits3 = EMOJI2BYTE.get(char3) or 0
        out = [0] * 5
        out[0] = bits0 >> 2
        out[1] = ((bits0 & 0x3) << 6) | (bits1 >> 4)
        out[2] = ((bits1 & 0xf) << 4) | (bits2 >> 6)
        out[3] = ((bits2 & 0x3f) << 2) | (bits3 >> 8)
        out[4] = bits3 & 0xff
        out = bytes(out)
        if char1 == PADDING:
            out = out[:1]
        if char2 == PADDING:
            out = out[:2]
        if char3 == PADDING:
            out = out[:3]
        if char3 in (PADDING40, PADDING41, PADDING42, PADDING43):
            out = out[:4]
        writer.write(out)
        char0 = _read_emoji(reader)


def _read_emoji(reader):
    c = reader.read(1)
    if len(c) == 0:
        return ''
    while c == '\n':
        c = reader.read(1)
    return c
