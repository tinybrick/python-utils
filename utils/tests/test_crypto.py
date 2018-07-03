from unittest import TestCase
from utils import crypto

class TestCrypto(TestCase):
    def test_aes(self):
        aes = crypto.AESCipher(256)
        enc, dec = aes("132")
        code = enc("abc")
        assert("abc" == dec(code))
        code = enc("ABC")
        assert("ABC" == dec(code))

        content = "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 " \
            "longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 longer then 256 "
        code = enc(content)
        assert(content == dec(code))