from sys import argv

script, filename = argv
# saying to open txt file
txt = open(filename)
# string is printing the txt file
print(f"Here's your file {filename}:")
print(txt.read())

print(f"Here's your file {filename}:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())
