from Personaje import Personaje

class Elfo(Personaje):

    def __init__(self, nombre='', raza='', arma='', vida='', daño='', bonificacion='', reino=''):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__reino = reino
    
    def __str__(self):
        return super().__str__()+'Reino: {}'.format(self.__reino)
    
    def GetReino(self):
        return self.__reino
    def Setreino(self,reino):
        self.__reino = reino
    
    def historia():
        print('La raza mas grande y poderosa de todo el mundo esta siendo en la actualidad muy debilitada; las guerras largas han provocado su disminucion')
        
    def victoria(self):

        print('Informacion del ganador')
        print('El nombre del Enano es:')+ self.__nombre
        print('La raza del Enano es:')+ self.__raza
        print('La arma ocupada fue :') + self.__arma
        print('El reino ganador es: ') + self.__reino

        print('¡¡lO LOGRASTE, EL REINADO DE ELFOS AUN PERDURA!!.......... pero no por mucho... ')

    def derrota():
        print('La raza mas grande y poderosa de todo el mundo esta siendo en la actualidad muy debilitada; las guerras largas han provocado su disminucion')

    def quitavida():
        pass