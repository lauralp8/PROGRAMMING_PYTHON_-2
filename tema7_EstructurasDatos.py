# defaultdict hace un callable y lo devuelve (mirar ejemplo)


# ÁRBOLES - HEAPQ
print("HEAPQ (PUSH Y POP)")
print("EJEMPLO ÁRBOLES 1")
from dataclasses import dataclass
import heapq
@dataclass
class Job:
    id: int
    name: str


taks = [(10, Job(1, 'study ai')),
        (4, Job(2, 'study ml')),
        (1, Job(3, 'study dss'))]
# Covert to a heap
heapq.heapify(taks)     # O(n). Conviertes la lista de objetos a árbol
# estamos metiendo un elemento en el árbol y le pasamos:
# el peso de su rama (el 0)
# el tipo de objeto
heapq.heappush(taks, (0, Job(3, 'study prog II')))
while True:             # bucle infinito
    try:
        task = heapq.heappop(taks)
        # sacas cada elemento de la lista (según el elemento que menos pese)
        print(task[1])  # O(1). Sacamos el elemento 1 con pop y lo eliminamos.
    except IndexError:  # cuando la lista esté vacía, se mete en el except.
        # el error de Index, es cuando el índice no existe (lista vacía)
        print('End')
        break           # sale del loop con el break

# PUSH Y POP EN LISTAS
print("\n\n\nEJEMPLO PUSH Y POP (LISTAS)")
aux = [1,2,3,4]
while True:
    try:
        print(aux.pop())
    except IndexError:
        print("La lista se ha quedado vacía")
        break
print("El programa continúa de forma normal")

# PUSH Y POP ÁRBOLES
print("\n\n\nEJEMPLO ÁRBOLES 2")
@dataclass
class Job:
    priority: int
    id: int
    name:str

    def __lt__(self, other):
        return self.priority < other.priority

taks = [ Job(4, 1, 'study ai'), Job(2, 2, 'study ml'), Job(3, 3, 'study dss')]

heapq.heapify(taks) # transformamos a árbol y ordenamos de menor a mayor prioridad
heapq.heappush(taks, Job(0, 4, 'study prog II'))    # elemento nuevo
while True:
    try:
        task = heapq.heappop(taks)  # saca el elemento con menor peso y lo guarda en task
        print(task.name)  # imprimimos sólo los nombres en el orden dado anteriormente
    except IndexError:
            print('End')
            break

# CHAINMAPS:
# es un tipo de objeto ya creado.
# le pasamos la cantidad de diccionarios que tu quieras
# une los diccionarios (lista de dics) y de los atributos repetidos, guarda el que se ha metido primero
print("\n\n\nEJEMPLO CHAINMAP")
from collections import ChainMap

baseline ={'music': 'bach', 'art': 'rembrandnt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}

cm = ChainMap(adjustments, baseline)        # hacemos una lista de diccionarios
# juntamos dos diccionarios
# cuando accedemos a una clave que tienen los dos, devuelve la primera que se ha metido o la primera que encuentre
print(cm)
print(cm['music'])
print(cm['art'])

# creamos un chainmap nuevo para meter un diccionario nuevo:
cm2 = cm.new_child(m={'art': 'picasso', 'opera': 'la_traviata'})    # la m se puede no poner (es para indicar el tipo)
print(cm)   # esta lista de dics se queda igual
print(cm2)  # se imprime añadiendo el nuevo elemento al principio de la lista de dicts


# COUNTER
# crea un diccionario con los elementos de una lista y te imprime los elementos de la lista y cuantas veces se repite
# lo ordena de mayor a menor (de mayor repetición a menor repetición)
print("\n\n\nEJEMPLO COUNTER 1")
from collections import Counter
cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(cnt)
print(cnt['purple'])    # si buscas un elemento dentro del dic sale 0 porque no existe

print("\n\n\nEJEMPLO COUNTER 2")
cnt['red']+=1       # suma 1 a red
print(cnt)

# sumamos diccionarios
cnt2 = Counter(['red', 'blue', 'red'])
print(cnt + cnt2)

print("\n\n\nEJEMPLO COUNTER 3: Count the number of multiples of 3 between 0 and 100")
i=0
list = []
for i in range(100):
    if i%3 == 0:
        list.append(i)

print(list)
list_cnt = Counter(list)
print(list_cnt)


# POPITEM()
# saca el último elemento
print("\n\n\nEJEMPLO POPITEM")
a = dict(john='A', mary='A+', sonya='A++')
print(a.popitem())  # te devuelve el útimo elemento
print(a)            # lo saca de la lista

# iter cuando convertimos un objeto en iterable, para poder hacer el next
it = iter(a.keys())     # hacemos iterables john y mary que son las keys (sus valores son values)
print(next(it))
print(next(it))

"""
print("\n\nREVERSED")
a_reversed = list(reversed(a.keys))
"""


# TIMEBOUNDED LRU: CACHE
# la caché es un diccionario ordenado en función del tiempo y después del resultado
# FUNCIONAMIENTO DE LA CACHE FIFO
# HUECO CACHÉ
# - si existe el elemento: el elemento se mueve al primero más vacío (izq) y todos un hueco a la drch
# - si no existe el elemento: lo metes en el de más de el principio
# CACHÉ LLENA
# - si existe el elemento: lo mueves al de más a la izq y el resto un huecho a la drcha
# - si no existe el elemento: se pone en el de más a la izq y todos se mueven uno a la drch,
#   el de más a la drch, se elimina
print("\n\n\nEJEMPLO TIMEBOUNDED LRU: CACHÉ")
import time
from typing import OrderedDict
class TimeBoundedLRU:
    """ LRU Cache that invalidates and refreshes old entries """
    def __init__(self, func, maxsize=128, maxage=30):
        # la caché se va a crear como un diccionario ordenado conforme al tiempo
        self.cache = OrderedDict()  # { args : (timestamp, result)}
        self.func = func
        self.maxsize = maxsize
        self.maxage = maxage

    def __call__(self, *args):  # no sabemos cuantos argumentos le vamos a pasar
        if args in self.cache:  # si el argumento ya está en la caché (no le pasamos la función)
            self.cache.move_to_end(args)    # movemos el argumento de tal forma que se queda como el más reciente (drch)
            timestamp, result = self.cache[args]    # en la caché metemos el tiempo en el que se ha accedido y el valor
            if time.time() - timestamp <= self.maxage:  # miramos si la diferencia entra dentro del rango permitido
                return result
        result = self.func(*args)   # si no está dentro de la caché, se llama a la función
        self.cache[args] = time.time(), result  # guarda el valor con el tiempo y su resultado
        if len(self.cache) > self.maxsize:      # si se pasa el tamaño de la caché
            self.cache.popitem(False)           # sacamos el elemento que lleva más tiempo
            # El False sirve para que no coja el de la derecha, que es el más reciente, sino que coge el de más a la izq
        return result

# función que eleva el elemento al cuadrado
def cuadrado(x):
    return x**2


aux = TimeBoundedLRU(cuadrado)  # llamas a la clase y le pasas la función del init
aux(2)
print(aux.cache)
aux(3)
print(aux.cache)
aux(2)
print(aux.cache)


# NAMED TUPLES
print("\n\n\nNAMED TUPLES")
# crea una tupla donde creas un nombre de la tupla y la lista de atributos
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y']) # creas un objeto tipo Point (tupla)
p = Point(11, 22)
print("Imprimimos", p)

print("Sumas:")
suma1 = p[0] + p[1]
suma2 = p.x + p.y
print(suma1, suma2)

print("Asignamos valores de la tupla a x e y")
x, y = p
print(p)


print("\n\n\nEJERICIO TIMEBOUNDED LRU: CACHÉ ")
class TimeBoundedLRU:
    def __init__(self, func, maxsize=128, maxage=30):
        self.cache = OrderedDict()
        self.func = func
        self.maxsize = maxsize
        self.maxage = maxage

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            timestamp, result = self.cache[args]
            if time.time() - timestamp <= self.maxage:
                return result
        result = self.func(*args)
        self.cache[args] = time.time(), result
        if len(self.cache) > self.maxsize:
            self.cache.popitem(False)
        return result

def query(x: int, y: int) -> int:
    print('Computing...')
    time.sleep(2)
    print('End')
    return x + y

aux = TimeBoundedLRU(query)
aux(8,7)
aux(8,7)
aux(9,7)

print(aux.cache)