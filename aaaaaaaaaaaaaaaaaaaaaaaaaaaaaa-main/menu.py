import n_class
import random
adatok = []
válaszok = ["azmegmicsodaaaa??!","ammeg mi?? ?","Tesó te ismerz ilyet?","Nem létezik","Öcskösöm jól tetszel vagy?","Te meg mit hiszel?","Valami létezőt"]

def inputFile(file):
    f = open(file,"r")
    for sor in f:
        sor = sor[:-1].split(";")
        példány = n_class.Nevezetességek(sor[0],sor[1],sor[2],sor[3])
        adatok.append(példány)

    f.close()
           
def menu():


    print("[1]Minden adat kiírása")
    print("[2]Érdekelt ország kiírása")
    print("[3]Érdekelt évszám kiírása")
    print("[0]Kilépés")
    
inputFile("aaa.txt")
menu()
option = int(input("Válassz a lehetőségek közül: "))

while(option!=-1):

    if (option == 1):
        print("\tEgyes évszámok nem valós információt tartalmazhatnak!")

        for i in range(len(adatok)):

            print("\t\n",adatok[i].rekordok())


    elif (option == 2):
        print("\tEgyes évszámok nem valós információt tartalmazhatnak!")


        a = input("\tKérem az érdekelt ország nevét: ")

        found = False
        
        for i in range(len(adatok)):
            
            if a == adatok[i].country:
                print("\t\n",adatok[i].rekordok())
                found = True
                
            elif a == "Románia":
                
                print("\t",random.choice(válaszok))
                
                found = True
                break

            elif a == "Szlovákia":
                print("\t",random.choice(válaszok))
                
                found = True
                break

            elif a == "Ukrajna":
                print("\tMég létezik, de nem sokáig")

                found = True
                break
                

        if found == False:
            print("\tNincs ilyen ország az adatbázisban!")


    elif option == 3:

        a = int(input("\tKérem az érdekelt ország nevét: "))
        found = False

        for i in range(len(adatok)):
            if a == adatok[i].year:
                print("\t\n",adatok[i].rekordok())
                found = True

        if found == False:
            print("\tNincs ilyen évszám az adatbázisban!")
        

    elif (option == 0):
        quit()
        

    else:
        print("Érvénytelen lehetőség.")

    print()
    menu()
    option = int(input("Válassz a lehetőségek közül: "))
