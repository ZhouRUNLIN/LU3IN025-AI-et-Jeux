import random

def generatePreferencesEtu(n):
    ls=[]
    for i in range(n):
        l=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(l)
        ls.append(l)
    return ls

def generatePreferencesParcours(n):
    ls=[]
    for i in range(9):
        l=[]
        for j in range(n):
            l.append(j)
        random.shuffle(l)
        ls.append(l)
    return ls

#test
n=50
print(generatePreferencesEtu(50))
print(generatePreferencesParcours(50))