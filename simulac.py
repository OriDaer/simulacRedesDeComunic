class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def enviar_mensaje(self, mensaje):
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje, self)

    def recibir_mensaje(self, mensaje, remitente):
        print(f"{self.nombre} recibió: '{mensaje}' de {remitente.nombre}")

# creo los nodos
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente1")
cliente2 = Nodo("Cliente2")
cliente3 = Nodo("Cliente3")

# hago las conexiones entre ellos
servidor.agregar_conexion(cliente1)
cliente1.agregar_conexion(servidor)
servidor.agregar_conexion(cliente2)
cliente2.agregar_conexion(servidor)
servidor.agregar_conexion(cliente3)
cliente3.agregar_conexion(servidor)
servidor.enviar_mensaje("Mensaje de prueba para todos los clientes")