import partie1
import partie2

def generate_pl_egalitarian_criterion(pref_etu,pref_spe,k:int):
    n_etu = len(pref_etu)
    n_spe = len(pref_spe)
    f = open(str(k)+"-premier_choix.lp","w+")
    f.write("Minimize"+"\n") #Minimize
    # generate the object to be minimized
    str_temp = ""
    for i in range(n_etu):
        for j in range(n_spe):
            str_temp += str(n_spe-pref_etu[i].index(j)-1)+" "+"c"+str(i)+"_"+str(j)+" + "+str(n_etu-pref_spe[j][1:].index(i)-1)+" "+"c"+str(i)+"_"+str(j)+" + "
    str_temp = str_temp[0:-3]
    f.write(str_temp+"\n") #Σij cij(jmax-j + imax-i)
    f.write("Subject To"+"\n")
    # part ST
    res_count = 1
    for i in range(n_etu):
        str_temp1 = "c"+str(res_count)+": "
        str_temp2 = "c"+str(res_count+1)+": "
        res_count += 2
        for j in range(n_spe):
            if pref_etu[i].index(j)<k:
                str_temp1 += "c"+str(i)+"_"+str(j)+" + "
            else:
                str_temp2 += "c"+str(i)+"_"+str(j)+" + "
        str_temp1 = str_temp1[0:-3]+" = 1"
        str_temp2 = str_temp2[0:-3]+" = 0"
        f.write(str_temp1+"\n")
        f.write(str_temp2+"\n")
    
    for j in range(n_spe):
        str_temp1 = "c"+str(res_count)+": "
        str_temp2 = "c"+str(res_count+1)+": "
        res_count += 2
        for i in range(n_etu):
            if pref_spe[j][1:].index(i)<k:
                str_temp1 += "c"+str(i)+"_"+str(j)+" + "
            else:
                str_temp2 += "c"+str(i)+"_"+str(j)+" + "
        str_temp1 = str_temp1[0:-3]+" = "+str(pref_spe[j][0])
        str_temp2 = str_temp2[0:-3]+" = 0"
        f.write(str_temp1+"\n")
        f.write(str_temp2+"\n")
    
    f.write("Bounds"+"\n")
    # part Bounds
    for i in range(n_etu):
        for j in range(n_spe):
            f.write("0 <= "+"c"+str(i)+"_"+str(j)+" <= 1"+"\n") #我想写只在0和1之间选的但是不知道怎么写，所以先写属于[0,1]了
    
    f.write("Binary"+"\n")
    # part Binary
    str_temp = ""
    for i in range(n_etu):
        for j in range(n_spe):
            str_temp += "c"+str(i)+"_"+str(j)+" "
    f.write(str_temp[0:-1]+"\n")

    f.write("End"+"\n")