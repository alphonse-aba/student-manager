class Etudiant:
    def __init__(self, nom, note1, note2, note3):
        self.nom = nom
        self.notes = [note1, note2, note3]
        self.moyenne = (note1 + note2 + note3) / 3

    def afficher(self):
        print("--------")
        print(f"Nom     : {self.nom}")
        print(f"Notes   : {self.notes}")
        print(f"Moyenne : {self.moyenne:.2f}")

    def est_admis(self):
        if self.moyenne >= 10:
            print(f"{self.nom} -> ADMIS ✓")
        else:
            print(f"{self.nom} -> RECALÉ ✗")


# Liste des étudiants
etudiants = []

def ajouter_etudiant():
    nom = input("Nom de l'étudiant : ")
    try:
        note1 = float(input("Note 1 : "))
        note2 = float(input("Note 2 : "))
        note3 = float(input("Note 3 : "))
        e = Etudiant(nom, note1, note2, note3)  # on crée un objet
        etudiants.append(e)
        print("Étudiant ajouté !")
    except ValueError:
        print("erreur!entre un nombre!")
        return

def voir_etudiants():
    if len(etudiants) == 0:
        print("Aucun étudiant enregistré.")
    else:
        for e in etudiants:
            e.afficher()          # on appelle la méthode

def voir_resultats():
    if len(etudiants) == 0:
        print("Aucun étudiant enregistré.")
    else:
        for e in etudiants:
            e.est_admis()         # on appelle la méthode

# Menu principal
while True:
    print("\n=== STUDENT MANAGER ===")
    print("1. Ajouter un étudiant")
    print("2. Voir tous les étudiants")
    print("3. Voir les résultats")
    print("4. Quitter")
    choix = input("Ton choix : ")

    if choix == "1":
        ajouter_etudiant()
    elif choix == "2":
        voir_etudiants()
    elif choix == "3":
        voir_resultats()
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Choix invalide !")
    

