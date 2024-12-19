#EXERCISE page 41
#**3.4- guest list:
guestName=["Luffy","Zoro","Jimbei"]
print(f"Hello {guestName[0]}. You are invited")
print(f"Hello {guestName[1]}. You are invited")
print(f"Hello {guestName[2]}. You are invited")
print(guestName)

#**3.5- Changing guest list
print(f"Sorry {guestName[2]} cant make it to our invitation")
guestName.remove("Jimbei")
guestName.append("Sanji")
print(guestName)
print(f"Hello {guestName[0]}. You are invited")
print(f"Hello {guestName[1]}. You are invited")
print(f"Hello {guestName[2]}. You are invited")

#**3.6- More guest
print(f"I found a new big table")
guestName.insert(0,"Nami")
guestName.insert(1,"Robin")
guestName.append("Brook")
print(guestName)
print(f"Hello {guestName[0]}. You are invited")
print(f"Hello {guestName[1]}. You are invited")
print(f"Hello {guestName[2]}. You are invited")
print(f"Hello {guestName[3]}. You are invited")
print(f"Hello {guestName[4]}. You are invited")
print(f"Hello {guestName[5]}. You are invited")

#**3.7- Shrinking the guest
print("Sorry guys. my diner table wont arrive in time so I can only invite two people")
brook="Brook"
guestName.pop()
print(f"Sorry {brook} you are already dead.")
sanji="Sanji"
guestName.pop()
print(f"Sorry {sanji} you are a pervert.")
zoro="Zoro"
guestName.pop()
print(f"Sorry {zoro} you only eat riceballs.")
luffy="Luffy"
guestName.pop()
print(f"Sorry {luffy} you are a monster eater.")
print(f"Hello {guestName[0]}. You are invited")
print(f"Hello {guestName[1]}. You are invited")
print(guestName)
del guestName[0]
print(guestName)
#del guestName[1]
#print(guestName)


#EXERCISE page- 45
#**3.8- seeing the world
places=["japan","switzerland","greek","bangladesh","china"]
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
print(sorted(places))
places.reverse()
print(places)
places.sort()
print(places)
places.reverse()
print(places)

#**3.9- dinner guests
guestLen=len(guestName)
print(guestLen)


#!USING EACH FUNCTIONS INTRODUCED IN THIS CHAPTER
bdplaces=["barisal","jashore","dhaka","rajhshahi","bogra","noakhali","sylet","khulna"]
print(bdplaces)

bdplaces.append("netrokona")
print(bdplaces)

bdplaces.insert(4,"tangail")
print(bdplaces)

del bdplaces[5]
print(bdplaces)

pp=bdplaces.pop(4)
bdplaces.pop(4)
print(bdplaces)
print(pp)

byeNet='netrokona'
bdplaces.remove(byeNet)
print(f"{byeNet} has been romoved from the list.")
print(bdplaces)

bdplaces.sort()
print(bdplaces)

bdplaces.reverse()
print(bdplaces)

print(sorted(bdplaces))

lenBdp=len(bdplaces)
print(lenBdp)