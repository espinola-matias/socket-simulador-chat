# 🐍 Python Multithreaded Chat (TCP Sockets)

Un sistema de chat en tiempo real basado en consola (CLI), construido desde cero utilizando **Python**, **Sockets** y **Threading**.

Este proyecto demuestra la implementación de una arquitectura **Cliente-Servidor** utilizando el protocolo TCP/IP, gestionando múltiples conexiones simultáneas mediante hilos y asegurando la integridad de los datos con mecanismos de sincronización.

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Características Principales

* **Comunicación Bidireccional:** Mensajería en tiempo real entre múltiples clientes.
* **Arquitectura Multihilo:** Uso de `threading` para manejar múltiples clientes sin bloquear el servidor.
* **Thread Safety:** Implementación de `threading.Lock()` para prevenir condiciones de carrera (Race Conditions) en el acceso a recursos compartidos.
* **Gestión de Recursos:** Uso de `SO_REUSEADDR` para evitar el bloqueo del puerto tras el reinicio del servidor.
* **Broadcast:** Sistema de difusión de mensajes a todos los usuarios conectados.
* **Sanitización Básica:** Manejo de desconexiones abruptas y codificación UTF-8.

## 🛠️ Arquitectura

El sistema funciona mediante un socket servidor que escucha conexiones entrantes. Por cada nueva conexión, se instancia un hilo dedicado (`Thread`) que gestiona la comunicación con ese cliente específico, permitiendo que el hilo principal siga aceptando nuevos usuarios.

```mermaid
graph TD
    S[Servidor] -->|Acepta Conexión| C1[Cliente 1]
    S -->|Acepta Conexión| C2[Cliente 2]
    S -->|Acepta Conexión| C3[Cliente 3]
    
    C1 -- Envía Mensaje --> S
    S -- Broadcast (Reenvío) --> C2
    S -- Broadcast (Reenvío) --> C3