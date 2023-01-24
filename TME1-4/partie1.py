def read_pref_etu(file_path:str):
    file_etu = open(file_path, "r")
    content = file_etu.readlines()  
    file_etu.close()
    content = content[1:]
    for line in range(len(content)):
        content[line]=content[line].split()[2:]
        for column in range(len(content[line])):
            content[line][column]=int(content[line][column])
    return content

def read_pref_spe(file_path:str):
    file_spe = open(file_path, "r")
    content = file_spe.readlines()  
    file_spe.close()
    capacity = content[1].split()[1:]
    content = content[2:]
    for line in range(len(content)):
        content[line] = [capacity[line]]+content[line].split()[2:]
        for column in range(len(content[line])):
            content[line][column] = int(content[line][column])
    return content

def hospital_algorithm(mat_patient,mat_hospital):
    list_patient_free = [i for i in range(len(mat_patient))] # La liste que contient les internes libres
    list_next_patient_choice = [0 for i in range(len(mat_patient))] # list_next_patient_choice[patient] : le prochain hôpital choisi par l'interne
    list_hospital = [[] for i in range(len(mat_hospital))] # L'affectation des internes
    while len(list_patient_free) != 0:
        patient = list_patient_free[0]
        hospital = mat_patient[patient][list_next_patient_choice[patient]]
        if len(list_hospital[hospital]) < mat_hospital[hospital][0]: # Si H n’a pas encore atteint sa capacité max
            list_hospital[hospital].append(patient)
            list_patient_free.pop(0)
        else:
            patient_compared = list_hospital[hospital][-1]
            if mat_hospital[hospital][1:].index(patient) < mat_hospital[hospital][1:].index(patient_compared): # Si H préfère I à I′
                list_patient_free.pop(0)
                list_patient_free.append(patient_compared)
                list_hospital[hospital][-1] = patient
        list_next_patient_choice[patient] += 1
    return list_hospital

def hospital_algorithm_Hoptimized(mat_patient,mat_hospital):
    list_next_hospital_choice = [1 for i in range(len(mat_hospital))] # list_next_hospital_choice[hospital] : la prochaine interne choisi par l'hôpital
    list_patient_free = [i for i in range(len(mat_patient))] # La liste que contient les internes libres
    list_hospital_free = [i for i in range(len(mat_hospital))] # La liste que contient les hôpitals libres
    list_hospital = [[] for i in range(len(mat_hospital))] # L'affectation des internes
    while len(list_hospital_free) != 0:
        hospital = list_hospital_free[0]
        patient = mat_hospital[hospital][list_next_hospital_choice[hospital]]
        if patient in list_patient_free: # Si l'interne est libre aussi
            list_patient_free.remove(patient)
            list_hospital[hospital].append(patient)
            if len(list_hospital[hospital]) == mat_hospital[hospital][0]:
                list_hospital_free.remove(hospital)
        else:
            hospital_compared = -1
            for i in range(len(list_hospital)):
                if patient in list_hospital[i]:
                    hospital_compared = i
                    break
            if mat_patient[patient].index(hospital) < mat_patient[patient].index(hospital_compared):
                list_hospital[hospital].append(patient)
                if len(list_hospital[hospital]) == mat_hospital[hospital][0]:
                    list_hospital_free.remove(hospital)
                list_hospital[hospital_compared].remove(patient)
                if hospital_compared not in list_hospital_free:
                    list_hospital_free.append(hospital_compared)
        list_next_hospital_choice[hospital] += 1
    return list_hospital





def stability_verification(assignment,mat_patient,mat_hospital):
    """
    Nous comparons toutes les combinaisons de (patient, hôpital) et vérifions si c'est instable
    """
    for patient in range(len(mat_patient)):
        for hospital in range(len(mat_hospital)):
            if patient in assignment[hospital]:
                continue
            hospital2 = -1
            for i in range(len(assignment)):
                if patient in assignment[i]:
                    hospital2 = i
                    break
            patients2 = assignment[hospital]
            for patient2 in patients2:
                if mat_hospital[hospital][1:].index(patient) < mat_hospital[hospital][1:].index(patient2) and mat_patient[patient].index(hospital) < mat_patient[patient].index(hospital2):
                    return False
    return True

