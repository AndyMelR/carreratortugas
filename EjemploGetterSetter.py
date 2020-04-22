class ClaseconGetterySetter():
    def __init__(self):
        self.__propiedad_privada=None  #atributo privado y tengo que crear un metodo

    def setPropiedadPrivada(self,valor): #setter fija la propiedad
        self.__propiedad_privada=valor 
    
    def getPropiedadPrivada(self,valor): #getter 
        self.__propiedad_privada

    def __str__(self):
        return "ClaseconGetterySetter con propiedad privada: {} ".format(self.__propiedad_privada)
    
if __name__== "__main__":
    c=ClaseconGetterySetter()
        