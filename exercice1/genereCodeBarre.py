import random


def calculer_chiffre_controle(code):
    """Calculer le chiffre de contrôle pour un code-barres de 12 chiffres."""
    digits = [int(digit) for digit in code]
    somme_impaire = sum(digits[i] for i in range(0, 12, 2))
    somme_pair = sum(digits[i] for i in range(1, 12, 2)) * 3
    total = somme_impaire + somme_pair
    return (10 - (total % 10)) % 10


def generate_valid_barcode():
    """Générer un code-barres valide de 13 chiffres."""
    code_pays = str(random.choice([300, 400, 600, 750, 890]))  # Codes pays valides
    code_fabricant = str(random.choice(["12345", "40012", "30078", "60123", "01234"]))  # Fabricant aléatoire
    code_produit = str(random.randint(1000, 9999)).zfill(4)  # Produit aléatoire

    code_sans_chiffre_controle = code_pays + code_fabricant + code_produit

    chiffre_controle = calculer_chiffre_controle(code_sans_chiffre_controle)

    return code_sans_chiffre_controle + str(chiffre_controle)


valid_file_path = 'codes_barres_a_verifier.txt'

valid_codes_barres = [generate_valid_barcode() for _ in range(10)]

# Écriture des codes-barres valides dans le fichier
with open(valid_file_path, 'w') as f:
    for code in valid_codes_barres:
        f.write(f"{code}\n")

print(f"Fichier créé : {valid_file_path}")
