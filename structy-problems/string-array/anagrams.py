# write a function, anagrams, that takes in two strings as arguments.
# The function should return a boolean indicating whether or not the
# strings are anagrams. Anagrams are strings that contains the
# same characters, but in any order.

# def anagrams(s1, s2):
#   return sorted(s1) == sorted(s2)

def anagrams(s1, s2):
    characterCount = {}
    for letter in s1:
        if letter not in characterCount:
            characterCount.update({letter: 0})
        characterCount[letter] += 1

    for letter in s2:
        if letter not in characterCount:
            return False
        characterCount[letter] -= 1

    for count in characterCount.values():
        if count != 0: return False
    return True
print(anagrams('restful', 'fluster')) # -> True
print(anagrams('cats', 'tocs')) # -> False
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
print(anagrams('paper', 'reapa')) # -> False
print(anagrams('elbow', 'below')) # -> True
print(anagrams('tax', 'taxi')) # -> False
print(anagrams('taxi', 'tax')) # -> False
print(anagrams('night', 'thing')) # -> True
print(anagrams('abbc', 'aabc')) # -> False
print(anagrams('po', 'popp')) # -> false
print(anagrams('pp', 'oo')) # -> false