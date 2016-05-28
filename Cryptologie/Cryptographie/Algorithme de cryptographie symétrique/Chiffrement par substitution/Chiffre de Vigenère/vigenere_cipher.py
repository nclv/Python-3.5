# -*- coding: utf-8 -*-

import os

from itertools import starmap, cycle


def encrypt(message, key):

    # convert to uppercase.
    # strip out non-alpha characters.
    message = filter(lambda _: _.isalpha(), message.upper())

    # single letter encrpytion.
    def enc(c, k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))

    return "".join(starmap(enc, zip(message, cycle(key))))


def decrypt(message, key):

    # single letter decryption.
    def dec(c, k): return chr(((ord(c) - ord(k)) % 26) + ord('A'))

    return "".join(starmap(dec, zip(message, cycle(key))))

text = "Beware the Jabberwock, my son! The jaws that bite, the claws that catch!"
key = "VIGENERECIPHER"

encr = encrypt(text, key)
decr = decrypt(encr, key)

print(text)
print(encr)
print(decr)

os.system("pause")
