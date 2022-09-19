guestList = ['Kobe Bryant', 'Selena Gomez', 'Kylie Jenner']
print(f"You are invited to my dinner {guestList[0]}!")
print(f"You are invited to my dinner {guestList[1]}!")
print(f"You are invited to my dinner {guestList[2]}!")

print(f"Sorry Everyone, {guestList[0]} couldn't make it.")

guestList[0] = "Michael Jordan"
print(f"You are invited to my dinner {guestList[0]}!")
print(f"You are invited to my dinner {guestList[1]}!")
print(f"You are invited to my dinner {guestList[2]}!")

print(f"Hey Everyone, I have found a bigger table and will be adding 3 more people to the guest list.")

guestList.insert(0,'Jack Harlow')
guestList.insert(2,'Jack Paisley')
guestList.insert(4,'Jeniffer Lopez')
print(guestList)

print(f"You are invited to my dinner {guestList[0]}!")
print(f"You are invited to my dinner {guestList[1]}!")
print(f"You are invited to my dinner {guestList[2]}!")
print(f"You are invited to my dinner {guestList[3]}!")
print(f"You are invited to my dinner {guestList[4]}!")
print(f"You are invited to my dinner {guestList[5]}!")
