import turtle
import random

class Circuito():
    corredores=[]
    __posStartY = (-30,-10,10,30)
    __colorTurtle= ('red','blue','green','orange')
    
    def __init__(self,width,height):
        self.__screen=turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor('lightgrey')
        self.__startLine=-width/2 + 20
        self.__finishLine= width/2 - 20
        
        self.__createRunners()
        
    def __createRunners(self):
        for i in range(4): #este bucle crea los 4 corredores
            new_turtle=turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startLine,self.__posStartY[i])          
            
            self.corredores.append(new_turtle)
                
    def competir(self):
        
        hayGanador=False
        
        while not hayGanador :          
            for tortuga in self.corredores:
                avance=random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.position()[0]>=self.__finishLine:
                    hayGanador=True
                    print ("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break
                     
if __name__== '__main__':
    
    circuito=Circuito(640,480) #es buena costumbre poner esto así para permitir probarlo o utilizarlo como módulo para otros scrpts de python
    circuito.competir()    
        
        