import serial
import time

# Configura el puerto serial (reemplaza 'COMx' con el número de tu puerto)
ser = serial.Serial('COM3', 115200, timeout=1)  # Ejemplo con COM3, cambia según tu puerto

# Datos DMX (512 canales)
data = [0] * 512  # Inicializa todos los canales a 0 (apagados)
data[2] = 255  # Canal 1 al máximo (255)

# Enviar el encabezado DMX y los canales
# El encabezado 0x7E es estándar para la mayoría de adaptadores USB-DMX
# el segundo parametro son los bytes enviados
ser.write(b'\x7E\x06\x01' + bytearray(data))  # 0x7E es el comando de inicio DMX


# Esperar para ver el resultado
time.sleep(1)

# Cerrar el puerto después de enviar los datos
ser.close()
