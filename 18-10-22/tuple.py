thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]);

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if 'apple' in thistuple:
    print('yes apple is in the fruits tuple')

# Python - Update Tuples
x = ("apple", "banana", "cherry")

y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append('orange')
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ('orange', 'kiwi',)
thistuple += y
print(thistuple);

# remove item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove('banana')
thistuple = tuple(y)
print(thistuple)

# delete items
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)

# Python - Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# =========================
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for s in thistuple:
    print(s)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")

fruit = 0;
while fruit < len(thistuple):
    print(thistuple[fruit])
    fruit = fruit + 1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("a", "b", "c")
mytuple = fruits * 3

print(mytuple)