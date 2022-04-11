"""
define all the characters available for encryption/decryption 
please note we made an assumption of using lower case english letters only
"""
allChars = 'abcdefghijklmnopqrstuvwxyz'

"""
taking the plain text as input from the user with some helper functions
.replace(' ', '') replace all spaces with empty char ie. remove all spaces
.lower() make sure that the plain text is all lower case 
"""
plain_text = input('enter you plain text: \n>> ').replace(' ', '').lower()

"""
the key should be an integer
"""
key = 5


"""
this is the function that is responsible for encryption (convert plain text to cipher text)
"""
def encryptIt(plain_text):
    # initiate the cipher text as empty string
    cipher_text = ''
    # loop through each char in the plain text to encrypt it.
    for char in plain_text:
        """
        .find() : Searches the string for a specified value (character or substring) and returns the position of where it was found 
        Example:
            if plain_text = 'hello'
            then plain_text.find('l') = 3  
            # note it only returns the first match
        """
        p_index = allChars.find(char)  # the index of the plain text character in the allChars

        cipher_text += allChars[(p_index+key) % 26]
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
    # loop over each char in the cipher text to decrypt it 
    for char in cipher_text:
        """
        .find() : Searches the string for a specified value (character or substring) and returns the position of where it was found 
        Example:
            if cipher_text = 'xkrmj'
            then plain_text.find('m') = 3  
            # note it only returns the first match
        """
        c_index = allChars.find(char) # the index of the cipher text character in the allChars

        plain_text += allChars[(c_index-key) % 26]
    """
    the return of the function is the plain_text
    note: the return function outside the for loop
    """
    return plain_text


plain_text2 = decryptIt(cipher_text)

print(plain_text2)
