import json
def solo_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("No es un numero")

def creacion_usuario():
    with open("data/modulos/clientes.json", "r") as outfile:
        clientes = json.load(outfile)

    cliente_nuevo={}
    ID_max = max([cliente_nuevo["ID"] for cliente_nuevo in clientes["Clientes"]],default= 0)
    cliente_nuevo["ID"] = ID_max + 1
    cliente_nuevo["N_documento"] = solo_numero("N_documento: ")
    cliente_nuevo["nombres"] = input("Nombres: ")
    cliente_nuevo["apellidos"] = input("Apellidos: ")
    cliente_nuevo["telefono"] = solo_numero("Telefono: ")
    cliente_nuevo["Fijo"] = solo_numero("Fijo: ")
    cliente_nuevo["direccion"] = input("Direccion: ")

    clientes["Clientes"].append(cliente_nuevo)

    with open("data/modulos/clientes.json", "w") as outfile:
        json.dump(clientes, outfile, indent=4)
def mostrar_infousuarios():
    with open("data/modulos/clientes.json", "r") as outfile:
        clientes = json.load(outfile)

    for cliente in clientes["Clientes"]:
        print(cliente)
def actualizar_usuario():
    with open("data/modulos/clientes.json", "r") as outfile:
        clientes = json.load(outfile)
    cliente_ID = int(input("Ingrese el id del usuario al que quiere actualizar su info: "))
    for i in clientes:
        if Clientes["ID"] == cliente_ID:
            N_documento = input("Ingre el nuevo N_documento: ")
            nombres = input("Ingresa los nuevos nombres: ")
            apellidos = input("Ingresa los nuevos apellidos: ")
            telefono = solo_numero("Ingresa el nuevo telefono: ")
            Fijo = solo_numero("Ingresa el nuevo Fijo: ")
            direccion = input("Ingresa la nueva direccion: ")
            
