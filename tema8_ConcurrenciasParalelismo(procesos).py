from time import sleep
from multiprocessing import Process, Pipe
from multiprocessing import Pool
from multiprocessing import Lock
from threading import Barrier, Thread
from random import randint
from threading import Thread, Semaphore, current_thread
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

# EJECUTAMOS DOS FUNCIONES IGUALES
# NO SON NI HILOS NI PROCESOS
"""
print("SEQUENTIAL PROCESSING")
start = time.perf_counter()     # cuenta la cantidad de tiempo

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done Sleeping...{seconds}')

# si estamos en el proceso del main ponemos esto:
if __name__ == '__main__':      # se ejecuta cuando el proceso principal es el del main (el más tabulado a la izq)
    do_something(1)
    do_something(1)

    finish = time.perf_counter()    # todo lo que dura desde q haces el start hasta que haces el finish

    print(f'Finished in {round(finish-start, 2)} second(s)')
"""


# USING POOL CON PROCESOS
"""
def worker(x):
    print("In worker with: ", x)
    sleep(2)
    return x*x

if __name__ == '__main__':
    print("USING POOL CON PROCESOS")
    with Pool(processes=4) as loquequiera:  # um procesos = 4
        print(loquequiera.map(worker, [0,1,2,3,4,5,6]))   # map = recorrer toda la lista
"""

# PIPE IN ACTION 1
"""
print("PIPE_IN_ACTION 1")
def worker(conn):
    print('Awake, waiting for data')
    data = conn.recv()  # guardamos en data lo que el proceso va a recibir
    sleep(1)            # espera a recibir la información
    data = data ** 2    # data va a devolver el cuadrado
    conn.send(data)     # enviamos data de nuevo al proceso


if __name__ == '__main__':
    # creamos el proceso
    print('Main - starting, creating the Pipe')
    main_connection, worker_connection = Pipe()     # creamos la conexión
    print('Main - setting up the process')
    p = Process(target=worker, args=(worker_connection,))
    print('Main - starting process')
    p.start()                   # iniciamos el proceso
    sleep(1)                    # espera (mientras la función se ejecuta)
    main_connection.send(3)     # mandamos a la función el dato
    result = main_connection.recv()     # metemos en el result el valor que vamos a recibir de la otra función
    print(result)               # imprimimos el resultado
"""


# PIPE IN ACTION 2
"""
def worker(conn):
    print('Worker - started now sleeping for 1 second')
    sleep(1)
    print('Worker - sending data via Pipe')
    conn.send('hello')
    print('Worker - closing worker end of connection')
    conn.close()

print('Main - starting, creating the Pipe')
main_connection, worker_connection = Pipe()
print('Main- setting up de process')
p = Process(target=worker, args=(worker_connection,))
print('Main - starting the process')
p.start()
print('Main - wait for a response from the child process')
print(main_connection.recv())
print('Main - closing parent process end of connection')
main_connection.close()
print('Main - Done')
"""

# BARRERAS CON HILOS (FUNCIONA IGUAL QUE CON PROCESOS)
"""
print('BARRERAS CON HILOS 1')
# creamos una función y le pasamos un mensaje y la barrera
def print_it(msg, barrier):
    print('print_it for:', msg)
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
    sleep(randint(1, 6))                    # hace un sleep de un num al azar entre 1 y 6
    print('Wait for barrier with:', msg)
    barrier.wait()  # hace que el hilo empuje el muro para que se caiga y se quedan aqui esperando los hilos
                    # que ya han empujado
    # Una vez se haya caído el muro, se ejecuta el siguiente print
    print('Returning from print_it:', msg)  # TODOS los hilos que existan imprimen esta línea a la vez y ACABA
        # si fuesen 15 hilos en total y se necesitasen 3 para destruir la barrera, sólo se imprimiría 3 veces

def callback():
    print('\nCallback Executing')

def main():
    print('Main - Starting')

    # sólo tenemos un objeto barrier que hemos asignado a 3 hilos
    barrier = Barrier(2, callback)                          # creamos el objeto barrera (lo llamamos como queramos)
    # tiene dos parámetros:
    #   El num de veces que se tiene que ejecutar barrier.wait para que se destruya la barrera
    #   Callback, función que se va a ejecutar una vez se haya abierto la barrera

    # CREAMOS 3 HILOS (puede haber 15 hilos, aunque para tirar la barrera se necesiten 4). Los iniciamos
    t1 = Thread(target=print_it, args=('A', barrier))
    t2 = Thread(target=print_it, args=('B', barrier))
    t3 = Thread(target=print_it, args=('C', barrier))
    t1.start()
    t2.start()
    t3.start()
    print('\nMain - Done')      # esto se imprime independiente porque es del main y el main va por su cuenta

if __name__ == '__main__':
    main()
"""
# BARRERAS CON HILOS 2
"""
print("BARRERAS CON HILOS 2")
def print_it(msg, barrier):
    print('print_it for:', msg)
    sleep(msg)
    barrier.wait()
    sleep(msg)
    print('Fin hilo',msg)

def callback():
    print('\nCallback Executing')
def main():
    print('Main - Starting')
    barrier = Barrier(3, callback)
    t1 = Thread(target=print_it, args=(1,
    barrier))
    t2 = Thread(target=print_it, args=(2,
    barrier))
    t3 = Thread(target=print_it, args=(3,
    barrier))
    t4 = Thread(target=print_it, args=(4,
    barrier))
    t5 = Thread(target=print_it, args=(5,
    barrier))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

if __name__ == '__main__':
    main()
"""


# LOCK (HILOS)
"""
print('LOCK HILOS')
def f(lk, i):
    lk.acquire()        # pasa un hilo se bloquea
    try:
        print('hola', i)
    finally:
        lk.release()    # termina y se vuelve a abri para que pasen mas hilos

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
"""

# SEMÁFOROS
"""
print('SEMÁFOROS')
def worker(semaphore):
    with semaphore:
        print(current_thread().name + " - entered")
        sleep(0.5)
        print(current_thread().name + " - exiting")

print('MainThread - Starting')

semaphore = Semaphore(2) # marcamos el numero de hilos que pueden entrer a la vez
# creamos 5 hilos
for i in range(0, 5):
    thread = Thread(name='T' + str(i), target=worker, args=(semaphore,))
    thread.start()

print('MainThread - Done')
"""

# QUEUE (PROCESOS)
# (lo mismo que pipes pero con put y get)
"""
print("QUEUE")
def worker(queue):
    print('Worker - going to sleep')
    sleep(2)
    print('Worker - woken up and putting data on queue')
    queue.put('Hello World')

def main():
    print('Main - Starting')
    queue = Queue()
    p = Process(target=worker, args=(queue,))
    print('Main - Starting the process')
    p.start()
    print('Main - waiting for data')
    print(queue.get())
    print('Main - Done')

if __name__ == '__main__':
    main()
"""
""
# FUTUROS (POOL)
def worker(msg):
    for i in range(0,10):
        print(msg,end='', flush=True)
        sleep(1)
    return True
if __name__ == '__main__':
    print('FUTUROS')
    print('Starting...')
    pool = ProcessPoolExecutor(3)
    future1 = pool.submit(worker, 'a')
    future2 = pool.submit(worker, 'B')
    future3 = pool.submit(worker, 'C')
    future4 = pool.submit(worker, 'D')
    print('\nfuture4.result():', future4.result())
    print('All Done')