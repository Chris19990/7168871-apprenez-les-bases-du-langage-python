def main():
   # Instructions
   nombre_a_gauche = input("Entrez un nombre entier:")
   nombre_a_droite = input("Entrez un nombre entier:")
   operateur = input ("Entrez l'operateur souhaité['+','-','*','/']:")
   resultat = 0
if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
else:
    nombre_a_gauche = int(nombre_a_gauche)
    nombre_a_droite =int(nombre_a_droite)   
    match operation:
        case"+":
             resultat: nombre_a_gauche + nombre_a_droite
        case "-":
            resultat : nombre_a_gauche - nombre_a_droite 
        case "*":
            nombre_a_gauche * nombre_a_droite
        case "/": 
            if le nom_a_droite == 0:
                print("Erreur: impossible de divider par 0")
            else:
                resultat : nombre_a_gauche / nombre_a_droite
        case_:
            print("Erreur: l'operateur doit être: '+','-','*','/'.)
    print(f"le resultat de l'operation est:{le resultat}")
    

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()