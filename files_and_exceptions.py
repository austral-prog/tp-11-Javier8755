def read_file_to_dict(filename):
    
    diccionario = {}
    
    with open(filename, "r") as file:
        contenido = file.read()    
        lista1 = contenido.strip().split(";")
        for linea in lista1:
            if linea:
                producto, valor = linea.strip().split(":")
                if producto not in diccionario:
                    diccionario[producto] = [(float(valor))]
                else:
                    diccionario[producto].append((float(valor)))

    return diccionario


def process_dict(data):

    for key, values in data.items():
        suma = 0
        for value in values:
            suma += value
        average = suma/len(values)
        print(f"{key}: ventas totales ${suma:.2f}, promedio ${average:.2f}")
