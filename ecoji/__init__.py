# coding: utf-8
from .mapping import EMOJIS, PADDING, PADDING40, PADDING41, PADDING42, PADDING43


def encode(reader, writer):
    read_bytes = reader.read(5)
    num_read = len(read_bytes)
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
        read_bytes = reader.read(5)
        num_read = len(read_bytes)
