#ALLOW YOU TO CONNECT PIECES OF INFORMATION

#?A simple dictionary
alien_0={"color":'red','points':65}
print(alien_0['color'])
print(alien_0['points'])
new_alien_0=alien_0['points']
print(f"your got {new_alien_0} points")


#?Adding new key-value pairs
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)


#?Staring with an empty dictionary
empty_alien_0={};
print(empty_alien_0)
empty_alien_0['color']="Black"
empty_alien_0['point']=50
print(empty_alien_0)


#?Modifying values in a dictionary
print(f"The color of this alien is {alien_0['color']}")
alien_0['color']="yellow"
print(f"The new color of this alien is {alien_0['color']}")

#!FUN
alien_spec={'x_position':0,'y_position':25,'speed':'medium'}
print(f"The original speed of this alien is {alien_spec['x_position']}")

if alien_spec['speed']=='slow':
    x_increase=1
elif alien_spec['speed']=='medium':
    x_increase=2
else: x_increase=3
alien_spec['x_position']=alien_spec['x_position']+x_increase
print(f"This alien is {alien_spec['speed']} and its position in X direction is {alien_spec['x_position']}")


#?Removing a key value pair
del alien_0['points']
print(alien_0)


#?A dictionary of similar objects
favourite_languages={
    'john':'C++',
    'Onii-chan':'Go',
    'Leon':'Python'
}
leonLan=favourite_languages['Leon'].upper()
print(f"The favourite language of leon is {leonLan}")


#using keys in brackets to retrieve a value might cause one problem:
#if the value dont exist in the dictionary I'll get an error
#?Using GET() function to access values
#the get method requires a key as a first argument
#as a second argument, you can pass the value to be returned if the key doesn't exist
get_val=alien_0.get("point","no point key, you can pass this method instead")
print(get_val)


#?Looping through all key value pairs
user={
    'name':'Leon',
    'age':18,
    'profession':'students'
}
for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
#the first word after for is key and its indicates KEY in dictionary
#the second word after comma is value and its indicates VALUE in dicionary
#you can use any name instead of key and value
#item() method: returns a sequence of key-value pairs

for name,language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.upper()}")


#?Looping through all the keys in dictionary
#for names in favourite_languages.keys():
    #print(names)
another_names=["Leon","Luffy"]
for names in favourite_languages.keys():
    print(names);
if names in another_names:
    lan=favourite_languages[names].upper()
    print(f"{names}, I see you love {lan}")
if "Luffy" not in favourite_languages.keys():
    print("Luffy, please take our poll!")


#?Looping through a dictionary's keys in a particular order
for namess in sorted(favourite_languages.keys()):#sort them from A to Z
    print(f"{namess}, Thanks for taking the poll!")


#?Looping through all values in a dictionary
favourite_languages['Luffy']='Python'
for lang in favourite_languages.values():
    print(lang)

#*set() method is a collection in which each item must be unique   
for lang in set(favourite_languages.values()):
    print(lang)


#?NESTING
#?A list of dictionaries
alien_1={"color":"white","points":10}
alien_2={"color":"brown","points":20}
alien_3={"color":"black","points":30}
aliens=[alien_0,alien_1,alien_2,alien_3]
print(aliens)
for alien in aliens:
    print(alien)

#!using range() to make a fleet of 10 alien
#Make an empty list for alien
alienn=[];
for al in range(10):
    new_aliens={'color':'red','points':30,'speed':'slow'}
    alienn.append(new_aliens)

for alin in alienn[:5]:
    print(alin)

#modifying the first three item
for alin3 in alienn[0:3]:
    if alin3['color']=='red':
        alin3['color']='black'
        alin3['speed']='medium'
        alin3['points']=10
    #elif alin3['color']=='black':
        #alin3['color']='yellow'
        #alin3['speed']='fast'
        #alin3['points']=5   
        #print(alin3)

for alien5 in alienn[:5]:
    print(f"\n{alien5}")


#?A list in a dictionary 
pizza={
    'crust':'thick',
    'toppings':["extra cheese","pineapple","mushrooms"]
}
print(f"You ordered a {pizza['crust']}-crust pizza")
for topp in pizza['toppings']:
    print(f"\t{topp}")

fav_lan={
    'leon':["Python","Go"],
    'lein':["c++","ruby"],
    'loid':["javascript"],
    'anya':["html","css"]
}
for n,l in fav_lan.items():
    print(f"{n.title()}");
    for l1 in l:
        print(f"Your favourite language is {l1.upper()}")


#?A dictionary in a dictionary
user={
    'user0':{
        'first':"leon",
        'age':18
    },
    'user1':{
        'first':"luffy",
        'age':21
    }
}
for un,ui in user.items():
    #print(un,ui)
    print(f"hello {un}")
    fullname=f"{ui['first']}"
    print(f"Your name is {fullname}")
    print(f"And you are {ui['age']} years old.")
