import sys  

if len(sys.argv) < 2 or len(sys.argv) > 3:  
   print("""Program wymaga co najmniej 1 parametru:\
               1 - hasło (wymagane)\
               2 - nazwa pliku w którym mają zostać zapisane wyniki. Domyślenie hasla.txt""")
   sys.exit()  
elif len(sys.argv) == 3:  
   plik = sys.argv[2]  
else:  
   plik = "hasla.txt"

lista = [sys.argv[1]]  # pierwszy parametr to hasło, dodajemy je do listy

def dodajCyfre(haslo, liczba, nowa):  # funkcja dodająca cyfrę do hasła
   nowa.append(haslo + str(liczba))
   if liczba < 9:
       return dodajCyfre(haslo, liczba+1, nowa)  # rekurencyjne wywołanie funkcji
   else:
       return nowa  # zwracamy listę z nowymi hasłami

def zamienLitere(haslo, pozycja, nowa):  # funkcja zamieniająca literę na wielką literę
   if haslo[pozycja].islower():
       haslo2 = haslo[0:pozycja] + haslo[pozycja].upper() + haslo[pozycja+1:]
   nowa.append(haslo2)
   if pozycja < len(haslo)-2:
       return zamienLitere(haslo, pozycja+1, nowa)  # wywołanie funkcji
   else:
       return nowa  # zwracamy listę z nowymi hasłami

def przejrzyj(lista, pozycja, nowa, funkcja):  # funkcja wywołująca poprzednie funkcje
   nowa += funkcja(lista[pozycja], 0, [])  # dodajemy nowe hasło do listy
   if pozycja < len(lista)-1:
       return przejrzyj(lista, pozycja+1, nowa, funkcja)  # wywołanie funkcji
   else:
       return nowa  

lista = przejrzyj(lista, 0, [], dodajCyfre)  # wywołujemy funkcję przejrzyj z funkcją dodajCyfre
lista = przejrzyj(lista, 0, [], zamienLitere)  # wywołujemy funkcję przejrzyj z funkcją zamienLitere

print(lista)  # wyświetlamy listę z nowymi hasłami

plik = open("./"+plik, "w")  # otwieramy plik do zapisu
plik.write('\n'.join(lista))  # zapisujemy listę do pliku
plik.close()  # zamykamy plik