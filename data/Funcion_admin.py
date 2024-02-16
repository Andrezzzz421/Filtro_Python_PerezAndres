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

def asignarle_categoria():
    with open("data/modulos/clientes.json", "r") as outfile:
        clientes = json.load(outfile)
        clientes = clientes["Clientes"]

    while True:
        cliente_ID = input("Ingrese el id del usuario al que quiere asignarle una categoría (o ingrese 'salir' para terminar): ")
        if cliente_ID.lower() == "salir":
            break

        try:
            cliente_ID = int(cliente_ID)
            cliente = next(filter(lambda c: c["ID"] == cliente_ID, clientes))
            break
        except (StopIteration, ValueError):
            print("ID inválido. Intente nuevamente.")

    while True:
        print("Que categoría desea asignarle al usuario?")
        print("1. Nuevo Cliente")
        print("2. Cliente regular")
        print("3. Cliente leal")

        try:
            op = int(input("Ingrese la opción por favor: "))
            if op == 1:
                cliente["Categoria"] = "Nuevo Cliente"
            elif op == 2:
                cliente["Categoria"] = "Cliente regular"
            elif op == 3:
                cliente["Categoria"] = "Cliente leal"
            else:
                print("Opción inválida. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Opción inválida. Intente nuevamente.")

    with open("data/modulos/clientes.json", "w") as outfile:
        json.dump(clientes, outfile, indent=4)