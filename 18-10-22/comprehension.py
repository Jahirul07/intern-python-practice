fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if 'b' in x:
        newList.append(x)

print(newList)


# one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if 'a' in x]
print(newList)

# newList = [expression for item in iterable if condition == true]

newList = [x for x in fruits if x != 'apple']
print(newList)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)