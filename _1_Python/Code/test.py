class Car:
    def __init__(self,distance,colour,engine_displacement):
        self.distance=distance
        self.colour=colour
        self.engine=engine_displacement
        self.reset_counter=distance*0
        self.increase_counter=distance+232
car1=Car(1500,'red',500,)
car2=Car(2000,'green',510)    
print(car2.increase_counter,'km')
print(car1.reset_counter,'km')

     
    