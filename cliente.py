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

def conectar_servidor():
    for intento in range(3):
        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            cliente.connect(("localhost", 9999))
            return cliente
        except:
            print(f"No se pudo conectar, reintentando conexion intento {intento + 1} /3")
            time.sleep(1)
    else:
        print("No se logro restablecer la conexion con el servidor")
        exit()