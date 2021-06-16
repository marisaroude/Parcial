#2. Dada una cola con las notificaciones de las aplicaciones de red social de un Smartphone, 
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el
#mensaje, resolver las siguientes actividades:
#c. escribir una función que elimine de la cola todas las notificaciones de
#Facebook;
#d. escribir una función que muestre todas las notificaciones de Twitter, cuyo
#mensaje incluya la palabra ‘Python’, si perder datos en la cola;
#e. utilizar una pila para almacenar temporalmente las notificaciones de
#Instagram y mostrar el contenido de dicha pila. 

from cola import Cola
from pila import Pila

class Notificaciones (object):
    def __init__ (self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

cola_notificaciones = Cola()
cola_aux = Cola()
pila_temporal = Pila()

notificaciones = Notificaciones('21:00', 'Facebook','Ha recibido un mensaje de Marta')
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('23:00', 'Facebook','A Marta le ha gustado tu publicacion')
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('07:00', 'Instagram','2 personas han dado me gusta a su publicacion')
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('08:00', 'Twitter','Marta ha twiteado que le gusta programar con python')
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('12:00', 'Twitter','Marta le ha dado mg a su tweet')
cola_notificaciones.arribo(notificaciones)

#Punto c
while (not cola_notificaciones.cola_vacia()):
    dato = cola_notificaciones.atencion()
    if(dato.aplicacion != 'Facebook'):
        cola_aux.arribo(dato)

while (not cola_aux.cola_vacia()):
    cola_notificaciones.arribo(cola_aux.atencion())

#Punto d
while (not cola_notificaciones.cola_vacia()):
    dato = cola_notificaciones.atencion()
    if 'python' in dato.mensaje:
        print ('El mensaje es ', dato.mensaje)
    cola_aux.arribo(dato)

while (not cola_aux.cola_vacia()):
    cola_notificaciones.arribo(cola_aux.atencion())

while (not cola_notificaciones.cola_vacia()):
    dato = cola_notificaciones.atencion()
    if (dato.aplicacion == 'Instagram'):
        pila_temporal.apilar(dato)
    cola_aux.arribo(dato)

while (not cola_aux.cola_vacia()):
    cola_notificaciones.arribo(cola_aux.atencion())



#muestra sin facebook.
cantidad_elementos = 0 
while(cantidad_elementos < cola_notificaciones.tamanio()):
    datos = cola_notificaciones.mover_al_final()
    print('Notificacion de :', datos.aplicacion)    
    cantidad_elementos += 1  

while (not pila_temporal.pila_vacia()):
    print(pila_temporal.desapilar())