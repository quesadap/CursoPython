#programa de prueba - ejercicio clase 2

#nombre = input('digame su nombre: ')
#apellido = input('digame su apellido: ')
#edad = input('digame su edad: ')
#edad = int(edad)

#print('Su nombre es: '+nombre+' '+apellido)

#if edad<0:
    #print('Usted no nacio')
#elif edad <18:
    #print('Usted es Menor de edad')
#elif edad <65:
    #print('Usted es Mayor de edad')
#elif edad <120:
    #print('Usted esta Jubilado')
#else:
    #print('Usted esta Fallecido')


#programa de prueba II
clientes = int(input('Ingrese numero de clientes: ')
for i in range(clientes):
    print(i)

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
