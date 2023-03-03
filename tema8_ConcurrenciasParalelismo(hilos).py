# TEMA 8 CONCURRENCIAS Y PARALELISMO

from threading import Thread, local
# esta función suspende (hace esperar) a la ejecución del hilo actual por un tiempo dado.
from time import sleep
from multiprocessing import Pool

# HILOS
# Permite que se ejecuten varias operaciones en el mismo espacio de proceso.
# Cada ciclo de ejecución es el hilo.
print("Hilos, ejemplo 1:")

def simple_worker():        # definimos la función que va a ejecutar el hilo
    print("hello")

# Crear un nuevo hilo y empezarlo.
# El hilo hará el run de la función simple_worker.
hilo1 = Thread(target=simple_worker)    # target para decir cuál es el nombre de la función a la que va a llamar.
hilo1.start()       # se inicia el hilo


print("\n\nHilos, ejemplo 2:")
def worker():
    for i in range(0,10):
        print('.', end='', flush=True)  # flush cleans the internal buffer
        sleep(0.2)      # paramos el proceso por 2 segundos

print('Starting')

# creamos el hilo y lo referenciamos con la función creada
t = Thread(target=worker)
# empezamos el hilo
t.start()

# si el hilo está en modo demonio, necesitamos "join", para que el hilo termine antes de que lo haga el principal.
# espera hasta que el hilo se complete
t.join()

print('\nDone')


print("\n\nHilos, ejemplo 3:")
def worker_in():
    for i in range(0,10):
        print('*', end='', flush=True)
        sleep(0.2)

def worker_out():
    t_in = Thread(target=worker_in, name='in')
    # empezamos el hilo en worker_in
    t_in.start()
    for i in range(0,10):
        print('.', end='', flush=True)
        sleep(0.2)

print('Starting')
t_out = Thread(target=worker_out(), name='out')
t_out.start()
t_out.join()

print('\nDone')


print("\n\nCREATING  THREAD")
"""
    Define two workers:
    one that prints dots every second (total 5 dots), 
    and another one that prints dashes every 2 seconds (total 5 dashes).
    Instantiate two threads for these two workers. 
    The main program should:
    1) Start both threads. 
    2) Join both threads to the main program, immediately after.
    3) Sleep for two seconds. 
    4) Print \nDone.
"""
def worker_dots():
    for i in range(0,5):
        print('.', end='', flush=True)
        sleep(1)

def worker_dashes():
    for i in range(0,5):
        print('-', end='', flush=True)
        sleep(2)

worker1 = Thread(target=worker_dots())
worker2 = Thread(target=worker_dashes())

worker1.start()
worker2.start()

worker1.join()
worker2.join()

print('\nDone')


print("\n\nHilos, ejemplo 4:")
def worker(msg):
    for i in range(0,10):
        print(msg, end='', flush=True)
        sleep(1)

print('Starting')
t1 = Thread(target=worker, args='a', name='t1')
t2 = Thread(target=worker, args='b', name='t2')
t3 = Thread(target=worker, args='c', name='t3')
# sigue el orden la primera vez que les llamas
t1.start()
t2.start()
t3.start()
sleep(0.3)
print('Done')   # por eso se imprime el done


print("\n\nHilos, ejemplo 5 (run y subclases):")
# define a subclass of Thread
class WorkerThread(Thread):
    # incializamos el init a None
    def __init__(self, daemon=None, target=None, name=None):
        # como queremos el init de la clase a la que nos referimos, lo copiamos con el 'super'
        super().__init__(daemon=daemon, target=target, name=name)

    # override the run() - sobreecribe el run
    def run(self):
        for i in range(0,10):
            print('.', end='', flush=True)

print('Starting')
t = WorkerThread()  # no le especificamos el target, porque la función run está reservada
# si no le pasamos ninguna función y existe 'run' lo ejecuta
# la subclase sólo tiene el __init__ y la función run, que puedo editar como yo quiera
t.start()
print('\nDone')

"""
"""
print("\n\nHilos, ejemplo 6 (daemon threads):")
def worker(msg):
    for i in range(0,10):
        print(msg, end='', flush=True)
        sleep(1)

print('Starting')

# Create a daemon thread
d = Thread(daemon=True, target=worker, args='C')
d.start()

sleep(5)
print('Done')

print("\n\n\nHILOS: POOL")
def worker(x):
    print('In worker with: ', x)
    sleep(4)
    return x * x

if __name__ == '__main__':
    with Pool(threads=4) as pool:
        print(pool.map(worker, [0, 1, 2, 3, 4, 5]))