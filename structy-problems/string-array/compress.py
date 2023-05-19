# Write a function, compress, that takes in a string as an argument. The function should
# return a compressed version of the string where consecutive occurrences of the same characters
# are compressed into the number of occurrences followed by the character. Single character occurrences
# should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# Two pointers
# starting at start of string, assign a var as current char
# also asssign a count var that will keep track of the number of appearances
# increment second pointer until you encounter another char
# when you encounter another char, add current char to a final string the number of times that it appeared

def compress(s):
    i = 0
    j = 0
    finalString = ''
    while (i < len(s)):
        currentChar = s[i]
        j += 1
        if j >= len(s):
            count = j - i
            finalString += string(currentChar, count)
            break

        elif s[j] != currentChar:
            count = j - i
            finalString += string(currentChar, count)
            i = j

    return finalString


def string(char, count):
    return char if count == 1 else f"{str(count)}{char}"


print(compress('ccaaatsss'))  # -> '2c3at3s'
print(compress('ssssbbz'))  # -> '4s2bz'
print(compress('ppoppppp'))  # -> '2po5p'
print(compress('nnneeeeeeeeeeeezz'))  # -> '3n12e2z'
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'))  # -> '127y'
