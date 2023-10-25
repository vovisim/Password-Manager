from random import shuffle, choice, randint



def GenerationPass(passlen=16, dot= True, SpecialCharacters= True):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    special_characters = ["#", "%", "$", "!", "?"]

    passlen1 = 0
    prepass = []
    passs = ""


    if dot == True:
        prepass.append(".")
    if SpecialCharacters == True:
        for i in range(round(passlen / 8)):
            s = str(choice(special_characters))
            prepass.append(s)
    while len(prepass) != passlen:
        if passlen1 % 2 == 0:
            prepass.append(choice(numbers))
        else:
            n = str(choice(alfabet))
            if randint(0, 1) == 0:
                n = n.upper()
            prepass.append(n)
        passlen1 +=1

    shuffle(prepass)

    passs ="".join(str(el) for el in prepass)

    return passs



print(GenerationPass())
















