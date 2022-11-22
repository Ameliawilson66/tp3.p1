#amelia wilson
#401

import random

def jeu():
    ndv = 20
    print("niveau de vie" + str(ndv))
    nombre_de_victoires = 0
    nombre_de_defaites = 0

    while True:
        fadv = random.randint(1, 6)
        #quand le niveau de vie du jeur est a 0, il perd et le jeu recommence
        if ndv == 0:
            lost = input("vous avez perdu! voulez-vous commencer une nouvelle partie? oui/non: ")
            if lost == "oui":
                jeu()
            if lost == "non":
                exit()

        print("force de l'adversaire: " + str(fadv))
        choix = input("""que voulez-vous faire?: 
        1: combattre
        2: essayer une autre porte
        3: afficher les règles du jeu
        4: quitter
        
        option(#): """)

        if choix == "1":
            #rdd1 = roulage de dés 1: la force de l'attaque du joueur
            rdd1 = random.randint(1, 6)
            print("force de l'adversaire" + str(fadv))
            print("force de votre attaque" + str(rdd1))
            if fadv < rdd1:
                ndv += fadv
                print("victoire! votre niveau de vie augmente de " + str(fadv))
                print("niveau de vie: " + str(ndv))
                nombre_de_victoires += 1
                print("nombre de victoires: " + str(nombre_de_victoires))
                print("nombres de défaites: " + str(nombre_de_defaites))

            elif fadv > rdd1:
                ndv -= fadv
                print("défaite! vous avez perdu " + str(fadv) + " points de vie")
                print("niveau de vie: " + str(ndv))
                nombre_de_defaites += 1
                print("nombre de victoires: " + str(nombre_de_victoires))
                print("nombres de défaites: " + str(nombre_de_defaites))

            elif fadv == rdd1:
                print("égalité! réessayez")

        if choix == "2":
            ndv -= 1
            print("vouz avez une pénalité de 1 point de vie en faisant cette action")
            print("niveau de vie: " + str(ndv))

        if choix == "3":
            input("""Vous ouvrez la porte à un monstre:
            
            Si vous décidez de le combattre: vous roulez un dés, ce qui décidera la force de votre attaque.
                                             Si votre niveau d'attaque est supérieur à celui du monstre, vous gagner 
                                             ses points de vie.
                                             Si votre niveau d'attaque est inférieur à celui du monstre, vous perdez
                                             des points de vie selon l'attaque du monstre.
                                             
                                             Une nouvelle rencontre avec un nonstre recommencera automatiquement.
            Si vous décidez de le l'éviter, vous avez une pénalitéde de 1 point de vie. Une nouvelle rencontre avec un nonstre recommencera automatiquement.
            
            La partie se termine lorsque vous décidez de quitter ou lorsque vous avez 0 point de vie
            
            
            Cliquez ENTER pour continuer le jeu""")

        if choix == "4":
            leave = input("voulez-vous quitter la partie? oui/non: ")
            if leave == "non":
                jeu()
            if leave == "oui":
                exit()

        else:
            print("Ceci n'est pas un des choix. Veuillez appuyer sur ENTER pour réessayer")

jeu()