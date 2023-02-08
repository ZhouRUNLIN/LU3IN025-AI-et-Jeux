import partie1
import partie2
import partie3

pref_etu = partie2.generate_pref_etu(11)
pref_spe = partie2.generate_pref_spe(11)
print(partie3.find_minimum_k(pref_etu, pref_spe, False, True))
partie3.generate_pl_egalitarian_criterion(pref_etu,pref_spe,6,True)
