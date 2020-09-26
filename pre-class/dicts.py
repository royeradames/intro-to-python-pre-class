# Analogous to JS's objects

# create an empty dict
d = {}

# create a dict with some key-value pairs
e = {'foo': 12, 'bar': 20}

k = {10: 'baz', 15: 'car', 'foo': 12}

# how do we access a value in a dict?
# access it via its key using bracket notation
# there is no accessing of dict values via dot notation
print(e['foo'])
print(k[15])


# iterate through a dictory
# without using a special method, when we iterate, we
# only get access to the keys
for key in k:
    print(f'key: {key}, value: {k[key]}')

# we can access keys and values directly when iterating using
# the special method `items()`
for key, value in k.items():
    print(f'key: {key}, value: {value}')
