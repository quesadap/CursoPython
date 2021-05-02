#programa de prueba II
def estado(edad):
    if edad < 0:
        estado = 'usted no nacio'
    if edad < 18:
        estado = 'usted es menor'
    elif edad < 65:
        estado = 'usted es mayor'
    else:
        estado = 'usted es jubiliado'
    return estado

clientes = int(input('Ingrese numero de clientes: '))
for i in range(clientes):
    edad = 0
    print('cliente numero: '+str(i+1))
    while edad < 1 or edad > 120:
        edad = int(input('Ingrese edad: '))
    estado_final = estado(edad)
    print(estado_final)
