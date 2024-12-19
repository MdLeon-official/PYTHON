
#?if you wanna work with a part of list, first you have to slice that part
laptop=["hp","lenovo","asus","acer","msi","dell"]
print(laptop[0:3])#in this syntax you can see the value of 0,1,2
print(laptop[1:4])#1,2,3
print(laptop[:4])#without a start index, python starts from the beginning- 0,1,2,3
print(laptop[2:])#2,3,4,5....
print(laptop[-2:])#print the last two item
#you can use loop to print the slice part
for lp in laptop[1:4]:
    print(lp)


#?Copying a List
#to copy a list, you can make a slice that includes the entire original list by omitting the first index and the 2nd index [:]
myLp=laptop[:]
myLp.append("leon")
print(myLp)


#?TUPLES: a list of item that cannot change called an immutable
#use 1st bracket instead of 3rd bracket
strHat=("luffy","zoro","sanji","jimbei")
print(strHat)
print(strHat[1])
#if you want to define a tuple in one element you need to include a trailing comma
tt=(3,)

#looping through all values in a tuple
for hat in strHat:
    print(hat)

#writing over a tuple
dimensions=(200,50)
print("original dimensions")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)

pp=(1,2,3,4)
print(pp)
pp=(3,54,3,5,3)
print(pp)