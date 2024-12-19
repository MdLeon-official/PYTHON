message = "leon islam"
print(message)

#STRINGS in python: anything inside quotes
name= "leon isLam"
print(name.title())
print(name.lower())

#F-STRING: used to using variables in strings -- format for f-string: f"{var1} {var2}"
firstName="Monkey D."
lastName="Luffy"
fullName=f"{firstName} {lastName}"
print(fullName)
print(fullName.title())
print(fullName.lower())
print(fullName.upper())
#you can also use f-string to compose a message and then assign the entire message into a new one
fN=f"Hello, {firstName} {lastName}"
print(fN, fullName.upper())


#Adding whitespace to string with tabs and newlines
#\t : use this to use tab
#\n : use this to create newlines
print("\tPython")
print("Languages: \nPython\nC++\Jaavscript")
print("Languages: \n\tPython\n\tC++\n\tJavascript")


#python can detect extra whitespace and delete that. To do that use RSTRIP() method(remove whitespace from the right side)
#LSTRIP() method(remove whitespace from the left side)
#STRIP() method(remove whitespace both side)
language= "pearl "
print(language)
print(language.rstrip())#this metod only remove whitespaces temporarily
#use this to remove whitespaces permanently
lan=language.rstrip()
print(lan)


#sometimes removing prefixes is important (from url)- to do that use use REMOVEPREFIX(the prefix you want to remove)
randomUrl= "https://google.com"
afterremPrefix=randomUrl.removeprefix('https://')
print(randomUrl)
print(afterremPrefix)


#EXERCISE 1: personal message
ex1name="Eric"
expMss=f"hello {ex1name} would you like to learn some Python today?"
print(expMss)
#EXERCISE 2: famous quotes
quotes= 'Monkey D. Luffy once said, "If you are hungry, eat"'
print(quotes)
#EXERCISE 3: removesuffix
fileExt="index.html"
print(fileExt.removesuffix('.html'))
