#Removing an item from a tuple (by converting to list)
a = (1920, 1080, 'hi')
b = list(a)
b.remove(1920)
a = tuple(b)
print(a)


