from random import shuffle, choice, randint

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alfabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ["#, %, &, !, ?"]

def GenerationPass(passlen=8, dot="True", SpecialCharacters="False"):
    passlen1 = passlen
    if SpecialCharacters == False:
        lenspecial = 0
        if passlen % 2 != 0:
            passlen1 -= 1
    elif passlen % 2 == 0:
        lenspecial = 2
        passlen1 -= 2
    else:
        lenspecial = 1
        passlen -= 1
    prepass = []
    for i in passlen1//2:
        prepass.append(choice(numbers))
    for i in passlen1//2:
        prepass.append(choice(alfabet))
    if dot == True:
        prepass.append(".")
        lenspecial -= 1

    for i in lenspecial:
        prepass.append(choice(special_characters))

    if len(prepass) > passlen:
        prepass.pop
    return prepass

print(GenerationPass(8, True, False))







