class City:
    def __init__(self, name, veterinarians):
        self.name = name
        self.veterinarians = veterinarians


class Veterinarian:
    def __init__(self, name):
        self.name = name
        self.applied_vaccines = 0


def add_city(cities):
    name = input("Ingrese el nombre de la ciudad: ")
    veterinarians = []
    cities.append(City(name, veterinarians))
    print(f"Ciudad '{name}' agregada.")


def add_veterinarian(city):
    name = input("Ingrese el nombre del veterinario: ")
    veterinarian = Veterinarian(name)
    city.veterinarians.append(veterinarian)
    print(f"Veterinario '{name}' agregado a la ciudad '{city.name}'.")


def record_vaccines(city):
    print("Veterinarios en", city.name)
    idx: object
    for idx, vet in enumerate(city.veterinarians, start=1):
        print(f"{idx}. {vet.name}")

    vet_idx = int(input("Seleccione el veterinario (número): ")) - 1
    if 0 <= vet_idx < len(city.veterinarians):
        cantidad = int(input("Ingrese la cantidad de vacunas aplicadas: "))
        city.veterinarians[vet_idx].applied_vaccines += cantidad
        print(f"Se registraron {cantidad} vacunas para el veterinario '{city.veterinarians[vet_idx].name}'.")
    else:
        print("Selección de veterinario inválida.")


def mostrar_ciudades(cities):
    print("Lista de ciudades:")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city.name}")


def mostrar_total_vacunas_por_ciudad(city):
    total_vacunas = sum(vet.applied_vaccines for vet in city.veterinarians)
    print(f"Total de vacunas aplicadas en {city.name}: {total_vacunas}")


def mostrar_total_vacunas_por_veterinario(city):
    print("Veterinarios en", city.name)
    for idx, vet in enumerate(city.veterinarians, start=1):
        print(f"{idx}. {vet.name} - Total de vacunas: {vet.applied_vaccines}")


def main():
    cities = []

    while True:
        print("\n1. Agregar Ciudad")
        print("2. Agregar Veterinario a Ciudad")
        print("3. Registrar Vacunas para Veterinario en Ciudad")
        print("4. Mostrar Ciudades")
        print("5. Mostrar Total de Vacunas por Ciudad")
        print("6. Mostrar Total de Vacunas por Veterinario en Ciudad")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            add_city(cities)  # Llama a la función para agregar una ciudad a la lista.
        elif opcion == "2":
            mostrar_ciudades(cities)  # Muestra la lista de ciudades existentes.
            ciudad_idx=int(input("Seleccione la ciudad (numero):")) -1
            if 0 <= ciudad_idx < len(cities):
                add_veterinarian(
                    cities[ciudad_idx])  # Llama a la función para agregar un veterinario a la ciudad seleccionada.
            else:
                print("Selección de ciudad inválida.")
        elif opcion == "3":
            mostrar_ciudades(cities)
            ciudad_idx = int(input("Seleccione la ciudad (número): ")) - 1
            if 0 <= ciudad_idx < len(cities):
                record_vaccines(
                    cities[ciudad_idx])  # Llama a la función para registrar vacunas para un veterinario en una ciudad.
            else:
                print("Selección de ciudad inválida.")
        elif opcion == "4":
            mostrar_ciudades(cities)  # Muestra la lista de ciudades existentes.
        elif opcion == "5":
            mostrar_ciudades(cities)
            ciudad_idx = int(input("Seleccione la ciudad (número): ")) - 1
            if 0 <= ciudad_idx < len(cities):
                mostrar_total_vacunas_por_ciudad(
                    cities[ciudad_idx])  # Muestra el total de vacunas aplicadas en una ciudad.
            else:
                print("Selección de ciudad inválida.")
        elif opcion == "6":
            mostrar_ciudades(cities)
            ciudad_idx = int(input("Seleccione la ciudad (número): ")) - 1
            if 0 <= ciudad_idx < len(cities):
                mostrar_total_vacunas_por_veterinario(
                    cities[ciudad_idx])  # Muestra el total de vacunas aplicadas por veterinario en una ciudad.
            else:
                print("Selección de ciudad inválida.")
        elif opcion == "7":
            break  # Sale del bucle while, terminando el programa.
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()  # Llama a la función principal del programa.
