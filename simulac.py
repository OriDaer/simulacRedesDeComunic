class Nodo:
    def __init__(self, nombre):#Inicializa un nodo con un nombre y una lista vacía de conexiones.
        self.nombre = nombre
        self.conexiones = []
    def agregar_conexion(self, nodo):#Agrega una conexión entre el nodo actual y otro nodo.
        self.conexiones.append(nodo)
    def enviar_mensaje(self, mensaje):#Simula el envío de un mensaje desde el nodo actual a todos sus nodos conectados.
        print(f"{self.nombre} está enviando el mensaje '{mensaje}' a sus conexiones.")
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje, self.nombre)
    def recibir_mensaje(self, mensaje, remitente):#Simula la recepción de un mensaje desde otro nodo
        print(f"{self.nombre} ha recibido el mensaje '{mensaje}' de {remitente}")
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)
mensaje = "Hola, clientes!"
servidor.enviar_mensaje(mensaje)