from unittest import result


def mufunction(fname,lname):
    print(fname +" "+lname)

mufunction('jahirul','islam')


def my_function(*kids):
    print('The youngest child is ' + kids[2])

my_function('email', 'tobies','linus')

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1="Emai",child2="Tobies",child3="Linus")

def my_function(**kid):
    print("his last name is "+ kid['lname'])

my_function(fname = 'Tobias',lname = 'Refsnes')

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)

def my_function(x):
    return 5 * x

print(my_function(10))

# Recursion Function

def tri_recusion(k):
    if (k > 0):
        result = k + tri_recusion(k-1)
        print(result);
    else:
        result = 0
    return result

print('\n\nRecursion Example Results')
tri_recusion(6)

#! lambda function
x = lambda a : a + 10
print(x(5))


x = lambda a,b : a*b

print(x(5,6))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))