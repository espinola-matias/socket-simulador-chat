import socket
import threading
import time

salir_cliente = False

# hilo de recibir mensajes en paralelo
def recibir_mensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode()

            if mensaje == "El servidor a cerrado la conexion":
                print("El servidor finalizo las conexiones")
                break
            else:
                print(mensaje)
        except:
            if not salir_cliente:
                print("Error al recibir mensajes")
            break
    cliente.close()