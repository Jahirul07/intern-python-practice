list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2;
print(list3);

# another way -- append
list1 = ["a", "b" , "c"]
list2 = [3, 2, 1]
for x in list2:
    list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
