# class Autos:
#     def __init__(self, marca, modelo, patente, color, velocidad_maxima):
#         self.marca = marca
#         self.modelo = modelo
#         self.patente = patente
#         self.color = color
#         self.velocidad_maxima = velocidad_maxima
#         self.velocidad_actual = 0
#         self.encendido = False
#
#     def mostrar_informacion(self):
#         return ('Este auto es un '+self.marca+' '+self.modelo+' y esta andando a '+str(self.velocidad_actual))
#
#     def acelarar(self, velocidad):
#         if self.encendido:
#             try:
#                 velocidad_final = self.velocidad_actual + velocidad
#                 if velocidad_final < self.velocidad_maxima:
#                     self.velocidad_actual = self.velocidad_actual + velocidad
#                 else:
#                     self.velocidad_actual = self.velocidad_maxima
#             except TypeError:
#                 print('no puedo acelarar eso')
#             except ValueError:
#                 print('lo que nos paso no es un integer')
#             except:
#                 print('excepcion atrapada')
#             finally:
#                 print('se intento acelar con '+str(velocidad))
#         else:
#             self.velocidad_actual = self.velocidad_maxima
#
#
#     def frenar(self):
#         if self.encendido:
#             try:
#                 velocidad_final = self.velocidad_actual + velocidad
#                 if velocidad_final > 0:
#                     self.velocidad_actual = self.velocidad_actual + velocidad
#                 else:
#                     self.velocidad_actual = self.velocidad_maxima
#             except TypeError:
#                 print('no puedo frenar eso')
#             except ValueError:
#                 print('lo que nos paso no es un integer')
#             except:
#                 print('excepcion atrapada')
#             finally:
#                 print('se intento frenar con '+str(velocidad))
#         else:
#             self.velocidad_actual = self.velocidad_maxima
#
#     def encender(self):
#         if not self.encendido:
#             self.encendido = True
#         else:
#             print('el auto ya esta encendido')
#
#     def apagar(self):
#         if self.encendido:
#             self.encendido = False
#             #self.velocidad_actual = 0
#             self.frenar(self.velocidad_actual)
#         else:
#             print('el auto ya esta apagado')
#
# mi_auto = Autos('Ford', 'Falcon', 'AE5211XX', "rojo", 200)
# print(mi_auto.marca)
# print(mi_auto.mostrar_informacion())
# mi_auto.encender()
# mi_auto.acelerar(50)
# print(mi_auto.velocidad_actual)
# mi_auto.acelerar(5000)
# print(mi_auto.velocidad_actual)
# print(mi_auto.velocidad_maxima)
# mi_auto.acelerar(100)
# mi_auto.acelerar(12.34)

class Autos:
    def __init__(self, marca, modelo, patente, color, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.color = color
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def mostrar_informacion(self):
        return ('Este auto es un '+self.marca+' '+self.modelo+' y esta andando a '+str(self.velocidad_actual))

    def acelerar(self,velocidad):
        if self.encendido:
            if type(velocidad) is float:
                raise Exception('Only Integers')
            try:
                velocidad_final = self.velocidad_actual + velocidad
                if velocidad_final < self.velocidad_maxima:
                    self.velocidad_actual = velocidad_final
                else:
                    self.velocidad_actual = self.velocidad_maxima
            except TypeError:
                print('No puedo acelerar eso')
            except ValueError:
                print('Lo que nos pas?? no es un integer')
            except:
                print('Excepci??n atrapada')
            finally:
                print('Se intent?? acelerar con '+str(velocidad))
        else:
            print('Debe encender el auto')

    def frenar(self):
        if self.encendido:
            try:
                velocidad_final = self.velocidad_actual - velocidad
                if velocidad_final> 0:
                    self.velocidad_actual = velocidad_final
                else:
                    self.velocidad_actual = self.velocidad_maxima
            except TypeError:
                print('No puedo frenar eso')
            except ValueError:
                print('Lo que nos pas?? no es un integer')
            except:
                print('Excepci??n atrapada')
            finally:
                print('Se intent?? frenar con '+str(velocidad))
        else:
            print('Debe encender el auto')

    def encender(self):
        if not self.encendido: #if self.encendido == False
            self.encendido = True
        else:
            print('El auto ya est?? encendido')

    def apagar(self):
        if self.encendido: #if self.encendido == True
            self.encendido = False
            #self.velocidad_actual = 0
            self.frenar(self.velocidad_actual)
        else:
            print('El auto ya est?? apagado')

mi_auto = Autos('Ford', 'Fiesta', 'AE 167','Azul',180)

print(mi_auto.marca)
print(mi_auto.mostrar_informacion())
mi_auto.encender()
mi_auto.acelerar(50)
print(mi_auto.velocidad_actual)
mi_auto.acelerar(5000)
print(mi_auto.velocidad_actual)
print(mi_auto.velocidad_maxima)
mi_auto.acelerar('papa')
mi_auto.acelerar(12.34)
