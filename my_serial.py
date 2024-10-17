import estado
import serial


def read_serial(cola):
    puerto = serial.Serial('COM3', 115200, timeout=1)
    try:
        while True:
            if puerto.in_waiting > 0:
                datos_bytes = puerto.readline().strip()
                datos_string = datos_bytes.decode('utf-8', 'ignore')
                cola.put(datos_string[1:], timeout=0.1)
            if estado.grabando:
                puerto.rts = True
            else:
                puerto.rts = False
            print(f'grabando? {estado.grabando}')
    except KeyboardInterrupt:
        print('Programa cancelado por el usuario')
    finally:
        puerto.close()


def read_serial_pila(pila):
    puerto = serial.Serial('COM3', 115200, timeout=1)
    try:
        while True:
            if puerto.in_waiting > 0:
                datos_bytes = puerto.readline().strip()
                datos_string = datos_bytes.decode('utf-8', 'ignore')
                pila.clear()
                pila.append(datos_string[1:])
            if estado.grabando:
                puerto.rts = True
            else:
                puerto.rts = False
            print(f'grabando? {estado.grabando}')
    except KeyboardInterrupt:
        print('Programa cancelado por el usuario')
    finally:
        puerto.close()


def read_serial_variable():
    puerto = serial.Serial('COM3', 57600, timeout=1)
    try:
        while True:
            if puerto.in_waiting > 0:
                print('entro al if')
                datos_bytes = puerto.readline().strip()
                datos_string = datos_bytes.decode('utf-8', 'ignore')
                print(f'datos_string: {datos_string}')
                estado.cubeta = datos_string[1:]
                print(f'cubeta:{estado.cubeta}')
            if estado.grabando:
                puerto.rts = True
            else:
                puerto.rts = False
            print(f'grabando? {estado.grabando}')
    except KeyboardInterrupt:
        print('Programa cancelado por el usuario')
    finally:
        puerto.close()
