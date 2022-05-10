import math
import numpy as np
key = ""

def getkey():
    key = input("please enter you key\n >>> ").replace(" ", "").upper()
    dim = math.floor(math.sqrt(len(key)))
    print(dim)
    if dim < 2:
        print("invalid Key")
        return getkey()
    return (key[:dim*dim], dim)


key, dim = getkey()

plain_text = input("please enter your plain text\n >>> ").replace(" ", "").upper()
end_of_plain_text = (len(plain_text)//dim)*dim
plain_text = plain_text[:end_of_plain_text]


def generateKeyMatrix(key, dim):
    keyMatrix = []
    for i in range(0, len(key), dim):
        keyMatrix.append([ord(j)-65 for j in key[i:i+dim]])
    return keyMatrix


def generatePlainMatrix(plain_text, dim):
    return [
        [ord(j) % 65 for j in list(plain_text[i:(i+dim)])]
        for i in range(0, len(plain_text), dim)
    ]


keyMatrix = generateKeyMatrix(key, dim)
plainMatrix = generatePlainMatrix(plain_text, dim)

print(keyMatrix)
print(plainMatrix)

# this function return the cipher text
def encrypt_it(encryptionKey,WorkingMatrix,dim):
    cipher_text = ""
    for i in range(len(WorkingMatrix)):
        working = WorkingMatrix[i]
        for j in range(dim):
            result = 0
            for k in range(dim):
                result += encryptionKey[j][k] * working[k]
            cipher_text+= chr((result%26)+65)
    return cipher_text
    
cipher_text = encrypt_it(keyMatrix, plainMatrix, dim)
print(cipher_text)
