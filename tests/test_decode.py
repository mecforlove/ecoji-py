# coding: utf-8
import unittest
import io

from ecoji import decode


class TestDecode(unittest.TestCase):
    def test_decode(self):
        r = io.StringIO('🎌🚟🎗🈸🎥🤠📠🐂🎐🚯🏛🐇\n')
        w = io.BytesIO()
        decode(r, w)
        self.assertEqual(b'123456789123456', w.getvalue())
        r.close()
        w.close()

    def test_decode_four_byte_tail(self):
        # Each padding emoji carries the last two bits of a 4-byte tail.
        cases = [
            ('🎌🚟🎖⚜\n', b'1230'),
            ('🎌🚟🎖🏍\n', b'1231'),
            ('🎌🚟🎖📑\n', b'1232'),
            ('🎌🚟🎖🙋\n', b'1233'),
            ('💽📸🌎🔍🍑📴🍧🏍\n', b'{"a":"b"}'),
        ]
        for encoded, expected in cases:
            with self.subTest(expected=expected):
                w = io.BytesIO()
                decode(io.StringIO(encoded), w)
                self.assertEqual(expected, w.getvalue())
