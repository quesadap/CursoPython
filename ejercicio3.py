#programa de prueba II
import funciones

clientes = int(input('Ingrese numero de clientes: '))
for i in range(clientes):
    edad = 0
    print('cliente numero: '+str(i+1))
    while edad < 1 or edad > 120:
        edad = int(input('Ingrese edad: '))
    if edad < 0:
        print('usted no nacio')
    if edad < 18:
        print('usted es menor')
        datos = funciones.menor()
        #funciones.menor()
    elif edad < 65:
        print('usted es mayor')
        funciones.mayor()
    else:
        print('usted es jubiliado')
        funciones.jubilado()
