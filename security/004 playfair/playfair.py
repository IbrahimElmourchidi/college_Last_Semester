allChar = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
key= 'SECRET'
plain_text = input("enter your plain text\n >>").replace(" ", "").upper().replace('J', 'I')

def constructMat(allChar,key):
    matCore = key+allChar
    dummyDic = {}
    for i in matCore:
        dummyDic[i] = 0
    matrix = [[list(dummyDic.keys())[i+j] for i in range(5)] for j in range(5)]
    return matrix

mat = constructMat(allChar, key)

def plain_splitter(plain_text):
    t=0
    while t < len(plain_text)-1:
        ch1=plain_text[t]
        ch2=plain_text[t+1]
        if ch1==ch2:
            plain_text=plain_text[0:t+1]+'X'+plain_text[t+1:]
        t+=1
    return plain_text       

print(plain_splitter(plain_text))