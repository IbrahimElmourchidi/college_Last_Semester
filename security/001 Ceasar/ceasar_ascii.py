plain_text = input('enter you plain text: \n>> ').replace(' ', '').lower()

key = 5

def encryptIt(plain_text):
    cipher_text = ''
    for i in plain_text:
        index = ord(i)
        cipher_text+= chr(index+key)
    return cipher_text

cipher_text = encryptIt(plain_text)
print(cipher_text)


def decryptIt(cipher_text):
    plain_text = ''
    for i in cipher_text:
        index = ord(i)
        plain_text += chr(index-key)
    return plain_text

plain_text2 = decryptIt(cipher_text)
print(plain_text2)

