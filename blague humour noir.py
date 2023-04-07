import random

blagues_string = open("Stats/blagues.txt", "r", 1, "UTF-8").read()
blagues_list = []
counter = 1


for i in range(len(blagues_string)):
    if blagues_string[i] == str(counter):
        blagues_list.append(blagues_string[i+1:blagues_string.find("|", i+1)])
        counter = (counter + 1) % 9

def blague():
    print(blagues_list[random.randint(0, len(blagues_list)-1)])
