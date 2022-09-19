guestList = ['Jack Harlow', 'Michael Jordan', 'Jack Paisley', 'Selena Gomez', 'Jeniffer Lopez', 'Kylie Jenner']

print(f"Sorry everyone, but unfortunately the dining room will not be available at that time so I can only invite 2 guests.")
remove = guestList.pop(0)
print(f"I am sorry but I will not be able to invite you to dinner {remove.title()}. ")
remove = guestList.pop(-1)
print(f"I am sorry but I will not be able to invite you to dinner {remove.title()}. ")
remove = guestList.pop(-2)
print(f"I am sorry but I will not be able to invite you to dinner {remove.title()}. ")
remove = guestList.pop(-3)
print(f"I am sorry but I will not be able to invite you to dinner {remove.title()}. ")
print(guestList)
print(f"You are invited to my dinner still {guestList[0]}!")
print(f"You are invited to my dinner still {guestList[1]}!")