from Personaje import Personaje
from Enano import Enano
from Elfo import Elfo
from Humano import Humano
from random import *

selectpersonaje1 = randint(1,3)
selectpersonaje2 = randint(1,3)

print(selectpersonaje2)
print(selectpersonaje1)

while selectpersonaje2 == selectpersonaje1:
    selectpersonaje2 = randint(1,3)

if selectpersonaje1 == 1:
    print("Te toco elfo")
    raza="Elfo"
    reino="colo colo"
    nombre=input("Ingresa Nombre de tu personaje ")
    arma=input("ingresa el arma con la que lucharas")
    Personaje1=Elfo(nombre,raza,arma,0,0,0,reino)
        
elif selectpersonaje1 == 2:
    print("Te toco humano")
    raza="Humano"
    reino="Coquimbo"
    nombre=input("Ingresa Nombre de tu personaje ")
    arma=input("ingresa el arma con la que lucharas")
    Personaje1=Humano(nombre,raza,arma,0,0,0,reino)
            
elif selectpersonaje1 == 3:
    print("Te toco enano")
    raza="Enano"
    reino="U de Chile"
    nombre=input("Ingresa Nombre de tu personaje ")
    arma=input("ingresa el arma con la que lucharas")
    Personaje1=Enano(nombre,raza,arma,0,0,0,reino)
        #Personaje 2
elif selectpersonaje2 == 1:
    print("Te toco elfo")
    raza="Elfo"
    reino="colo colo"
    nombre=input("Ingresa Nombre de tu personaje ")
    arma=input("ingresa el arma con la que lucharas")
    Personaje2=Elfo(nombre,raza,arma,0,0,0,reino)
        
elif selectpersonaje2 == 2:
    print("Te toco humano")
    raza="Humano"
    reino="Coquimbo Unido"
    nombre=input("Ingresa Nombre de tu personaje ")
    arma=input("ingresa el arma con la que lucharas")
    Personaje2=Humano(nombre,raza,arma,0,0,0,reino)
            
elif selectpersonaje2 == 3:
    print("Te toco enano")
    raza="Enano"
    reino="U de Chile"
    nombre=input("Ingresa Nombre de tu personaje ")
    arma=input("ingresa el arma con la que lucharas")
    Personaje2=Enano(nombre,raza,arma,0,0,0,reino)