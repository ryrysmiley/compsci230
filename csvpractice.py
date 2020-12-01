import csv
x=input("what file you want to open")
list=[]
user_input=""
while user_input!="q":
    try:
        fields=input("Enter the name and the grade of your student")
        lst=fields.split() #["Doe", "John", "A"]
        if lst[2] not in ["A","B","C","D","F"]:
            raise ValueError("Invalid Grade")
        with open(x,"a",newline="") as fd:
            writer=csv.writer(fd,delimiter=",")
            writer.writerow(lst)
    except ValueError as e:
        print(e)
    user_input = input("enter q to quit")
