ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
list = [42, 'forty-two','Forty-two','forty two','FoRty TwO'," 42 "]
if ans == str(42) or ans == "forty-two" or ans == "Forty-two" or ans == "FoRty TwO" or ans == " 42 " or ans == 'forty two':
    print("yes")
elif "42" in ans:
    print("yes")
else:
    print("no")
