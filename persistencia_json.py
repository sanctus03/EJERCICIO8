import persistencia_json as RB
lista_coches = []
Nombre_documento = input("Nombre del documento: ")
while True:
    coche = {}
    marca = input("Marca de coche: ")
    if marca == "fin":
        break
    coche["Marca Coche"] = marca
    coche["Modelo"] = input("Modelo: ")
    coche["Combustible"] = input("Combustible: ")
    coche["Cilindrada"] = input("Cilindrada: ")

    lista_coches.append(coche)

RB.store(lista_coches, Nombre_documento)
lista_coches = []
print("Lista coches: \n", lista_coches)

lista_coches = RB.retrieve(Nombre_documento)
print("Lista coches: \n", lista_coches)
