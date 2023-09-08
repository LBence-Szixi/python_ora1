print("\033[36m\033[01mÓRA 1 \033[0m \n \n")

print("Helló Nyíregyháza! \n")
input()
#float
PI = 3.14159
print("A π hozzávetőleges értéke \033[92m" + str(PI) + "\033[0m. \n")

# boolean logikai
tanulo_e = True
print("Tanuló vagyok-e: \033[92m" + str(tanulo_e) + "\033[0m. \n")

input()

#valtozok
szam = 10
szoveg = "péntek 7. óra"

print(type(szam))
print(type(szoveg))
print(type(tanulo_e))
print(type(PI))

input()

# beszédes változóneveket adjunk!
legmenobb_tanar_valaha = "batbat" #snake_case
# legmenobbTanarValaha -> camelCase

# dinamikus típusok
nev = "Lakatos Bence"
print(nev)
nev = 15
print(nev)

input()

vezeteknev = "Kiss"
keresztnev = "Zoltán"
eletkor = 69
print("Helló " + vezeteknev + " " + keresztnev + "!") # a + nem rak space-t közé
print("Helló" , vezeteknev , keresztnev , "!") # a , rak space-t és automatice átalakítja string-é

input()

print("Helló" , vezeteknev , keresztnev , ", te most\033[91m", eletkor, "\033[0méves vagy!")
print("Helló " + vezeteknev + " " + keresztnev + ", te most \033[91m" + str(eletkor) +  "\033[0m éves vagy!")
print(f"Helló {vezeteknev} {keresztnev}, te most \033[91m{eletkor}\033[0m éves vagy!")

input()

print("Jó napot ",keresztnev,"!",sep="",end="\n")

input()

print("\033[33mBoci boci tarka, \033[93m\n se füle se farka... \n")

input()