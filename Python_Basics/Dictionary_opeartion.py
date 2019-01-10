from collections import OrderedDict

dict0 = {'color': 'green'}
print(dict0['color'])

dict1 = {}
dict1['color'] = 'green'
dict1['points'] = 5
print(dict1)

dict2 = {'color': 'green', 'points': 5}
print(dict2)
del dict2['points']
print(dict2)

dict3 = {
    'usr1': 'python',
    'usr2': 'c',
    'usr3': 'c++',
    'usr4': 'matlab',
}
print(dict3['usr1'])

# Looping through all key-value pairs
user0 = {
    'username': 'hahaha',
    'first': 'my_first_name',
    'last': 'my_last_name',
}
for key, value in user0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# Looping through all the keys in a dictionary
dict4 = {
    'usr1': 'python',
    'usr2': 'c',
    'usr3': 'c++',
    'usr4': 'matlab',
}
for name in dict4.keys():
    print(name)

# Looping through a dictionary's keys in order
dict5 = {
    'usr1': 'python',
    'usr2': 'c',
    'usr3': 'c++',
    'usr4': 'matlab',
}
for name in sorted(dict5.keys()):
    print(name)

# Looping through all values in a dictionary
dict6 = {
    'usr1': 'python',
    'usr2': 'c',
    'usr3': 'c++',
    'usr4': 'matlab',
}
for language in dict6.values():
    print(language)

# Without repetition, we can use a set.
dict7 = {
    'usr1': 'python',
    'usr2': 'c',
    'usr3': 'c++',
    'usr4': 'python',
}
for language in set(dict7.values()):
    print(language)

# Dictionary in list
# Make an empty list for storing aliens.
dict_list = []
# Make 30 green aliens.
for dict_number in range(30):
    new_dict= {'color': 'green', 'points': 5, 'speed': 1}
    dict_list.append(new_dict)
# Show the first 5 dicts:
for dictElement in dict_list[:5]:
    print(dictElement)

# List in dictionary
dict8 = {
    'field1': 'value1',
    'field2': ['value11', 'value12'],
}

# Dictionary in dictionary
users = {
    'user1': {
        'first': 'user1 first',
        'last': 'user1 last',
        'location': 'user1 location',
        },
    'user2': {
        'first': 'user2 first',
        'last': 'user2 last',
        'location': 'user2 location',
        },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# Keep track of the order in which key-value pairs are added with OrderedDict
para_dict = OrderedDict()
para_dict['field1'] = 'para1'
para_dict['field2'] = 'para2'
para_dict['field4'] = 'para4'
para_dict['field3'] = 'para3'
for key, value in para_dict.items():
    print(key + ": " + value + ".")
