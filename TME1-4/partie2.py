import partie1
import random
import time
import matplotlib.pyplot as plt

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
    time_passed = time.time()
    assignment = partie1.hospital_algorithm(pref_etu,pref_spe)
    time_passed = time.time() - time_passed
    return time_passed

def analyse_running_time_HAHO(n:int):
    pref_etu = generate_pref_etu(n)
    pref_spe = generate_pref_spe(n)
    time_passed = time.time()
    assignment = partie1.hospital_algorithm_Hoptimized(pref_etu,pref_spe)
    time_passed = time.time() - time_passed
    return time_passed

def analyse_running_time_graph(n1:int,n2:int,step:int):
    y1 = []
    y2 = []
    for n_value in range(n1,n2+1,step):
        y1_temp=0
        y2_temp=0
        for index_n in range(10):
            y1_temp += analyse_running_time_HA(n_value)/10.0
            y2_temp += analyse_running_time_HA(n_value)/10.0
        y1.append(y1_temp)
        y2.append(y2_temp)
    x = [i for i in range(n1,n2+1,step)]
    l1 = plt.plot(x,y1,'r--',label="Patient-optimized")
    l2 = plt.plot(x,y2,'b--',label="Hospital-optimized")
    plt.xlabel('n')
    plt.ylabel('running time')
    plt.legend()
    plt.show()
    return None
