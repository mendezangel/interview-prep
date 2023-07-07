def all_permutations(string, i=0, letters=set()):
    if i >= len(string):
        return string
    letters = set([*string])
    print(string)
    for letter in letters:
        if letter != string[i]:
            string_list = [*string]
            string_list[i] = letter
            new_string = ''.join(string_list)
            all_permutations(new_string, i + 1, letters)
        


print(all_permutations('abc'))