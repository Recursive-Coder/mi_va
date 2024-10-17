import requests

# Coordenadas del primer punto (latitud, longitud)
punto1 = (-34.57720, -60.94976)

# Coordenadas del segundo punto (latitud, longitud)
punto2 = (-32.94503, -60.66141)  # Roma, Italia

# URL de la API de OSRM
url = f"http://router.project-osrm.org/route/v1/driving/{punto1[1]},{punto1[0]};{punto2[1]},{punto2[0]}?overview=false"

# Hacer la solicitud HTTP
response = requests.get(url)
data = response.json()

# Extraer la distancia en metros
distancia_metros = data['routes'][0]['distance']

# Convertir la distancia a kilómetros
distancia_km = distancia_metros / 1000

# Mostrar la distancia
print(f"La distancia es {distancia_km:.2f} km")
