# -*- coding: utf-8 -*-

import os

# https://github.com/bt3gl/My-Gray-Hacker-Resources/blob/patch-1/Cryptography/Rotation-Ciphers/cesarCipher_simple_2.py

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

'''
Cesar encrypt - better
'''

import sys

def encrypt(message, k):
    cipher = ''
    for c in message:
        c = (ord(c) + k) % 26
        if c < 32:
            c += 32
        cipher += chr(c)
    return cipher

def decrypt(message, k):
    cipher = ''
    for c in message:
        c = (ord(c) - k) % 26
        if c < 32:
            c += 126-32
        cipher += chr(c)
    return cipher

def main():
    #MESSAGE = list(raw_input('Enter the message to be encrypted: ')) or "all your basis belong to us"
    MESSAGE = 'jxu qdimuh je jxyi ijqwu yi qdimuhxuhu'
    for k in range (13, 14):

        encrypted_msg = encrypt(MESSAGE, k)
        print("Encrypted message: " + encrypted_msg)


        decrypted_msg = decrypt(MESSAGE, k)
        print("Decrypted message: " + decrypted_msg)

if __name__ == '__main__':
    main()

os.system("pause")
