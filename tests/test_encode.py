# coding: utf-8
import unittest
import io

from ecoji import encode


class TestEncode(unittest.TestCase):
    def test_readnum_equals5(self):
        r = io.BytesIO(b'12345')
        w = io.StringIO()
        encode(r, w)
        self.assertEqual('🎌🚟🎗🈸\n', w.getvalue())
        r.close()
        w.close()

    def test_readnum_equals4(self):
        r = io.BytesIO(b'123456789')
        w = io.StringIO()
        encode(r, w)
        self.assertEqual('🎌🚟🎗🈸🎥🤠📠🏍\n', w.getvalue())
        r.close()
        w.close()

    def test_readnum_equals3(self):
        r = io.BytesIO(b'12345678')
        w = io.StringIO()
        encode(r, w)
        self.assertEqual('🎌🚟🎗🈸🎥🤠📒☕\n', w.getvalue())
        r.close()
        w.close()

    def test_readnum_equals2(self):
        r = io.BytesIO(b'1234567')
        w = io.StringIO()
        encode(r, w)
        self.assertEqual('🎌🚟🎗🈸🎥🤝☕☕\n', w.getvalue())
        r.close()
        w.close()

    def test_readnum_equals1(self):
        r = io.BytesIO(b'123456')
        w = io.StringIO()
        encode(r, w)
        self.assertEqual('🎌🚟🎗🈸🎥☕☕☕\n', w.getvalue())
        r.close()
        w.close()

    def test_wrap_cols(self):
        r = io.BytesIO(b'123456789123456')
        w = io.StringIO()
        encode(r, w, 6)
        wanted_str = '🎌🚟🎗🈸🎥🤠📠🐂\n🎐🚯🏛🐇\n'
        self.assertEqual(wanted_str, w.getvalue())
        r.close()
        w.close()

    def test_negative_wrap_cols(self):
        r = io.BytesIO(b'123456789123456')
        w = io.StringIO()
        encode(r, w, -1)
        wanted_str = '🎌🚟🎗🈸🎥🤠📠🐂🎐🚯🏛🐇\n'
        self.assertEqual(wanted_str, w.getvalue())
        r.close()
        w.close()
