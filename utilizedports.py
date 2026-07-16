import serial
import serial.tools.list_ports

# Obtener los puertos disponibles
puertos = serial.tools.list_ports.comports()

# Verificar cada puerto
for puerto in puertos:
    try:
        # Intentar abrir el puerto (abrirlo en modo de solo lectura)
        print(f"Verificando puerto: {puerto.device}")
        ser = serial.Serial(puerto.device, 9600, timeout=1)
        ser.close()  # Si se puede abrir, cerramos el puerto
        print(f"Puerto {puerto.device} no está en uso.")
    except serial.SerialException:
        # Si no se puede abrir el puerto, significa que está en uso
        print(f"Puerto {puerto.device} está en uso o no disponible.")
