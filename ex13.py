from sys import argv
# read the WYSS section for how to run thisscript, first ,secod,third, =argv
script,first,second,third,fourth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

print("How old are you?", end=' ')
age = input()
print("How much do you like this class?", end=' ')
like = input()
