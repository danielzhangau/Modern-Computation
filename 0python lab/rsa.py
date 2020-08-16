# -*- coding: utf-8 -*-
"""
RSA Encryption script

Created on Fri Feb  1 12:56:03 2019

@author: shakes
"""
import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

class RSA:
    '''
    RSA encryption class for encrypting/decrypting messages using modular exponentiation.
    '''

    def __init__(self, pubKey, key, mod):
        '''
        Constructor
        '''
        self.publicKey = pubKey #used to encrypt, everyone has access and can use
        self.privateKey = key #private, only you can use to decrypt
        self.modulus = mod
        
    def encrypt(self, m):
        '''
        Encrypt number given keys
        '''
        #modpow
        return m ** self.publicKey % self.modulus
    
    def decrypt(self, c):
        '''
        Decrypt number given keys
        '''
        #modpow
        return c ** self.privateKey % self.modulus
'''choose two large prime'''
p = 61
q = 53
n = p * q
'''euler totient function'''
phi = (p-1)*(q-1)
'''choose a small e, greater than 2'''
for e in range(2,phi):
    if gcd(e, phi) == 1:
        break
'''inverse of e mod phi
e * d mod phi = 1
'''
for i in range(1, 10):
    x = 1 + i*phi
    if x % e == 0:
        d = int(x/e)
        break
print(e)
print(d)
print(n)



Encryptor = RSA(e, d, n)
message = 9
print("Message:", message)
encryptedMessage = Encryptor.encrypt(message)
print("Encrypted Message:", encryptedMessage)
decryptedMessage = Encryptor.decrypt(encryptedMessage)
print("Decrypted Message:", decryptedMessage)
