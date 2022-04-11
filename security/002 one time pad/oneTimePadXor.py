
"""
taking the plain text as input from the user with some helper functions
"""
plain_text = input('enter you plain text : \n(length=10)>> ')

"""
the key should be a string with the same length of the plaintext
"""
key = "msecretkey"


"""
both encryption and decreption have the same logic , so this function is used 
for both encryption and decreption
"""
def encrypt_decrypt_it(text):
    # initiate the result as empty string
    result = ''
    """
    check if the length of the plain_text != length of the key print error message and stop the function
    """
    if (len(text) != len(key)):
        print("plain text and key must have the same length")
        return

    # loop through each char in the plain text, and the key to encrypt it.
    for i in range(len(text)):
        """
        i : integer that refers to an index of character in the text
        Example: 
            if text = 'hello' and i =1
            then text[i] = 'e'  #remember string index is zero based

        chr(i) : get the character with ascii code = i ; i is integer
        ord(ch) : get the ascii code of ch; ch is character
        """
        result+=chr(ord(text[i])^ord(key[i]))
    """
    the return of the function is the text
    note: the return function outside the for loop
    """ 
    return result


cipher_text = encrypt_decrypt_it(plain_text)
print(len(cipher_text))

plain_text2 = encrypt_decrypt_it(cipher_text)

print(plain_text2)