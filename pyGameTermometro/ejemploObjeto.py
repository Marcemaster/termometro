class Objeto():
    __atributoPrivado = None
    
    def __init__(self):
        self.__atributoPrivado = 0
        
    def getAtributo(self):
        return self.__atributoPrivado
        
    def setAtributo(self, valor):
        self.__atributoPrivado = valor
        
    # Getter y Setter en la misma función. (Es mejor hacerlo así.)
    
    def getsetAtributo(self, valor=None):
        if valor == None:
            return self.__atributoPrivado
        else:
            self.__atributoPrivado = valor
      