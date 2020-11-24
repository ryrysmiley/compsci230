#drink order :))
total_cost = 0

sm_tea = 2.0
sm_cof = 2.25

med_tea = 3.5
med_cof = 3.75 #shot of vanilla .50

lar_tea = 4.65 #fancy organic Oprah .75
lar_cof = 4.85 #shot of vanilla syrup .50

drink_list = []

while True:

  drink_type = input("Coffee or Tea? ")
  drink_size = ""
  drink_name = ""
  drink_cost = 0


  if drink_type == "Coffee" or drink_type == "coffee":
    drink_size = input("Small, Medium, or Large? ")
    drink_size = drink_size.upper()
    if drink_size == "SMALL" or drink_size == "S":
      drink_cost = sm_cof
      drink_name = "Small Coffee"

    elif drink_size == "MEDIUM" or drink_size == "M":
      choice = input("Would you like a shot of vanilla syrup for the coffee?(+$.50)")
      if choice == "Yes" or choice == "yes" or choice == "y":
        drink_cost = med_cof + .5
        drink_name = "Medium Coffee w/ vanilla syrup"
      elif choice == "No" or choice == "no" or choice == "n":
        drink_cost = med_cof
        drink_name = "Medium Coffee"
      else:
        print("input error try not to do that again, drink has been cancelled")
        continue

    elif drink_size == "LARGE" or drink_size == "L":
      choice = input("Would you like a shot of vanilla syrup for the coffee?(+$.50)")
      if choice == "Yes" or choice == "yes" or choice == "y" or choice == "Y":
        drink_cost = lar_cof + .5
        drink_name = "Large Coffee w/ vanilla syrup"
      elif choice == "No" or choice == "no" or choice == "n" or choice == "N":
        drink_cost = lar_cof
        drink_name = "Large Coffee"
      else:
        print("input error try not to do that again, drink has been cancelled")
        continue

    else:
      print("input error try not to do that again, drink has been cancelled")
      continue

  elif drink_type == "Tea" or drink_type == "tea":
    drink_size = input("Small, Medium, or Large? ")
    drink_size = drink_size.upper()
    if drink_size == "SMALL" or drink_size == "S":
      drink_cost = sm_tea
      drink_name = "Small Tea"

    elif drink_size == "MEDIUM" or drink_size == "M":
      drink_cost = med_tea
      drink_name = "Medium Tea"

    elif drink_size == "LARGE" or drink_size == "L":
      choice = input("Would you like to upgrade to the fancy-organic-Oprah-sponsored option?(+$.75)")
      if choice == "Yes" or choice == "yes" or choice == "y":
        drink_cost = lar_tea + .75
        drink_name = "Large Tea (fancy-organic-Oprah-sponsored option)"
      elif choice == "No" or choice == "no" or choice == "n":
        drink_cost = lar_tea
        drink_name = "Large Tea"
      else:
        print("input error try not to do that again, drink has been cancelled")
        continue

    else:
      print("input error try not to do that again, drink has been cancelled")
      continue
  else:
    print("input error try not to do that again, drink has been cancelled")
    continue

  print("Drink:{}".format(drink_name))
  print("Price:${:.2f}".format(float(drink_cost)))

  drink_list.append(drink_name)
  total_cost += drink_cost
  print("Total Cost:${:.2f}".format(float(total_cost)))
  ordermore = input("Continue ordering? yes or no?")
  ordermore = ordermore.upper()

  if ordermore == "YES" or ordermore == "Y":
      continue
  elif ordermore == "NO" or ordermore == "N":
      break
  else:
      print("Invalid input ending order")
      break


print("List of drinks:", drink_list)
print("Your total is ${:.2f}".format(float(total_cost)))
