import csv
import math 

def pedir_numero(mensaje):

    while True:
        try:
            valor_str = input(mensaje)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print("  Error: Ingrese solo números, sin puntos ni comas.")

def obtener_filtros_usuario():

    print("--- 1. Configuración de Filtros ---")

    print("\nPASO 1: Continente")
    continente_input = input("Ingrese el nombre del continente (ej: América): ")
    continente = continente_input.capitalize()

    print("\nPASO 2: Rango de Población ")
    print("A continuación, ingrese el rango de población (solo números).")
    pob_min = pedir_numero("  Población MÍNIMA (ej: 1000000): ")
    pob_max = pedir_numero("  Población MÁXIMA (ej: 50000000): ")
    print(f"Rango de población establecido: {pob_min} a {pob_max}")

    print("\nPASO 3: Rango de Superficie ")
    print("Ingrese el rango de superficie (en km², solo números).")
    sup_min = pedir_numero("  Superficie MÍNIMA km² (ej: 100000): ")
    sup_max = pedir_numero("  Superficie MÁXIMA km² (ej: 5000000): ")
    print(f"Rango de superficie establecido: {sup_min} km² a {sup_max} km²")

    filtros = {
        "continente": continente,
        "pob_min": pob_min,
        "pob_max": pob_max,
        "sup_min": sup_min,
        "sup_max": sup_max
    }
    return 


def mostrar_estadisticas(archivo_csv):
    """
    Lee el CSV completo y calcula estadísticas clave.
    """
    
    
    pais_mayor_pob = ""
    mayor_pob = 0
    
    pais_menor_pob = ""
    menor_pob = math.inf  #
    
    total_poblacion = 0
    total_superficie = 0
    conteo_paises = 0
    conteo_continentes = {}  

    print("\n---  Iniciando Análisis Estadístico ---")
    
    try:
        with open(archivo_csv, mode='r', encoding='utf-8', newline='') as f:
            lector = csv.DictReader(f)

            if not lector.fieldnames:
                print(f"Error: El archivo '{archivo_csv}' está vacío.")
                return  
            for fila in lector:
                try:
                    poblacion_int = int(fila['población'])
                    superficie_int = int(fila['superficie'])
                    nombre_pais = fila['nombre']
                    continente = fila['continente']

                    total_poblacion += poblacion_int
                    total_superficie += superficie_int
                    conteo_paises += 1

                    if poblacion_int > mayor_pob:
                        mayor_pob = poblacion_int
                        pais_mayor_pob = nombre_pais

                    if poblacion_int < menor_pob:
                        menor_pob = poblacion_int
                        pais_menor_pob = nombre_pais

                    conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

                except (ValueError, KeyError, TypeError):
                    pass

        # 8. Calcular promedios (después de terminar el bucle)
        if conteo_paises > 0:
            promedio_pob = total_poblacion / conteo_paises
            promedio_sup = total_superficie / conteo_paises

            # 9. Imprimir todos los resultados
            print("--- Estadísticas Globales ---")
            # Usamos '{:,.0f}' para formatear los números con comas y sin decimales
            print(f"País con Mayor Población: {pais_mayor_pob} ({mayor_pob:,.0f})")
            print(f"País con Menor Población: {pais_menor_pob} ({menor_pob:,.0f})")
            print(f"Promedio de Población: {promedio_pob:,.0f} habitantes")
            print(f"Promedio de Superficie: {promedio_sup:,.0f} km²")
            
            print("\n--- 🌎 Conteo de Países por Continente ---")
            # Ordenamos el diccionario alfabéticamente por continente
            for continente, cantidad in sorted(conteo_continentes.items()):
                print(f" - {continente}: {cantidad} países")
        else:
            print("No se encontraron datos válidos para calcular estadísticas.")

    except FileNotFoundError:
        print(f"Error CRÍTICO: No se encontró el archivo '{archivo_csv}'")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante las estadísticas: {e}")