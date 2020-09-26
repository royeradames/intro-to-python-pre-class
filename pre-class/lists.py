# in python, arrays are called lists

# create an empty list
l = []

# create a list with some numbers
n = [10, 60, 20, 5]

# add a number to n
n.append(77)

# print our list n
print(n)

# print out each element in the n one at a time
for elem in n:
    print(elem)

# what if we also want the index of the element?
# enumerate gives us access to each list index and then it's element
for index, elem in enumerate(n):
    print(f'Element {index} is {elem}')
