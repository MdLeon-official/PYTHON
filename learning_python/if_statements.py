
#?work with any item
chars=["luffy","naruto","goku","ichigo"]
for char in chars:
    if char=="goku":
        print(char.upper())
    else:
        print(char.title())

#*Testing for equality is case sensitive in python
#can write like this: cars.lower()=="audi"

#?Testing for inequality
name="leon"
if name != "luffy":
    print(f"You are right, my name is {name}")

#?Numerical comparisons
#age =  18 --- age<21=true, age<=21=true, age>21=false, age>=21=false

#?Using and to check multiple condition
age=18;
if age < 21 and age>15 and age==18 and age <=20:
#if (age < 21) and (age>15) and (age==18) and (age <=20): #*to improve readability you can use parentheses around the individual tests
    print("Congratulations, You are good to go.")
else: print("Sorry, you are not eligible.")

#?Using or to check multiple condition
ageOr=18;
if ageOr > 21 or ageOr<=15 or ageOr==18 or ageOr >=20:
#if (ageOr < 21) or (ageOr>15) or (ageOr==18) or (ageOr <=20): #*to improve readability you can use parentheses around the individual tests
    print("Congratulations, You are good to go. example or")
else: print("Sorry, you are not eligible. example or")

#?Checking weather a value is in a list
big3=["One piece","Naruto","Bleach"]
a='Naruto' in big3
b='Gintama' in big3
print(a,b)
if 'One piece' in big3:
    print("One piece is the best in BIG THREE")
else: print("Something is wrong")

#?The if-elif-else chain
mark=100;
if mark <=33:
    print("You are a failure")
elif 33<mark<=50:
    print("You are still a failure")
elif 50<mark<=80:
    print("Kinda good but still a failure")
elif 80<mark<=99:
    print("Not bad. But try more.")
else: print("Good job")
#you can do like this
agee=65
if 0<agee<=12: price=0
elif 12<agee<=18:price=50
else: price=100
print(f"You are {agee} years old. So the price for you is {price}")


#?Testing multiple conditions
big33=["One piece","Naruto","Bleach"]
if 'One piece' in big33: print("One piece  is the best anime")
if 'gintama' in big33: print("Gintama is the best anime of all time")
else: print("adding extra drama")

#*If you want only one block of code to run, use an if-elif-else chain.
#*If more than one block of code needs to run, use a series of independent if statements.


#?Using if statements with lists
pizzas=["mushrooms","pineapples","extra cheese"]
for pizza in pizzas:
    if pizza=="pineapples":
        print("Sorry, we are our of pineapples.")
    else:
        print(f"Adding {pizza}")


#?Checking that list is not empty
requested_pizzas=[];
if requested_pizzas:
#when the name of a list used in if statements, python returns true if the list contains at least one item
#an empty list evaluates to false
    for requested_pizza in requested_pizzas:
        print(f"Adding {requested_pizza}")
else: print("Are you sure you want a plain pizza?")


#?Using multiple lists
available_toppings=["mushrooms","pineapples","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings=["mushrooms","green peppers","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:print("Sorry, the toppings you requested in currently not available.")
print("\nYour pizza is done")