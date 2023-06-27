dict1 = {}
dict1['x'] = 1 + dict1.get('x')
print(dict1['x'])
dict1['x'] = 1 + dict1.get('x')
print(dict1['x'])