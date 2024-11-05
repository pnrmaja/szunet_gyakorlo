import math
import random
def feladat1():
    szam: int =int(input("Kérek egy [200, 920] intervallumban lévő egész számot"))

    if 200 <= szam <= 920:
        szoveg_szam: str = str(szam)
        print(f"{szoveg_szam[0]}")
    else:
        print("Hiba")

def feladat2(szam:int):
    
    if szam == 1:
        print(f"Még 90% on vagyunk!")
    elif 2 <= szam <= 3:
        print(f"Még bírjuk (60%)")
    elif 4 <= szam <= 7:
        print(f"Progit tanulunk, töltődünk! 70%")
    elif 8 <= szam <= 9:
        print(f"Lassan nem bírjuk tovább! 50%")
    elif 10 <= szam:
        print(f"Ez már tényleg túlzás.")
    else:
        print(f"Be se jövök!")

def feladat3(nap:str, ora:str):
    if nap == "hétfő":
        print(f"alszik")
    elif nap == "kedd":
        if ora == "hittan":
            print(f"figyel")
        else:
            print(f"alszik")
    elif nap == "szerda":
        if ora == "programozás":
            print(f"dolgozik")
        else:
            print(f"nincs info")
    elif nap == "csütörtök":
        print(f"figyel")
    elif nap == "péntek":
        print(f"félig van jelen")
    else:
        print(f"nincs info")    

def feladat4():
    szam:float =float(input("Kérek egy valós számot"))
    if szam < 0:
        print(f"Hiba")
    else:
        negyzetgyok: float= math.sqrt(szam)
        print(f" A számunk {szam} és annak a négyzetgyöke: {negyzetgyok}")

def feladat5():
    szam:float =float(input("Kérek egy valós számot"))
    szam1:float =float(input("Kérek egy valós számot"))
    
    if szam1 >=0 and szam >=0:
        terulet:float=szam*szam1
        kerulet:float=2*(szam+szam1)
        print(f"A téglalap területe: {terulet:.2f} és a téglalap kerülete:{kerulet:.2f}")
    else:
        print(f"Hiba: a téglalap oldalai nem pozitívak!")    

def feladat1_1():
    szektor:str=input("Kérek egy szektort!")
        

    if szektor == "A":
        print(f"Nemzetközi Csarnok, World Conservation Forum 2021")
    elif szektor == "B" or szektor == "E":
        print(f"Kereskedelmi Csarnok")
    elif szektor == "C":
        print(f"Konferencia-központ Innovációs Showroom")
    elif szektor == "D":
        print(f"Hal, Víz és Ember")
    elif szektor == "F":
        print(f"Hagyományos Vadászati Módok Csarnoka")
    elif szektor == "G":
        print(f"Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
    elif szektor == "H":
        print(f"Központi Magyar Kiállítás")
    elif szektor.isdigit():
        print("HIBA: Adjon meg egy betűt A-H-ig!")

    else:
        print(f"Forduljon a pénztárhoz")

def feladat6():
    lista:list[int]=[]
    i:int=0

    while i < 13:
        szam=random.randint(-5,12)
        lista.append(szam)
        
        i+=1

    print(lista)
    return lista

def feladat6_1(lista:list[int]):
    db:int=0
    db_negativ:int=0
    i:int=0
    n:int=lista.__len__()
    while i < n:
        if lista[i]>0:
            db+=1
        elif lista[i]<0:
            db_negativ+=1
            
        i+=1
    print(f"db darab {db} pozitív szám. db darab {db_negativ} negatív számot találtunk.")


def feladat6_2(Lista:list[int]):
    i:int=0
    n:int=len(Lista)
    osszeg:int=0

    while i < n:
        if Lista[i]%2==0:
            osszeg+=Lista[i]
        i+=1

    print(f" A páros számok összege {osszeg}")

def feladat6_3(Lista:list[int]):
    i:int=0
    n:int=len(Lista)
    osszeg:int=0
    paros_osszeg:int=0

    while i < n:
        if Lista[i]%2==1:
            osszeg+=Lista[i]
        elif Lista[i]%2==0:
            paros_osszeg+=Lista[i]
            
        i+=1

    print(f" A páratlan számok összege {osszeg} és a páros számok összege: {paros_osszeg}")
    if osszeg >= paros_osszeg:
        print(f"A páratlan számok összege a nagyobb {osszeg}")
    else:
        print(f"A páros számok összege a nagyobb {paros_osszeg}")

def feladat6_4(Lista:list[int]):
    atlag:float=0
    i:int=0
    n:int=len(Lista)
    osszeg:float=0

    while i < n:
        osszeg+=Lista[i]
        i+=1
    atlag=osszeg/n
    print(f"A számok átlaga: {atlag}")

def feladat6_5(Lista:list[int]):
    max:int=Lista[0]
    i:int =0
    n:int=len(Lista)

    while i < n:
        if Lista[i] > max:
            max=Lista[i]
        i+=1
    print(f"A legnagyobb szám {max}")

def feladat7():
    nev:str=input("Kérek egy nevet!")
    van_a:bool=False
    nev_lista:list[str]=[]
    
    while nev != "@":
        nev_lista.append(nev)
        nev=input("Kérek egy nevet!")

    i:int=0
    n:int=len(nev_lista)
    max:str=""

    while i < n:
        if nev_lista[i][0].upper() == "A":
            van_a = True
        if len(nev_lista[i]) > len(max):
            max=nev_lista[i]
        
        i+=1
    print(f"Ennyi nevet adott meg a felhasználó: {n}")
    print(f"Van-e benne A betűvel kezdődő név? {van_a}")
    print(f"Ez a leghosszabb név: {max}")

def feladat8():
    db:int=0
    i:int=0
    bekeres:str=input("„f” vagy  „i” betűket kérek!")
    max:int=0
    f_sorozat:int=0

    while i < 10:
        while bekeres != "f" and bekeres!= "i":
            bekeres=input("„f” vagy  „i” betűket kérek!")
        if bekeres == "f":
            db+=1
            f_sorozat+=1
        elif bekeres =="i":
           
            f_sorozat=0
        if f_sorozat > max:
                max=f_sorozat
        bekeres=""
        i+=1
    print(f"Ennyiszer adott meg 'f' betűt:{db} ")
    print(f"A leghosszabb 'f' sorozat: {max}")

def feladat9():
    i:int=1
    n:int=11

    while i < n:
        print(f"{i} * {n-1}={i*(n-1)}")
        i+=1

def feladat10(szam:int):
    i:int=0
    while szam > 0:
        a:int=szam//10
        maradek:int=szam%10
        print(f"{maradek} db {10**i} van")
        szam=a
        i+=1

def feladat11(szam:int):
    osszeg:int=0
    eredeti_szam:int=szam
    while szam > 0:
        a:int =szam//10
        maradek:int=szam%10
        szam=a
        osszeg+=maradek
    print(f"{eredeti_szam} számjegyeinek összege:{osszeg} ")

def feladat12():
    szam:int=int(input("Kérek pozitív egész számot, és megmondom, hogy tökéletes szám-e!"))
    osszeg:int=0
    i:int=1

    while i<=szam:
        if szam %i==0:
            osszeg+=i
        i+=1
    if osszeg==szam*2:
        print(f"Ez egy tökéletes szám")
    else:
        print(f"Ez nem egy tökéletes szám")

def feladat13(szam:int,szam1:int):
    lnko = 1
    x = 1
    if szam > szam1:
            while x <= szam1:
                if szam % x ==0 and szam1 % x ==0:
                    lnko=x

                x+=1

    else:
        while x <= szam:
            if (szam % x == 0 and szam1 % x == 0):
                lnko = x

            x+=1
    if lnko > 1:
        print(f" A legnagyobb közös osztó: {lnko}")
    else:
        print("Nincs közös osztó")

def feladat13_1(szam:int,szam1:int):
    lnko=1
    x=szam
    talalt:bool=False
    if szam >szam1:
        x=szam1
    while x > 1 and not talalt:
        
        if szam % x == 0 and szam1 % x == 0:
            lnko=x
            talalt=True
        x-=1
    
    print(f" A legnagyobb közös osztó: {lnko}")
    

def feladat1_plusz_plusz(szam:int,szam1:int):
    lkkt:int=szam
    taLalt:bool=False
    x:int=szam1

    if szam >szam1:
        x=szam
        lkkt=szam1
        
    while x <= szam*szam1 and not taLalt:
        if x % szam==0 and x % szam1 == 0:
            taLalt=True
            lkkt=x
        x+=1
    print(f"A legkissebb közös többszörös: {lkkt}")

    

            


       


        
    








