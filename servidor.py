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

    except:
        print(f"Error con el cliente {direccion}")
    finally:
        cliente.close()
        if cliente in clientes_activos:
            del clientes_activos[cliente]

# Hilo del servidor con manejo de comandos, al morir el cliente pasa a ser false 
def administrar_servidor(servidor):
    while True:
        comando = input("Comando del servidor ('salir' para apagar): \n")
        if comando.strip().lower() == "salir":
            print("Cerrando el servidor")
            for cliente in list(clientes_activos):
                try:
                    cliente.send("El servidor a cerrado la conexion".encode()) 
                except Exception as error:
                    print(f"Error al cerrar cliente: {error}")
                finally:
                    cliente.close()
                    
            servidor.close()
            break

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("localhost", 9999))
    servidor.listen(40)
    print("Servidor esperando conexiones")

    threading.Thread(target=administrar_servidor, args=(servidor,)).start()

    while True:
        try:
            cliente, direccion = servidor.accept()
            hilo = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
            hilo.start()
        except OSError:
            break