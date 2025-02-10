#built-in functions/standards library functions

y = max(88, 44, 99, 66, 77)
print("the maximum value is", y)

x = min(88, 44, 99, 66, 77)
print("the minimum value is", x)

# user defined function
def name():
    print("jeremy")
name() #calling a function
def multiply():
    x = 10
    y = 2
    print(x * y)
multiply()

#-parameters/variable and argument/value
def add(a, b):

    print(a + b)
add(1, 2)
add(9, 6)

def employee(name, gender, position, salary, age):
    print(name, gender, position, salary, age)
employee("Jeremy", "Male","CEO" , 20000, 99)
employee("Mark", "Male","managing" , 20000, 99)
employee("Lucy", "female","HR" , 20000, 99)
employee("Grace", "female","DN" , 20000, 99)
employee("Brian", "Male","SC" , 20000, 99)

# A program that display details of 5 students
# Use a user-defined function with the parameter
# and argument
# Fullname age course gender

def student(Fullname,age,course,gender):
    print(Fullname,age,course,gender)
student("jeremy",99,"fullstack","Male")
student("Grace",88,"Medicine","Female")
student("Elizabeth",77,"Law","Female")
student("John",66,"Engineering","Male")
student("Lawrence",55,"Economics","Male")


