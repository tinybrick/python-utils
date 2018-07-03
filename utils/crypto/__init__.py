from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib
from functools import *


def AESCipher(length):
    length = length / 8

    def generate_crypto(key):
        _key = hashlib.sha256(key.encode()).digest()
        aes_new = partial(AES.new, _key, AES.MODE_CBC)

        def encrypter(raw):
            _raw = _pad(raw)
            _iv = Random.new().read(AES.block_size)
            cipher = aes_new(_iv)
            return base64.b64encode(_iv + cipher.encrypt(_raw))

        def decrypter(enc):
            _enc = base64.b64decode(enc)
            _iv = _enc[:AES.block_size]
            cipher = aes_new(_iv)
            return _unpad(cipher.decrypt(_enc[AES.block_size:])).decode('utf-8')

        def _pad(s):
            return s + int((length - len(s) % length)) * chr(int(length - len(s) % length))

        def _unpad(s):
            return s[:-ord(s[len(s)-1:])]

        return encrypter, decrypter

    return generate_crypto
