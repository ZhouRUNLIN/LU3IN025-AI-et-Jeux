import partie1
import random
import time

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
        pref_spe[random.randint(0,8)][0] += 1
    return pref_spe

def analyse_running_time_HA(n:int):
    pref_etu = generate_pref_etu(n)
    pref_spe = generate_pref_spe(n)
    print(pref_etu)
    print(pref_spe)
    time_passed = time.time()
    assignment = partie1.hospital_algorithm(pref_etu,pref_spe)
    time_passed = time.time() - time_passed
    print(assignment)
    assert partie1.stability_verification(assignment,pref_etu,pref_spe)
    return time_passed

