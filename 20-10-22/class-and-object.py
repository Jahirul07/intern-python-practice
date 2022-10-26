import secrets


class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# class __init__ function

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('John', 36)
# print(p1.name)
# print(p1.age)

# class __str__ function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# Object Method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is " + self.name)

p1 = Person('Jahir', 36)
p1.myfunc()

# The self Parameter

class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("hello my name is "+ abc.name)

p1 = Person("jhon",87)
p1.myfunc()
