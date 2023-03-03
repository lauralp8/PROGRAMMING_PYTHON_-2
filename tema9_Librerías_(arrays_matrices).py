# ARRAYS
import numpy as np
import pandas as pd

print("MATRICES 1:")
a = np.array([1, 2, 3])
print(type(a), a.shape, a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3],[4,5,6]])

print(b.shape)
print(b[0,0],b[0,1],b[1,0])

c = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
d = np.array([[1],[8]])
print(c.shape)
print(d.shape)

print("\n\nARRAY CREATION")
a = np.zeros((2,2,2))       # llenamos de 0
print('A',a)
b = np.ones((1,2))          # llenamos de 1
print('B',b)
c = np.full((2,2), 7)       # llenamos de una constante
print('C',c)
d = np.eye(2)               # matriz identidad del tamaño que pases
print('D',d)
e = np.random.random((2,2)) # llenamos de randoms
print('E', e)
f = np.zeros((2,1,4,2))
print(f)

print("\n\nBASIC SLICING")
# se hace con el shape
x = np.array([[0,10], [8,9]])
print(x.shape)
# para imprimir el 10 y 8
print(x[0,1],x[1,0])

y =np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(y[-2:10]) # empieza por la posición 10 y le resta 2
print(y[-3:3:-1])

print("\n\nIMPRIMIR POR ÍNDICES (SIN INCLUIR EL ÚLTIMO")
xy = np.array([[[1],[2],[3]], [[4],[5],[6]], [[7],[8],[9]]])
xy.shape
print(xy[2:3])

print("\n\nELLIPSIS")
print(xy[...,0])        # imprime la expansión completa del array


print("\n\nNEWAXIS: NO ENTIENDO BIEN")
x = np.array([[[1],[2],[3]], [[4],[5],[6]]])
# le añadimos una dimensión nueva
print(x[:,np.newaxis,:,:])
print(x[:,np.newaxis,:,:].shape)

print('\n\nSLICES AS VIEWS')
# Cambiar los valores que quieras
# a[:2, 1:3] = [[1, 0], [0, 1]]

print('\n\nADVANCED INDEXING')
x = np.array([[1,2],[3,4],[5,6]])
x[[0,1,2],[0,1,0]]
print(x[[0,1,2],[0,1,0]])   # eliges los valores que quieres mostrar (primero fila y luego valores)

print("\n\nSELECT CORNER ELEMENTS: EJERCICIO")
x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# seleccionar las esquinas de la matriz (0,2,9,11)
x[[0,0,3,3],[0,2,0,2]]
print(x[[0,0,3,3],[0,2,0,2]])

print("\n\nBOOLEAN INDEXING")
a = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
bool_idx = (a>2)    # imprime la matriz con true o false en función de si cumple o no la condición
print(bool_idx)
print(a[bool_idx])  # te imprime un array con los true
print(a[a>2])       # te imprime un array con los true

print("\n\nDATA TYPES")
# si no especificas numpy pone el tipo
a = np.array([[0,1,2]], dtype=str)
print(a)

print("\n\nMATHEMATICAL OPERATIONS")
sum1 = np.array([[0,1],[3,4]])
sum2 = np.array([[5,6],[2,3]])
print(sum1+sum2)
print(sum1-sum2)
print(sum1*sum2)
print(sum1/sum2)
print(np.sqrt(sum1))
print(sum1.dot(sum2))       # producto escalar
print(np.dot(sum1,sum2))    # priducto escalar

print("\n\nCOMPUTATIONS ON ARRAYS")
x = np.array([[1,2],[3,4]])
print(np.sum(x))            # suma de todos sus elementos
print(np.sum(x, axis=0))    # suma columnas
print(np.sum(x, axis=1))    # suma filas

print("\n\nPANDAS")
print("CREATING SERIES")
# adjudica un índice a un valor
s = pd.Series(list(range(5)), index=['a', 'b', 'c', 'd', 'e'])
print(s)    # imprimies una tabla con índices predeterminados y se imprime el tipo de los números
f = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(f)    # misma función pero con números random

print('\n\nPANDA NDARRAY-LIKE')
print(s[0])
print(s[:3])
print(s[s>s.median()])  # imprime todo lo que esté por encima de la mediana
print(s[[4,3,1]])       # imprime el que tenga valor 4 valor 3 y valor 1
print(np.exp(s))        # e elevado al número del índice

print('\n\nPANDA DICT-LIKE')
print(s['a'])
print(s+s)              # suma los elementos de s
#s['e'] = 12
print(s)
print("e" in s)         # ¿'e' está en s?
print(s[1:])
print(s[:-1])           # coges hasta la penúltima
# hace la intersección (coge los elementos que compartan ambos)
print(s[1:] + s[:-1])

print('\n\nINDEXES')
data = { 'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2] }
# establece la tabla con números base
purchases = pd.DataFrame(data)
print(purchases)
# establece la tabla con el índice que tu quieres
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases)

print('\n\nDICCIONARIOS')
df = pd.DataFrame.from_dict( {"A": [1, 2, 3], "B": [4, 5, 6]}, orient="index", columns=["one", "two", "three"], )
print(df)
print(df["one"])
df = pd.DataFrame.from_dict(
{"A": [1, 2, 3], "B": [4, 5, 6]},
orient="index",
columns=["one", "two", "three"],
)

dc = pd.DataFrame.from_dict(
{"A": [1, 2, 3], "B": [4, 5, 6]}
)


print(df)
print(dc)


print("\n\nIMPLEMENTATION")
from scipy.optimize import linprog

c = np.array([-29.9, -45.0, 0.0, 0.0])
A_ub = np.array([[1.0, -1.0, -3.0, 0.0], [-2.0, 3.0, 7.0, -3.0]])
b_ub = np.array([5.0, -10.0])
A_eq = np.array([[2.0, 8.0, 1.0, 0.0], [4.0, 4.0, 0.0, 1.0]])
b_eq = np.array([60.0, 60.0])

x0_bounds = (0, None)
x1_bounds = (0, 6.0)
x2_bounds = (-np.inf, 0.5)  # +/- np.inf can be used instead of None
x3_bounds = (-3.0, None)

bounds = [x0_bounds, x1_bounds, x2_bounds, x3_bounds]

result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

print(result)
