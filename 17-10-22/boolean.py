# print(10 > 9)
# print(10 == 9)
# print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

x = 45
y = 50

if x > y:
    print('x is greater than y')
else:
    print('x is not greater than y')


print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x, int))

print(bool(True))