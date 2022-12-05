from Personaje import Personaje

class Humano(Personaje):

    def __init__(self, nombre='', raza='', arma='', vida='', daño='', bonificacion='', familia=''):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__familia = familia
    
    def __str__(self):
        return super().__str__()+'Familia:{}'.format(self.__familia)
    
    def GetFamilia(self):
        return self.__familia
    def SetFamilia(self,familia):
        self.__familia = familia
    

    def historia():
        print('Una raza a comparacion de las otras muy actual y poderosa a su vez, ha hecho grandes daños a las demas razas posicionandose como lider actualmente del planeta')
        
    def victoria(self):

        print('Informacion del ganador')
        print('El nombre del Enano es:')+ self.__nombre
        print('La raza del Enano es:')+ self.__raza
        print('La arma ocupada fue :') + self.__arma
        print('La familia gandora es: ') + self.__familia

        print('¡¡lO LOGRASTE, La FAMILIA AUN PERDURA!!.......... pero no por mucho... ')
        
    def derrota():

        print('HAZ HECHO DESAPARECER A LA RAZA HUMANA.... ACTUALIZA TU ARMA PARA VOLVER A INTENTARLO')
        
        
    def superbono():
        pass
    