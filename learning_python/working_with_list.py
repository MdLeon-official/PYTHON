
#?if you want to do the same work with each item on a list, use for loop
tanks=["belerick","hylos","lolita","tigreal","minataur","atlas"];
for tank in tanks:
    print(tank)
    print(f"{tank} you are great") 


#?Making Numerical List
#range(): makes it easy to generate a series of number
for numbers in range(1,6):
    print(numbers)
print("Another way to use range() function")
for another in range(6):
    print(another)

#If you want to make a list of many numbers:
numberList=list(range(1,21))
print(numberList)

#we can also use range function to give deference between two numbers
numberListDiff=list(range(1,21,2));#*the last given value indicates how much difference we want between numbers
print(numberListDiff)

#if you want make a list of squre number of the first 10 numbers
square=[];
for sq in range(1,11):
    sqVal=sq**2
    print(sqVal)
    square.append(sqVal);
print(square)
#!or
square2=[];
for sq2 in range(21,41):
    square2.append(sq2**2);
print(square2)

#finding the minimum maximum and sum values in a list
finNum=list(range(0,201,10))
print(finNum)
a=min(finNum)
b=max(finNum)
c=sum(finNum)
print(a,b,c)


#?List Comprehensions: alows to generate the same list in just one lines of code
#a list comprehensions combines the for loop and the creation of new elements in just one line of code
squreCom=[valuesCom**2 for valuesCom in range(1,6)]
print(f"This is just a simple example of List Comprehensions {squreCom}")
