# __init__
# Este metodo es llamado cuando se crea un nuevo objeto
class Student:
    
    
    def __init__(self, name):
        self.name = name
    

# __class__
# Devuelve la clase a la que pertenece un objeto
movies = ['Matrix', 'finding nemo']
print(movies.__class__)
print('Hi'.__class__)



class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
    def __repr__(self):
        return f'<Garage {self.cars}>'
    
    def __str__(self):
        return f'Garage with {len(self)} cars.'



#__len__
# Este metodo debe ser definido. Si no esta definido devuelve un error

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(len(ford)) # llamada al metodo __len__

# __getitem__
# este metodo es usado para idexar un objeto. Si no esta definido devuelve error

print(ford[0])
print(ford[1])

# Al implemtar len y getitem methods, se habilitan nuevas funcionalidades
# Se puede iterar

for item in ford:
    print(item)

# __repr__
# devuelve un string que representa al objeto


# __str__
# Devuelve un string que le dice al usuario alguna informacion acerca del objeto

print(ford)


        



