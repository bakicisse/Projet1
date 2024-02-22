print("Bonjour")

print()


def Demander_nom(Nom_de_personne):
    Nom_de_personne = ""
    Nom_de_personne = input("Quel est votre nom? ")
    while Nom_de_personne == "":
        Nom_de_personne = input("Quel est votre nom? ")
    return Nom_de_personne


def Demande_age(Nom_de_personne):
    Age_de_personne = 0

    while Age_de_personne == 0:

        try:
            Age_de_personne = int(input(Nom_de_personne + " Quel est votre age? "))
        except:
            print("Vous devez entrer un numbre entier")

        # Age_de_personne=int(input("Quel est votre age? "))
    return Age_de_personne


def Demander_Age_et_nom(Nom, Age):
    print("Bonjour " + Nom + " vous avez " + str(Age))

    print(f"Bonjour {Nom},  vous avez  {Age}")

    print("Bonjour %s,  vous avez  %s" % (Nom, Age))

    print("""
         Vous 
         avez



         """)


Nom_de_personne = "All"

Nom = Demander_nom(Nom_de_personne)

# Nom2=Demander_nom(Nom_de_personne)


Age_de_personne = 10

# Age1=Demande_age(Nom1)
Age = Demande_age(Nom)

Demander_Age_et_nom(Nom, Age)

for i in range(0, 3):
    i = i + 1
    nom = "Nom" + str(i)
    print(nom)

# NbrSimul=int(input("choose the number of simulation you want to perform : "))
# CodeName=str(input("Choose the name of code you want ot run : "))
# Test=0
# while(Test==0):
#     try :
#         print("The number is " +  NbrSimul)
#     except :
#         print(" There are some mistake in your code"  )
#         Test=0
#         NbrSimul=int(input("choose the number of simulation you want to perform : "))
#         NbrSimul=str(NbrSimul)
#     else :
#         print("Code is true")
#         Test=1


# try :
#     print("The number is " +  CodeName)
# except :
#     print(" There are some mistake in your code"  )
# else :
#     print("This is true")