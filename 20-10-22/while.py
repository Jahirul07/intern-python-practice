# Python While Loops

from asyncio import constants


i = 1
while i <= 6:
    # print (i)
    i += 2

# Break statement
i = 1
while i< 6:
    # print(i)
    if i == 5:
        break
    i += 1

#  Continue 
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    # print(i)

# The else Statement
i = 1;
while i < 10:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')