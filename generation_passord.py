from random import randint as rand

l = "F9l25LA$E"
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alfabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = "#, %, &, !, ?"

for i in l:
    print(ord(i))


def GenerationPass(passlen=8, dot="True", SpecialCharacters="False"):

