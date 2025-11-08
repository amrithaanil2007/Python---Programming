#Basic Functions
def greet():
    print("Welcome to python function!")

greet()
greet()
greet()

# Greeting with name
def greet_user (name) :
    print("hello",name)

greet_user("amruthamol")
greet_user("elena")
greet_user("carolina")

##. Square function
def square(num):
    return num*num

result = square(3)
print ("sqare:",result)
result = square(6)
print("square:",result)
print(square(10))
print(square(100))

#maximum of two numbers
def get_max(a, b):
    if a > b:
        return a
    else:
        return b

max_value = get_max (40,30)
print("MAximum:",max_value)

#calling function inside a loop
def greet_user(name):
    print("Hello"+ name + "!")

names = ["elena","carolina","bony"]
for name in names:
    greet_user (name)

#function with default values - Ex guest
def greet_default(name="Guest"):
    print("Hello "+ name + "!")

greet_default ()
greet_default ("amruthamol")