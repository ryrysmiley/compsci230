int1 = int(input("Enter a number:"))
int2 = int(input("Enter another number:"))
print("Would you like to add or multiply the numbers? m for multiply a for add.")
choice = input()
if choice == "m":
    print(int1*int2)
elif choice == "a":
    print(int1+int2)
else:
    print("You failed to answer question run program again.")
