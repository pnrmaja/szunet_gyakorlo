def megszamlalas_tetele(szam_lista:list[int]):
    db:int=0
    i:int=0
    n:int=len(szam_lista)
    
    while  i < n:
       ##if szam_lista[i] > 0:
        db+=1
        i+=1

def osszegzes_tetele(szam_lista:list[int]):
    osszeg:int=0
    i:int=0
    n:int=len(szam_lista)

    while i < n:
        ## if szam_lista[i] >0:
        osszeg+=szam_lista[i]
        i+=1

def maximum_kivalasztas_tetele(szam_lista:list[int]):
    max:int=szam_lista[0]
    i:int=1
    n:int=len(szam_lista)

    while i < n:
        if szam_lista[i] > max:
            max=szam_lista[i]
        i+=1




    