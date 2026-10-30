def main():
    print("==== BIENVENIDO AL SISTEMA DE REGISTRO DEL HOSPITAL =====")

def registro_depacientes(nombre_completo):
    nombres = []
    nombre_completo = input("Ingrese el nombre completo del paciente por favor: ").lower()
    nombres.append(nombre_completo)
    if nombres(len) > 10:
        print("Error, la cantidad de nombres en la lista debe ser menor o igual a 10.")
    else:
        print(nombres)