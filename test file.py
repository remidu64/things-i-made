

filepath = "Stats/test.txt"
file = opw(filepath)
file.write("ceci est un test")

file = opr(filepath)
print(file.read())