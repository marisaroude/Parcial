#3. Dada una lista con nombres de personajes de la saga de Avengers, resolver las
#siguientes tareas:
#a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la
#misma;
#b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
#c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
#‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar
#cargados. 
# d. Realizar un barrido ascendente y descendente de la lista. 
# e. Mostrar la información del personaje en la posición 7. 
# f. Mostrar todos los personajes que comienzan con C o S. 
# g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo
#booleano que indica si es héroe True villano False), luego realizar un barrido
#ordenado por nombre y otro por año de aparición. Deberá cargar toda la
#información de nuevo.
from lista import Lista

lista_personajes = Lista()
lista_aux = Lista ()

personajes = [{'nombre': 'Scalet Witch'},
              {'nombre': 'Thor'},
              {'nombre': 'Capitan'},
              {'nombre': 'Yoda'},
              {'nombre': 'Luke'},]

auxiliar = [{'nombre': 'Black Widow'},
       {'nombre': 'Hulk'},
       {'nombre': 'Rocket Racoonn'},
       {'nombre': 'Loki'},]

for personaje in personajes  :
    lista_personajes.insertar(personaje,'nombre')

print('Lista principal: ')  
lista_personajes.barrido()

#Punto C
for aux in auxiliar   :
    lista_personajes.insertar(aux,'nombre')

print('Lista principal + lista aux')
lista_personajes.barrido()


#Punto A   
pos = lista_personajes.busqueda('Thor','nombre')

if (pos != -1):
    print ('Thor se encuentra en la posicion ',pos)
else:
    print ('Thor no se encuentra en la lista')

print()
#PuntoB
pos = lista_personajes.busqueda('Scalet Witch','nombre') 
if(pos!= -1 ): 
    lista_personajes.obtener_elemento(pos)['nombre'] = 'Scarlet Witch'

#Puntod
print('Barrido ascendente: ')
lista_personajes.barrido()
print()
print('Barrido descendete')
for i in range(lista_personajes.tamanio()-1, -1, -1):
    print(lista_personajes.obtener_elemento(i))

#PuntoE
print('Informacion del personaje que esta en la posicion 7 ',lista_personajes.obtener_elemento(7))

#PuntoF
for i in range (lista_personajes.tamanio()):
    if (i< lista_personajes.tamanio()):
        personaje= lista_personajes.obtener_elemento(i)
    
    if (personaje ['nombre'][0] == 'C'):
        print ('El personaje que empieza con C es ', personaje['nombre'])
    if (personaje ['nombre'][0] == 'S'):
        print ('El personaje que empieza con S es ',personaje['nombre'])





   