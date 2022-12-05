from Personaje import Personaje

class Enano(Personaje):

    def __init__(self, nombre='', raza='', arma='', vida='', daño='', bonificacion='', clan= ''):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__clan = clan
    
    def __str__(self):
        return super().__str__()+ 'Clan: {}'.format(self.__clan)

    def GetClan(self):
        return self.__clan
    def SetClan(self,clan):
        self.__clan = clan

    def historia():
        print('En el antiguo imperios de los enanos, muchos fallecieron tras las guerra de las razas pero aun quedan algunos sobrevivientes, dispuesto a seguir peleando para dominar el planeta y ser los predominantes')

     
    def victoria(self):
        print('Informacion del ganador')
        print('El nombre del Enano es:')+ self.__nombre
        print('La raza del Enano es:')+ self.__raza
        print('La arma ocupada fue :') + self.__arma
        print('El clan perteneciente es: ') + self.__clan

        print('¡¡lO LOGRASTE, LA RAZA ENANO AUN PERDURA!!.......... pero no por mucho... ')

    def derrota(self):
        print(self.__nombre)
        print('GAME OVER, la raza Enano ha si totalmente extinta')

        
    def aumentavida():
        pass