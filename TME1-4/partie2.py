import random

def generate_pref_etu(n:int):
    pref_etu = []
    for i in range(n):
        l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(l)
        pref_etu.append(l)
    return pref_etu

def generate_pref_spe(n:int):
    pref_spe = []
    for i in range(9):
        l = [j for j in range(n)]
        random.shuffle(l)
        pref_spe.append([1]+l)
    for i in range(n-9):
        pref_spe[random.randint(0,9)][0] += 1
    return pref_spe
