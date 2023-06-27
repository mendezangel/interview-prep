# Given a non empty string of lowercase letters and a non negative 
# integer representing a key, write a function that returns a new
# string obtained by shifting every letter in the input string by
# k positions in the alphabet, where k is the key

# Note that letters should "wrap" around the alphabet; in other words
# the letter z shifted by one returns the letter a.

def caesar_cipher_encryptor(string, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string_array = []
    for letter in string:
        new_letter_index = alphabet.index(letter) + key
        if new_letter_index > len(alphabet) - 1:
            new_letter_index = new_letter_index - (len(alphabet))
        string_array.append(alphabet[new_letter_index])
    return ''.join(str(letter) for letter in string_array)


print(caesar_cipher_encryptor("xyz", 2)) # "zab"