def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))

class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)
