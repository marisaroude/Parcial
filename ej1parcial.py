#1. Dado un vector con personaje de las películas de la saga de Star Wars resolver las
#siguientes actividades:
#a. Realizar un barrido recursivo del vector. 
# b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el
#vector y en que posición. 

personajes = ['Capitana Marvel','Iron Man','Capitan America','Yoda','Luke']

#PuntoA
def barrido(personajes):
    if (len(personajes) > 0):
        print(personajes[0])
        barrido(personajes[1:])


#PuntoB
def buscar (personajes, pos):
    if(pos< len(personajes)):
        if(personajes[pos] == 'Yoda'):
            return pos
        else:
            return buscar(personajes, pos+1)
    else:
        return -1

print(barrido(personajes))
print('Yoda se encuentra en la posicion ',buscar(personajes,0))

