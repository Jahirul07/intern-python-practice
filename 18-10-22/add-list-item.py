thislist = ["apple", "banana", "cherry"]
thislist.append('kiwi');
print(len(thislist));
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2,'orange');
print(len(thislist));

#  extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist[4])
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange","banana")
thislist.extend(thistuple)
print(thislist)