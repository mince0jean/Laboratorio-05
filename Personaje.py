class Personaje():
    def __init__(self, nombre='', raza = '', arma ='', vida= '', daño= '', bonificacion =''):
        self.__nombre = nombre
        self.__raza = raza
        self.__arma = arma
        self.__vida = vida
        self.__daño = daño
        self.__bonificacion = bonificacion
    
    def __str__(self):
        return 'Nombre: {} - Raza: {} - Arma: {} - Vida: {} - Daño: {} - Bonificacion: {} '.format(self.__nombre, self.__raza, self.__arma, self.__vida, self.__daño, self.__bonificacion)
    
    def Getnombre(self):
        return self.__nombre 
    def Setnombre(self,nombre):
        self.__nombre = nombre

    def Getraza(self):
        return self.__raza 
    def Setraza(self,raza):
        self.__raza = raza

    def Getarma(self):
        return self.__arma 
    def Setarma(self,arma):
        self.__arma = arma

    def Getvida(self):
        return self.__vida 
    def Setvida(self,vida):
        self.__vida = vida

    def Getdaño(self):
        return self.__daño 
    def Setdaño(self,daño):
        self.__daño = daño
        
    def Getbonificacion(self):
        return self.__bonificacion 
    def Setbonificacion(self,bonificacion):
        self.__bonificacion = bonificacion
    
    def combate():
        pass
    
    def historia():
        pass
    
    def victoria():
        pass
    
    def derrota():
        pass
    
    def Mensajeinicial():
        print('Bienvenido.........')
    
    