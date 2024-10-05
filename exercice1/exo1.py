import os
import sys


class CodeBarre:
    def __init__(self, codeBarre):
        if len(codeBarre) !=13:
            raise ValueError("Le code barre doit contenir 13 caractères.")

        self.codePays = codeBarre[0:3]
        self.codeFabricant = codeBarre[3:8]
        self.codeProduit = codeBarre[8:12]
        self.codeStatut = codeBarre[12]

    def __str__(self):
        return f"Le codeBarre est {self.codePays}_{self.codeFabricant}_{self.codeProduit}_{self.codeStatut}"

    def decode_pays(self):
        decodePays = int(self.codePays)
        if 0 < decodePays < 19:
            return f"Etats-Unis"
        elif 299 <= decodePays <= 379:
            return f"France"
        elif 400 <= decodePays <= 440:
            return f"Allemagne"
        elif 600 <= decodePays <= 603:
            return f"Afrique du sud"
        elif decodePays == 750:
            return f"Mexique"
        elif decodePays == 890:
            return f"Inde"
        elif decodePays == 489:
            return f"Hong-Kong"
        else:
            return f"Le code pays de ce produit n'est pas reconnu"

    def decode_fabricant(self):
        if self.codeFabricant == "12345":
            return f"Fab A"
        elif self.codeFabricant == "40012":
            return f"Fab B"
        elif self.codeFabricant == "30078":
            return f"Fab C"
        elif self.codeFabricant == "60123":
            return f"Fab D"
        elif self.codeFabricant == "01234":
            return f"Fab E"
        else:
            return f"Le code fabricant n'est pas valide"

    def verif_statut(self):
       # numeros = [int(numero) for numero in self.codePays + self.codeFabricant + self.codeProduit]
       numeros = []
       for numero in self.codePays + self.codeFabricant + self.codeProduit:
           numeros.append(int(numero))
       somme_impaire = sum(numeros[i] for i in range(0,12,2))
       somme_paire = sum(numeros[i] for i in range(1,12,2))*3
       total = somme_paire + somme_impaire
       chiffre_controle = (10 - (total % 10)) % 10

       return chiffre_controle == int(self.codeStatut)


def lire_et_verifier_codeBarre(fichier_entree, fichier_code_valide, fichier_code_erreur):
    try:
        with open(fichier_entree, 'r') as f_in, \
                open(fichier_code_valide, "w") as f_valide, \
                open(fichier_code_erreur, 'w') as f_erreur:

            for ligne in f_in:
                code_barre = ligne.strip()
                if code_barre:
                    try:
                        print(f"Traitement du code-barres : {code_barre}")  # Debug
                        produit = CodeBarre(code_barre)
                        provenance = produit.decode_pays()
                        fabricant = produit.decode_fabricant()
                        statut = produit.verif_statut()

                        erreurs = []
                        if "n'est pas reconnu" in provenance:
                            erreurs.append("Provenance INVALIDE")
                        if "n'est pas valide" in fabricant:
                            erreurs.append("Fabricant INVALIDE")
                        if not statut:
                            erreurs.append("Statut code-barre INVALIDE")

                        if not erreurs:
                            f_valide.write(f"{code_barre} :\n Provenance: {provenance}\n Fabricant: {fabricant}\n Statut: VALIDE\n")
                            print(f"Code-barres valide : {code_barre}")  # Debug
                        else:
                            #
                            erreur_msg = ", ".join(erreurs)
                            f_erreur.write(f"{code_barre} : {erreur_msg}\n")
                            print(f"Code-barres invalide : {code_barre} - {erreur_msg}")  # Debug

                    except ValueError as e:
                        print(f"Erreur avec le code-barres '{code_barre}': {e}")  # Debug
                        f_erreur.write(f"Erreur avec le code-barres '{code_barre}': {e}\n")

    except FileNotFoundError:
        print(f"Le fichier '{fichier_entree}' n'existe pas.")

def main():
    codebarre = CodeBarre("6001234599746")
    print(codebarre.decode_pays())
    #fichier_tous_codes = 'codes_barres_a_verifier.txt'
    #fichier_codes_valides = "C:/Users/herma/Downloads/codes_barres_valides.txt"
    #fichier_codes_invalides = "C:/Users/herma/Downloads/codes_barres_erreur.txt"
    if len(sys.argv) < 4:
        print("Erreur : Vous devez fournir trois arguments : fichier entrée, fichier validé, fichier erreur.")
        return

    fichier_tous_codes = sys.argv[1]
    fichier_codes_valides = sys.argv[2]
    fichier_codes_invalides = sys.argv[3]
    print("Début du traitement...")  # Debug
    lire_et_verifier_codeBarre(fichier_tous_codes, fichier_codes_valides, fichier_codes_invalides)
    print("Fin du traitement.")  # Debug

if __name__ == "__main__":
    main()


