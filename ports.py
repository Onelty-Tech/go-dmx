import serial.tools.list_ports

# Lista todos los puertos disponibles
puertos = serial.tools.list_ports.comports()

# Imprime la lista de puertos disponibles y sus detalles
for puerto in puertos:
    print(f"Puerto: {puerto.device}, Descripción: {puerto.description}, ID: {puerto.hwid}")
