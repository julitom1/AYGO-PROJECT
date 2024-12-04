import requests
import random

users = ["Yarit", "Laura", "Julian", "Carolina","Gaby", "Cesar", "Angelica","Gina","Milena"]
ages = [25, 25, 26, 29,19, 24, 24, 24,24,24]


# URL completa del API (asegúrate de incluir el endpoint específico)
url = 'https://gmj9fligpi.execute-api.us-east-1.amazonaws.com'
with open("./test.txt", 'r') as file:
    lines = file.readlines()  # Lee todas las líneas y las guarda en una lista
    for line in lines:
        random_number = random.randint(0, len(users) - 1)
        data = {
            'MessageBody': {
                'message': line,
                'edad': ages[random_number],
                'user': users[random_number]
            }
        }

        # Headers para indicar que el cuerpo es JSON
        headers = {'Content-Type': 'application/json'}

        try:
            # Hacer la petición POST con el cuerpo de la solicitud
            response = requests.post(url, json=data, headers=headers)

            # Verificar si la respuesta contiene un cuerpo JSON
            if response.status_code == 200:
                try:
                    print('Petición exitosa:', response)  # Intenta obtener el JSON
                except ValueError:
                    print('La respuesta no es un JSON válido. Respuesta del servidor:', response.text)
            else:
                print(f'Error en la petición. Código de estado: {response.status_code}')
                print(response.text)

        except requests.exceptions.RequestException as e:
            # Manejo de errores en caso de fallo de conexión o problemas de red
            print(f'Error al hacer la solicitud: {e}')
