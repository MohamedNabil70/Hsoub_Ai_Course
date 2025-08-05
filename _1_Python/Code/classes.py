class Car1:
    type = "SUV"
    
    def __init__(self, color, distance, engine_capacity):
        self.color = color
        self.distance = distance                #disctance in KM
        self.engine_capacity = engine_capacity  # engine_capacity in CC
    
    def increase_distance(self, increment):
        self.distance += increment
    def reset_distance(self):
        self.distance = 0

class Car2:
    type = "Sedan"
    
    def __init__(self, color, distance, engine_capacity):
        self.color = color
        self.distance = distance                #disctance in KM
        self.engine_capacity = engine_capacity  # engine_capacity in CC
    
    def increase_distance(self, increment):
        self.distance += increment
    def reset_distance(self):
        self.distance = 0



Tucson = Car1('white', 10000 , 520)

Qashqai = Car1('white', 20000 , 600)

C150 = Car2("Black",15000, 720)

print('*' * 50)
print('Tucson.type')
print(Tucson.type)
print('Qashqai.type')
print(Qashqai.type)
print('C150.type')
print(C150.type)

print('*' * 50)
print('Tucson.distance')
print(Tucson.distance)
print('Qashqai.distance')
print(Qashqai.distance)
print('C150.distance')
print(C150.distance)
print('*' * 50)
print('*' * 50)



Tucson.increase_distance(222)
C150.reset_distance()



print('*' * 50)
print('Tucson.distance')
print(Tucson.distance)
print('Qashqai.distance')
print(Qashqai.distance)
print('C150.distance')
print(C150.distance)
print('*' * 50)
print('*' * 50)


