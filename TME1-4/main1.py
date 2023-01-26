import partie1

# Partie 1
mat_etu = partie1.read_pref_etu("PrefEtu.txt")
mat_spe = partie1.read_pref_spe("PrefSpe.txt")
assignment = partie1.hospital_algorithm(mat_etu,mat_spe)
assignment2 = partie1.hospital_algorithm_Hoptimized(mat_etu,mat_spe)
print(assignment)
print(assignment2)
print(partie1.stability_verification(assignment,mat_etu,mat_spe))
print(partie1.stability_verification(assignment2,mat_etu,mat_spe))
print(partie1.stability_verification([[5, 3], [4], [1], [8], [10], [0], [9], [7], [6, 2]],mat_etu,mat_spe))
