nombre = input('Ingrese nombre: ')
apellido = input('Ingrese apellido: ')
edad = int(input('Ingrese edad: '))
#condicion_edad = str(condicion_edad)

if edad < 18:
    #print('menor')
    condicion_edad = 'menor'
elif  edad < 65:
    condicion_edad = 'mayor'
elif  edad < 120:
    condicion_edad = 'jubiliado'
else:
    condicion_edad = 'cadaver'

print('Su nombre es: '+nombre+' '+apellido+' '+'Y usted es '+condicion_edad)
