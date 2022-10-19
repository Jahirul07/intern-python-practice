thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)

names = ['jahir','mehedi','mamun','hasan']
for name in names:
    print(name)

names = ['jahir','mehedi','mamun','hasan']
for name in range(len(names)):
    print(names[name])

# while loop
names = ['jahir','mehedi','mamun','hasan']
name = 0;
while name < len(names):
    print(names[name])
    name = name + 1;

thislist = ["apple", "banana", "cherry"]
fruit = 0;
while fruit < len(thislist):
    print(thislist[fruit])
    fruit = fruit + 1; 

thislist = ["apple", "banana", "cherry"]
[print(fruit) for fruit in thislist]    