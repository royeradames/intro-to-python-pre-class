# create a list containing all of even numbers up to 20
evens = []

for n in range(20):
    # loop through these numbers
    # check if they're even
    # if they are, add it to our list
    if n % 2 == 0:
        evens.append(n)
print(evens)


# let's use a list comprehension to do the same thing
evens = [n for n in range(20)if n % 2 == 0]

print(evens)


# steps for creating a list comprehension
# 1. write out how you'd do the same logic with a normal for loop
# 2. Take the for loop you wrote and "translate" it into list comprehension

squares = []

# populate a list with all of the squares up to 20
for n in range(20):
    squares.append(n*n)
print(squares)

squares2 = [n*n for n in range(20)]


print(squares2)
