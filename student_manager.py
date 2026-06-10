etudiants =[]
def ajouter_etudiant():
    Nom =input("Nom de l'etudiant:")
    note1 =float(input("note1:"))
    note2 =float(input("note2:"))
    note3 =float(input("note3:"))
    moyenne = ( note1+ note2+note3)/3
    etudiant = {
       "Nom" : Nom,
       "noteS":[note1, note2, note3],
       "moyenne":moyenne
    }
    etudiants.append(etudiant)
    print (" etudiant ajouté!")
def voir_etudiants():
    if len(etudiants)==0:

        print("aucun étudiant enregistré.")
    else:
        for e in etudiants:
         print("--------")
        print("Nom:",e["Nom"])
        print("moyenne",e["moyenne"])
def voir_resultats():
        for e in etudiants:
            if e ["moyenne"]>=10:
                print(e["Nom"],"->ADMIS")
            else:
                print(e["Nom"],"->recalé")
while True:
        print("\n===STUDENT MANAGER===")
        print("1.Ajouter un étudiant")
        print("2.voir tous les étudiants")
        print("3.voir les résultats")
        print("4.Quitter")
        choix = input ("ton choix:")
        if choix =="1":
            ajouter_etudiant()
        elif choix =="2":
             voir_etudiants()
        elif choix =="3":
             voir_resultats()
        elif choix =="4":
            print("au revoir!")
            break
        else:
            print("choix invalide!")

