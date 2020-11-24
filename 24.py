Hours = int(input("Enter a time in 24 hour format. 0-23(integer):"))
if Hours < 0 or Hours > 23:
    print("Invalid Input")
elif Hours == 12:
    print(Hours, "PM")
elif Hours > 13:
    Hours -= 12
    print(Hours, "PM")
elif Hours == 0:
    print(12, "AM")
else:
    print(Hours, "AM")
