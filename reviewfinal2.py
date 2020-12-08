united_states_capitals = {
"Alabama":"Montgomery",
"California":"Sacramento",
"Colorado":"Denver",
"Hawaii":"Honolulu",
"Kansas":"Topeka",
"New Jersey":"Trenton",
"Ohio":"Columbus"
}
for key, value in united_states_capitals.items():
    print("The capital of {} is _____".format(key))
    x = input()
    if x==value:
        print("good job!")
    else:
        print("wrong! correct answer:", value)
