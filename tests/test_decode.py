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
