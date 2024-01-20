# principal.py

from numeros import generar_turno_perfumeria, generar_turno_farmacia, generar_turno_cosmeticos

def elegir_area():
    print("Seleccione el área a la que desea dirigirse:")
    print("1. Perfumería")
    print("2. Farmacia")
    print("3. Cosméticos")

    opcion = input("Ingrese el número de su elección: ")
    return opcion

def main():
    turnos_por_area = {"1": generar_turno_perfumeria, "2": generar_turno_farmacia, "3": generar_turno_cosmeticos}

    while True:
        area_elegida = elegir_area()

        if area_elegida in turnos_por_area:
            mensaje_turno = turnos_por_area[area_elegida]()
            print(mensaje_turno)

        seguir = input("¿Desea sacar otro turno? (s/n): ")
        if seguir.lower() != "s":
            print("Gracias por usar nuestro servicio. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
