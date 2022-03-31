import n_class
import random

adatok = []
kiegészítés = []

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
    print("[4]Források: ")
    print("[0]Kilépés")
    
inputFile("aaa.txt")
menu()
option = int(input("Válassz a lehetőségek közül: "))

#-#-#-#-#-#

while option !=-1:

    if option == 1:
        
        print()
        print("\tEgyes évszámok nem valós információt tartalmazhatnak!")
        print("\t\nA kiírt információk Ország - ahhoz tartozó nevezetesség - város - építés/felfedezés/megalapítás éve -sorrendben jelenik meg!")
        
        for i in range(len(adatok)):

            print("\t\n",adatok[i].rekordok())
            
    elif option == 2:

        answer = ["azmegmicsodaaaa??!","ammeg mi?? ?","Tesó te ismerz ilyet?","Nem létezik","Öcskösöm jól tetszel vagy?","Te meg mit hiszel?","Valami létezőt XDD","kys","Tu may giet may","XDDDDDDDDDDDDDD","Lyjasuó camp"]
        
        print()
        print("\tEgyes évszámok nem valós információt tartalmazhatnak!")
        print("\t\nA kiírt információk Ország - ahhoz tartozó nevezetesség - város - építés/felfedezés/megalapítás éve -sorrendben jelenik meg!")

        a = input("\tKérem az érdekelt ország nevét: ")

        found = False
        
        for i in range(len(adatok)):
            
            if a == adatok[i].country:
                
                print("\t\n",adatok[i].rekordok())
                found = True
                
            elif a == "Románia":
                
                print("\t\n",random.choice(answer))
                
                found = True
                break

            elif a == "Szlovákia":
                
                print("\t\n",random.choice(answer))
                
                found = True
                break
                
        if found == False:
            
            print("\t\nNincs ilyen ország az adatbázisban!")
            print()
                        
    elif option == 3:
        
        print()
        print("\tEgyes évszámok nem valós információt tartalmazhatnak!")
        print("\t\nA kiírt információk Ország - ahhoz tartozó nevezetesség - város - építés/felfedezés/megalapítás éve -sorrendben jelenik meg!")

        a = int(input("\tKérem az érdekelt ország nevét: "))
        found = False

        for i in range(len(adatok)):
            if a == adatok[i].year:
                print("\t\n",adatok[i].rekordok())
                found = True

        if found == False:
            
            print("\tNincs ilyen évszám az adatbázisban!")
            print()
            
    elif option == 4:

        print()

        print("\tGugli")
        
    elif option == 0:
        
        quit()
        
    else:
        print("Érvénytelen lehetőség.")
        print()

    print()
    menu()
    option = int(input("Válassz a lehetőségek közül: "))
