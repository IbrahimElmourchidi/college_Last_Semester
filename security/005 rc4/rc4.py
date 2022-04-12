plain_text = 'hello world'


# step 1
s = [ i for i in range(256)]
#step 2
key = 'secret'
t = [ord(key[i%len(key)]) for i in range(256)]

# step 3 ksa
j = 0
for i in range(256):
    j = (j +s[i] +t[i])%256
    s[i], s[j] = s[j], s[i]

# step 4 prga
j = 0
key = []
for i in range(len(plain_text)):
    i= (i+1)%len(plain_text)
    j = (j + s[i])% len(s)
    s[i], s[j] = s[j],s[i]
    t = (s[i]+s[j])% len(s)
    key.append(s[t])

cipher_text =''

for i in range(len(plain_text)):
    cipher_text += chr(ord(plain_text[i]) ^ key[i])

print(cipher_text)

plain_text2 = ''
for i in range(len(cipher_text)):
    plain_text2 += chr(ord(cipher_text[i]) ^ key[i])

print(plain_text2)



