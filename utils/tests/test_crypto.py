from unittest import TestCase
from utils import crypto

class TestCrypto(TestCase):
    def test_aes(self):
        aes = crypto.AESCipher(256)
        enc, dec = aes("132")
        code = enc("abc")
        assert("abc" == dec(code))