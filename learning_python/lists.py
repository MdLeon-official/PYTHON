#In python, square brackets indicate a list and individual elements in this list are seperated by commas
strawhats=["luffy","zoro","nami","ussop","sanji","chopper","robin","franky","brook","jimbei"]
print(strawhats)

#to print only one item from the list
print(strawhats[4])
print(strawhats[0].title())

#to get the last item from a list use index -1
print(strawhats[-1])
print(strawhats[-5].upper())

#using f string
print(f"The name of my favourite character form One Piece is {strawhats[4].title()}")

#to change an element, use the name of the list followd by the index of th eelement you want to change and then provie the new value you want that item to have
strawhats[2]="bonny"
print(strawhats)

#to add a new item to the list use appent(value)
strawhats.append("nami")
print(strawhats)

#you can add any elememt in any position using insert(index, "value") method
strawhats.insert(4, "bon chan")
print(strawhats)

#using del method to remove element from an list
nardo=["Naruto","Sasuke", "Sakura"]
print(nardo)
del nardo[2]
print(nardo)

#the pop method remove the last item in a list but it lets you work with that item after removing it
animals=["cats","dogs","snake","tiger","lion","human"]
newAnimal=animals.pop()#*if you print newAnimal now you can see the last value from the list which was removed
print(animals)
print(newAnimal)
#pop method not only can remove from the last also can remove item from any posititon- just give the index
rem2animal=animals.pop(1)
print(animals)
print(rem2animal)

#if you want to remove an item via value use remove()
#the remove method only deletes the first occurrence of the value you specify. if theres a possibility the value appears more than once youll need to use a loop to make sure all the occurrences of the value are removed
print(strawhats)
llcon="bonny"
strawhats.remove(llcon);
print(strawhats)
print(f"{llcon} can't be a strawhat cause she is a loli")
#!strawhats.remove("bonny")
#!print(strawhats)

#organizing a list : sorting a list permanently with SORT() method
cars=["audi","lamborgini","bmw","toyota"] #SORT() method alphabetically organize the list
print(cars)
cars.sort()
print(cars)

#***sorting a list alphabetically is a bit more complicated when all the values are not in lowercase

#organizing a list : sorting a list temporarily with SORT() method
anime=["naruto","pokemon","toradora","bleach","jjk"]
print(anime)
print(sorted(anime))

#printing a list in reverse order- REVERSE() method
anime.reverse()
print(anime)

#finding the length of a list
l1=len(cars)
l2=len(strawhats)
l3=len(animals)
l4=len(anime)
print(l1, l2, l3, l4)
