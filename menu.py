import data.Funcion_admin as func
def menu_principal():
    print("Bienvenido al Sistema de Movistar ¿Que desea hacer?")
    print("1.Admin")
    print("2.Servicios")
    print("3.Reportes")
    print("4.Bonificaiones")
    print("5.Salir")

def menu_de_usuarios():
    print("Bienvenido al menu de usuarios ¿que desea hacer?")
    print("1.Crear Usuario")
    print("2.Mostrar informacion de los usuario")
    print("3.Actualizar informacion de los usuarios")
    print("4.Eliminar usuario")
    print("5.Atras")

def main():
    while True:
        menu_principal()
        opcion = input("Ingrese una opcion: ")
        if opcion == '1':
            while True:
                menu_de_usuarios()
                opcion = input("Ingrese una opcion: ")
                if opcion == '1':
                    func.creacion_usuario()
                elif opcion == '2':
                    func.mostrar_infousuarios()
                elif opcion == '3':
                    func.actualizar_usuario()
                elif opcion == '4':
                    func.eliminar_usuario()
                elif opcion == '5':
                    break
                else:
                    print("Opcion no valida")
        # elif opcion == '2':
        #     func.mostrar_servicios()
        # elif opcion == '3':
        #     func.mostrar_reportes()
        # elif opcion == '4':
        #     func.mostrar_bonificaciones()
        elif opcion == '5':
            break
        else:
            print("Opcion no valida")

main()