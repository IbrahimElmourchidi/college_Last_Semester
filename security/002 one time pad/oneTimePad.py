"""
define all the characters available for encryption/decryption 
please note we made an assumption of:
    - using lower case english letters only
    - no spaces are allowed in the plain text
"""
allChars = 'abcdefghijklmnopqrstuvwxyz'

"""
taking the plain text as input from the user with some helper functions
.replace(' ', '') replace all spaces with empty char ie. remove all spaces
.lower() make sure that the plain text is all lower case 
"""
plain_text = input('enter you plain text : \n(length=10 without spaces)>> ').replace(' ', '').lower()

"""
the key should be a string with the same length of the plaintext
"""
key = "msecretkey"


"""
this is the function that is responsible for encryption (convert plain text to cipher text)
"""
def encryptIt(plain_text):
    # initiate the cipher text as empty string
    cipher_text = ''
    """
    check if the length of the plain_text != length of the key print error message and stop the function
    """
    if (len(plain_text) != len(key)):
        print("plain text and key must have the same length")
        return

    # loop through each char in the plain text, and the key to encrypt it.
    for i in range(len(plain_text)):
        """
        i : integer that refers to an index of character in the plain text
        Example: 
            if plain_text = 'hello' and i =1
            then plain_text[i] = 'e'  #remember string index is zero based

        .find() : Searches the string for a specified value (character or substring) and returns the position of where it was found 
        Example:
            if plain_text = 'hello'
            then plain_text.find('l') = 3  
            # note it only returns the first match
        """
        # the index of the plain text character in the allChars
        p_index = allChars.find(plain_text[i])
        # the index of the key character in the allChars
        k_index = allChars.find(key[i])
        cipher_text += allChars[(p_index+k_index)%26]
    """
    the return of the function is the cipher_text
    note: the return function outside the for loop
    """ 
    return cipher_text

# try the encryption function
cipher_text = encryptIt(plain_text)
print(cipher_text)


"""
this is the function that is responsible for decryption (convert cipher text to 
plain text)
"""
def decryptIt(cipher_text):
    # initiate the plain text as empty string
    plain_text = ''
    """
    check if the length of the cipher_text != length of the key print error message and stop the function
    """
    if (len(cipher_text) != len(key)):
        print("cipher text and key must have the same length")
        return
    """
        i : integer that refers to an index of character in the plain text
        Example: 
            if cipher_text = 'hello' and i =1
            then plain_text[i] = 'e'  #remember string index is zero based

        .find() : Searches the string for a specified value (character or substring) and returns the position of where it was found 
        Example:
            if plain_text = 'hello'
            then plain_text.find('l') = 3  
            # note it only returns the first match
    """
    for i in range(len(cipher_text)):
        # the index of the cipher text character in the allChars
        c_index = allChars.find(cipher_text[i])
        # the index of the key character in the allChars
        k_index = allChars.find(key[i])
        plain_text += allChars[(c_index-k_index)%26]
    """
    the return of the function is the cipher_text
    note: the return function outside the for loop
    """ 
    return plain_text

plain_text2 = decryptIt(cipher_text)
print(plain_text2)


"""
sample input: helloworld
cipher text: twpnfahbpb
"""