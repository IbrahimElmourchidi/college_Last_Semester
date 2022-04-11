allChars = 'abcdefghijklmnopqrstuvwxyz'
mat = [ [allChars[(i+j)%26] for i in range(len(allChars))] for j in range(len(allChars))]


plain_text = input('please enter your plain text\n>>> ').replace(" ", "").lower()
key = 'secret'

def encryptIt(plain_text, key):
    cipher_text = ''
    for i in range(len(plain_text)):
        p_index = allChars.find(plain_text[i])
        k_index = allChars.find(key[i%len(key)])
        cipher_text+= mat[k_index][p_index]
    return cipher_text

cipher_text = encryptIt(plain_text, key)
print(cipher_text)

def decryptIt(cipher_text, key):
    plain_text = ''
    for i in range(len(cipher_text)):
        k_index = allChars.find(key[i%len(key)])
        row = mat[k_index]
        character_index = row.index(cipher_text[i])
        plain_text += allChars[character_index] 
    return plain_text

plain_text2 = decryptIt(cipher_text, key)
print(plain_text2)


