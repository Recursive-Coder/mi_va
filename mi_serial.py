import serial

def leer_serial(cola):
    # Configura el puerto serie. Ajusta los parámetros según tus necesidades.
    ser = serial.Serial('COM3', 115200, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE, xonxoff=False, rtscts=False, dsrdtr=False)

    try:
        while True:
            if ser.in_waiting > 0:
                # Leer la línea desde el puerto serie
                raw_data = ser.readline().strip()

                try:
                    # Decodificar usando UTF-8
                    decoded_data = raw_data.decode('utf-8')

                    # Convertir a ASCII, reemplazando caracteres no ASCII
                    ascii_data = decoded_data.encode('ascii', 'ignore').decode('ascii')

                    # Eliminar caracteres no deseados
                    cleaned_data = ''.join(filter(str.isdigit, ascii_data))  # Mantener solo los dígitos

                    if cleaned_data:
                        print(f"Received data: {cleaned_data}")
                        cola.put(cleaned_data, timeout=0.1)
                   # print(f"Scanned barcode: {ascii_data}")

                except UnicodeDecodeError:
                    print("Error decoding data")
    except KeyboardInterrupt:
        # Cierra el puerto serie cuando se interrumpe el script
        ser.close()
        print("Serial port closed.")

