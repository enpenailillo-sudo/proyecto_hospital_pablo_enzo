def main():
    print("==== BIENVENIDO AL SISTEMA DE REGISTRO DEL HOSPITAL =====")
    print("1.- Registrar pacientes ")
    print("2.- Registrar lista de trabajadores")
    print("3.- Registrar medicamentos.")
    print("4.- Salir")
    print("=============================================================")
def leer_opcion(opcion):
    while True:
        try:
            opcion = int(input("Opcion del 1 al 4: "))
            if opcion < 1 or opcion > 4:
                print("Error la opcion debe ser del 1 al 4.")
                continue
        except ValueError:
            print("Error, los valores ingresados no son válidos.")
            continue
        match opcion:
            case 1:
                print("==== REGISTRAR PACIENTES ======")
                registro_depacientes()
            case 2:
                print("==== REGISTRAR LISTA DE TRABAJADORES====")
                registro_trabajadores()
            case 3:
                print("==== REGISTRAR MEDICAMENTOS ====")
                registrar_medicamentos()
            case 4:
                print("==== SALIENDO DEL PROGRAMA =====")
                opcion_salir()
def registro_depacientes(nombre_completo):
    nombres = []
    nombre_completo = input("Ingrese el nombre completo del paciente por favor: ").lower()
    nombres.append(nombre_completo)
    if len(nombres) > 10:
        print("Error, la cantidad de nombres en la lista debe ser menor o igual a 10.")
    else:
        print(nombres)

def registro_trabajadores(nombre_trabajadores):
    trabajadores_lista = []
    nombre_trabajadores = input("Ingres el nombre del trabajador: ")
    trabajadores_lista.append(nombre_trabajadores)
    if len(nombre_trabajadores) > 20:
        print("Error,la cantidad de nombres en la lista debe ser menor o igual a 20.")
    else:
        print(nombre_trabajadores)

def registrar_medicamentos(medicamentos,farmaco):
    medicamentos = []
    farmaco = input("Ingrese nombre del medicamento: ")
    medicamentos.append(farmaco)
    if len(medicamentos) <= 5:
        print(f"Se han agregado estos medicamentos a la lista: {medicamentos}")
def opcion_salir(salir):
    salir = input("¿Desea salir del programa?: ").lower()
    if salir == "si":
        print("Saliendo....")
    else:
        print("Continuando con el registro de pacientes...")
