def my_function(food):
    for x in food:
        print(x)
fruit = {"apple","banana","mango"}
my_function(fruit)

def is_adult(age):
    return age >= 18
print(is_adult(20))

def emo(happy):
    return happy=="laugh"
print(emo("laugh"))

def add(num):
    return 0+num
print(add(2))

def say_hello():
    print("hello")
say_hello()

def add(a,b):
    return a+b
result = add(2,3)
print(result)

def greet(name="LovePreet"):
    print("Welcome" ,name)
greet()
greet("Harpreet")


def is_even(number):
    if number % 2==0:
        print("Number is Even")
    else:
        print("Number is odd")
is_even(9)

def is_odd(no):
    if no % 2 ==0:
        return True
    else :
        return False
num = 9
if is_odd(num):
    print("Even Number")
else:
    print("Odd Number")