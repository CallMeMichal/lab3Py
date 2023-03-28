#tryb gry
import random
from getpass import getpass

iloscrund=int(input("wpisz ilosc rund"))
wybor =int(input("wprowadz rodzaj gry : 1.komputer 2.dwoch graczy"))
wynikgracz1=0
wynikgracz2lubNpc=0

kamien=1
papier=2
nozyce=3
i=0
if wybor==1:
    gracz1 = input("wprowadz nazwe gracza 1")
    while i < iloscrund:
        wyborgracz1=int(input("Wybiera gracz: 1.kamien,2.papier,czy 3.nozyce"))
        wyborNpc=random.randrange(1,3)

        if wyborgracz1==1:
            if wyborNpc == 2:
                print("Wygrywa komputer")
                wynikgracz2lubNpc +=1
                i += 1
            elif wyborNpc == 3:
                print("wygrywa gracz")
                i += 1
            else:
                print("remis")
                i += 1
        elif wyborgracz1 == 2:
            if wyborNpc == 3:
                print("Wygrywa komputer")
                wynikgracz2lubNpc += 1
                i += 1
            elif wyborNpc == 1:
                print("wygrywa gracz")
                wynikgracz1 +=1
                i += 1
            else:
                print("remis")
                i += 1
        elif wyborgracz1 == 3:
            if wyborNpc == 1:
                print("Wygrywa komputer")
                wynikgracz2lubNpc += 1
                i += 1
            elif wyborNpc == 2:
                print("wygrywa gracz")
                wynikgracz1 += 1
                i += 1
            else:
                 print("remis")
                 i += 1

    print("wynik Gracza "+str(wynikgracz1))
    print("wynik Komputera : "+ str(wynikgracz2lubNpc))
elif wybor==2:
    #gracz1 = input("wprowadz nazwe gracza 1")
    #gracz2 = input("wprowadz nazwe gracza 2")
    while i < iloscrund:
        wyborgracz1 = int(input("Wybiera gracz 1: 1.kamien,2.papier,czy 3.nozyce"))
        wyborgracz2 = int(input("wybiera gracz 2: 1.kamien,2.papier,czy 3.nozyce"))

        if wyborgracz1 == 1:
            if wyborgracz2 == 2:
                print("Wygrywa gracz2")
                wynikgracz2lubNpc += 1
                i += 1
            elif wyborgracz2 == 3:
                print("wygrywa gracz1")
                i += 1
            else:
                print("remis")
                i += 1
        elif wyborgracz1 == 2:
            if wyborgracz2 == 3:
                print("Wygrywa gracz2")
                wynikgracz2lubNpc += 1
                i += 1
            elif wyborgracz2 == 1:
                print("wygrywa gracz1")
                wynikgracz1 += 1
                i += 1
            else:
                print("remis")
                i += 1
        elif wyborgracz1 == 3:
            if wyborgracz2 == 1:
                print("Wygrywa gracz1")
                wynikgracz1 += 1
                i += 1
            elif wyborgracz2 == 2:
                print("wygrywa gracz2")
                wynikgracz2lubNpc += 1
                i += 1
            else:
                print("remis")
                i += 1
    print("wynik Gracza1 "+str(wynikgracz1))
    print("wynik Gracza2 : "+ str(wynikgracz2lubNpc))