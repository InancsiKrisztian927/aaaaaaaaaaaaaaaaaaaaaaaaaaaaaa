
def menu():
    print("[1]Elsőfokú egyenlet")
    print("[2]Másodfokú egyenlet")
    print("[0]Kilépés")

menu()
option = int(input("Válassz a lehetőségek közül: "))

while(option!=-1):
    if (option == 1):
        print("\tElsőfokú egyenlet (a*x+b=c)")


    elif (option == 2):
        print("\tMásodfokú egyenlet")


    elif (option == 0):
        quit()
        

    else:
        print("Érvénytelen lehetőség.")

    print()
    menu()
    option = int(input("Válassz a lehetőségek közül: "))
