#crear una clase persona
#nombre
#apellido
#edad
#dni
#METODOS:
#nombrar > CArlos > Carlos
#dar apellido > suarez > Suarez
#cumplir > cumplir años
#gustos de ropa > 0 a 9 le gusta la moda infantil
# 10 a 18 le gusta la moda juvenil
# 19 a 50 le gusta la ropa casual
# mas de 50 le gusta la ropa de viejo

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        #self.apellido = apellido
        #self .edad = 0
        #self.dni = dni

    def nombrar(self, mi_nombre):
        try:
            self.nombre = mi_nombre
            #return (mi_nombre)
            if (mi_nombre == ''):
                print('ingrese un nombre')
            else:
                print('el nombre es: '+mi_nombre.capitalize())
                return (mi_nombre)
        except TypeError:
            print('No puede estar vacio el nombre')

mi_persona = Persona('')
print(mi_persona.nombrar('test'))
#mi_persona.nombre = 'pablo'
#print(mi_persona.nombre.capitalize())
