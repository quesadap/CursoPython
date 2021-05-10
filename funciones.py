def menor():
    electronico = str(input('el jueguete es electronico?: '))
    if electronico != 'si':
        #print('el juguete no es electronico')
    else:
        #print('el juguete es electronico')
    camina = str(input('el jueguete camina?: '))
    if camina != 'si':
        #print('el juguete no camina')
    else:
        #print('el juguete camina')
    color = str(input('de que color es?: '))
    #print('el juguete es de color: '+color)

    return [electronico, camina, color]

def mayor():
    ropa = str(input('camisa o pantalon?'))
    if ropa == 'pantalon':
        print('eligio: '+ropa)
    else:
        print('eligio: '+ropa)
    color = str(input('de que color es?: '))
    print(ropa+' es de color: '+color)
    talle = str(input('cual es el talle?: '))
    print('el talle es: '+talle)

def jubilado():
    destino = str(input('A que destino desea viajar? :'))
    if destino == 'Federacion':
        print('eligio viajar a: '+destino)
    elif destino == 'Cataratas':
        print('eligio viajar a: '+destino)
    else:
        print('eligio viajar a santa teresita')
