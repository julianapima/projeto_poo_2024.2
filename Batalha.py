from random import *
from Agua import agua
from Grama import grama
from Fogo import fogo

class batalha:

    def _init_(self):
        self.__pokemonUsuario = 0
        self.__pokemonOponente = 0
        self.__status = 0

    def getPokemonUsuario(self):
        return self.__pokemonUsuario
    
    def getPokemonOponente(self):
        return self.__pokemonOponente
    
    def getStatus(self):
        return self.__status

    def setPokemonUsuario(self, pokemon):
        self.__pokemonUsuario = pokemon


    def selecaoUsuario(self):
        tipos = ["fogo", "agua", "grama"]
        aleatorio = randint(0, 2)

        for i in tipos:
            if i == tipos[i]:
                if tipos[i] == "fogo":
                    self.__pokemonUsuario:fogo
                elif tipos[i] == "agua":
                    self.__pokemonUsuario:agua
                elif tipos[i] == "grama":
                    self.__pokemonUsuario:grama
        
        

    
                



