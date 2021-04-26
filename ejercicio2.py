#programa de prueba II
clientes = int(input('Ingrese numero de clientes entre 1 y 120: '))
while clientes < 1 or clientes > 120:
    print('por favor ingrese un numero entre 1 y 120')
    clientes = int(input('Ingrese numero de clientes entre 1 y 120: '))
else:
    for i in range(clientes):

        print('cliente numero: '+str(i+1))
        nombre = input('Ingrese nombre: ')
        apellido = input('Ingrese apellido: ')
        edad = int(input('Ingrese edad: '))

        if edad <18:
            condicion_edad = 'menor'
        elif edad <65:
            condicion_edad = 'mayor'
        elif edad <120:
            condicion_edad = 'jubiliado'
        else:
            condicion_edad = 'cadaver'

        print('Su nombre es: '+nombre+' '+apellido+' '+'Y usted es '+condicion_edad)
