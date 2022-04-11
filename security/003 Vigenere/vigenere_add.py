allChars = 'abcdefghijklmnopqrstuvwxyz'
plain_text = input('please enter your plain text\n>>> ').replace(" ", "").lower()
key = 'secret'

def encryptIt(plain_text, key):
    cipher_text = ''
    for i in range(len(plain_text)):
        p_index = allChars.find(plain_text[i])
        k_index = allChars.find(key[i%len(key)])
        cipher_text+= allChars[(p_index+k_index)%26]
    return cipher_text

cipher_text = encryptIt(plain_text, key)
print(cipher_text)


def decryptIt(cipher_text, key):
    plain_text = ''
    for i in range(len(cipher_text)):
        c_index = allChars.find(cipher_text[i])
        k_index = allChars.find(key[i%len(key)])
        plain_text += allChars[(c_index - k_index)%26]
    return plain_text

plain_text2 = decryptIt(cipher_text, key)
print(plain_text2)