"""
try:
    f=open("test.txt")
    print(f.read())

except FileNotFoundError:
    print("File doesn't exist")

try:
    x=int(input())
    print(2/x)
except ValueError:
    print("that is not an int")
except ZeroDivisionError:
    print("can't divide by zero")
"""
user_input = ''
while user_input != "q":
    try:
        user_age=int(input("age"))
        if user_age<=0:
            raise ValueError("Invalid age")
        print(user_age)
        weight=int(input("weight"))
        if weight<=0:
            raise ValueError("Invalid weight")
        print(weight)
        height=int(input("height"))
        if height<=0:
            raise ValueError("Invalid height")
        print(height)
    except ValueError as e:
        print(e)

    user_input = input("q to quit")
