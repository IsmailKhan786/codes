# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:59:00 2021

@author: Ismail khan
"""

#ceasor cypher
#This func to encrypt the password
def encrypt(PT,Key):
    alph='abc defghijklmnopqrstuvwxyz'
    result=""
    for c in PT:
        #user input adds the key to it
        i=(alph.index(c) + Key)%27
        result+=alph[i]
    return result
#decrypt password

def decrypt(CT,Key):
    alph='abc defghijklmnopqrstuvwxyz'
    result=""
    for c in CT:
        #user input subtracts they kry to it
        i=(alph.index(c) - Key)%27
        result+=alph[i]
    return result
# user input passwprd 
pw=input("Enter the password")
shift=int(input("Enter the key tp shift"))
ciphertext=encrypt(pw,shift)
print(ciphertext)
plaintext= decrypt(ciphertext , shift)
print(plaintext)
