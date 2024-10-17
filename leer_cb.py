
def leer_cb(cola):
    while True:
        codigo = input()
        if codigo:
            cola.put(codigo, timeout=0.1)
