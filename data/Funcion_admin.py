import json
def ingresar_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit(): 
            return valor
        else:
            print("Por favor, ingrese un valor numérico.")

def creacion_usuario():
    with open("data/modulos/clientes.json", "r") as outfile:
        clientes = json.load(outfile)

    cliente_nuevo={}
    ID_max = max([cliente_nuevo["ID"] for cliente_nuevo in clientes["Clientes"]],default= 0)
    cliente_nuevo["ID"] = ID_max + 1
    cliente_nuevo["N_documento"] = ingresar_numero("Ingrese el Numero de documento")
    cliente_nuevo["nombres"] = input("Ingrese los Nombres: ")
    cliente_nuevo["apellidos"] = input("Ingrese los Apellidos: ")
    cliente_nuevo["telefono"] = ingresar_numero("Ingrese el numero Telefono: ")
    cliente_nuevo["Fijo"] = ingresar_numero("Ingrese el Numero Fijo: ")
    cliente_nuevo["direccion"] = input("Ingrese la Direccion: ")
    cliente_nuevo["Categoria"]= ""

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
        clientes= clientes["Clientes"]
    cliente_ID = int(input("Ingrese el id del usuario al que quiere actualizar su info: "))
    for cliente in clientes:
        if cliente["ID"] == cliente_ID:
            N_documento = ingresar_numero("Ingre el nuevo N_documento: ")
            nombres = input("Ingresa los nuevos nombres: ")
            apellidos = input("Ingresa los nuevos apellidos: ")
            telefono = ingresar_numero("Ingresa el nuevo telefono: ")
            Fijo = ingresar_numero("Ingresa el nuevo Fijo: ")
            direccion = input("Ingresa la nueva direccion: ")
            
            cliente["N_documento"] = N_documento
            cliente["nombres"] = nombres
            cliente["apellidos"] = apellidos
            cliente["telefono"] = telefono
            cliente["Fijo"] = Fijo
            cliente["direccion"] = direccion
    with open( "data/modulos/clientes.json", "w") as outfile:
        json.dump(clientes, outfile,indent=4)

def asignarle_categoria()