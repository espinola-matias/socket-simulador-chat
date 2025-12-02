import socket
import threading

# diccionario de clientes activos, socket:nombre del cliente
clientes_activos = {} 

# Boadcast para el reenvio de mensajes a los demas integrantes del chat 
def mensajes_enviados(mensaje, cliente_emisor):
    for cliente in clientes_activos:
        if cliente != cliente_emisor:
            try:
                cliente.send(mensaje.encode())
            except:
                cliente.close()
                del clientes_activos[cliente]
