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

# Hilo de clientes 
def manejar_cliente(cliente, direccion): 
    try:
        nombre = cliente.recv(1024).decode()
        clientes_activos[cliente] = nombre
        print(f"{nombre} se ha conectado desde {direccion}")
        mensajes_enviados(f"{nombre} se ha unido al chat", cliente)
        cliente.send("~ Para salir del chat escribe ('salir')\n".encode())
        cliente.send("~ Conectado al chat puedes iniciar una conversacion\n".encode())

        while True:
            mensaje = cliente.recv(1024).decode()
            if mensaje.strip().lower() == "salir":
                print(f"{nombre} se ha desconectado")
                mensajes_enviados(f"{nombre} salio del chat", cliente)
                break
            else:
                mensajes_enviados(f"{nombre}: {mensaje}", cliente)