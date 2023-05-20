# write a function, most_frequent_char, that takes in a string as an
#argument. The function should return the most frequent character
# of the string. If there are ties, return the character that appears
# earlier in the string.

# You can assume that the input string is non-empty

# brute force
# nested loops

def most_frequent_char(s):
  char_counts = {}
  max_count = 0
  letter = ''
  for letter in s:
    if letter not in char_counts:
      char_counts.update({letter: 0})
    char_counts[letter] += 1

  for key, value in char_counts.items():
    if value > max_count:
      max_count = value
      letter = key

  return letter
      

print(most_frequent_char('bookeeper')) # -> 'e'
print(most_frequent_char('david')) # -> 'd'
print(most_frequent_char('abby')) # -> 'b'
print(most_frequent_char('mississippi')) # -> 'i'
print(most_frequent_char('potato')) # -> 'o'
print(most_frequent_char('eleventennine')) # -> 'e'
print(most_frequent_char('riverbed')) # -> 'r'