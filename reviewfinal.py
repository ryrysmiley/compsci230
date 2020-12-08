import random
import csv

score = 0
name = input("Enter your name: ")
for i in range(3):
    first_num = random.randint(0,100)
    second_num = random.randint(0,100)
    print("What is {} + {}?".format(first_num,second_num))
    user_input=input("Answer: ")
    try:
        if int(user_input) == first_num + second_num:
            score+=1
    except ValueError:
        pass
print("Final score: {}/3".format(score))


with open("testgrades.csv","a",newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name,score])
