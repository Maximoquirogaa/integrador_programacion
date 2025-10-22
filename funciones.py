import csv
import math 

def BusquedaPais(busqueda):
    encontrado=False
    with open("paises_info_espanol.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if busqueda in linea:
                partes = linea.strip().split(",")
                print(f"\nPais encontrado: {partes[0]}\nPoblación: {partes[1]}\nSuperficie: {partes[2]}\nContinente: {partes[3]}")
                encontrado=True
        if not encontrado:
            print("No se encontro ningun pais.")

def OrdenarPorNombre():
    nombres=[]
    with open("paises_info_espanol.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            nombres.append(partes[0])
        
        #Odernar alfabeticamente ignorando mayusculas y minusculas
        nombres.sort(key=str.lower)

        for i in nombres:
            print(i)

def Ordenar(tipo):
    if tipo=="poblacion":
        parte=1
    elif tipo=="superficie_a" or tipo=="superficie_d":
        parte=2
    paises = []

    with open("paises_info_espanol.csv", "r", encoding="utf-8") as archivo:
        next(archivo)  # Saltar encabezado

        for linea in archivo:
            partes = linea.strip().split(",")
            try:
                nombre = partes[0]
                valor = int(partes[parte])
                paises.append((nombre, valor))
            except ValueError:
                print(f"Error con la línea: {linea}")
    if tipo=="superficie_d" or tipo=="poblacion":
        # Ordenar por valor de mayor a menor
        paises_ordenados = sorted(paises, key=lambda x: x[1], reverse=True)
    else:
        paises_ordenados = sorted(paises, key=lambda x: x[1], reverse=False)

    # Imprimir cada país con su valor
    for nombre, valor in paises_ordenados:
        print(f"{nombre}: {valor}")



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
    return filtros


def mostrar_estadisticas(archivo_csv):
        
    pais_mayor_pob = ""
    mayor_pob = 0
    
    pais_menor_pob = ""
    menor_pob = math.inf  
    
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

        if conteo_paises > 0:
            promedio_pob = total_poblacion / conteo_paises
            promedio_sup = total_superficie / conteo_paises

            print("--- Estadísticas Globales ---")
            
            print(f"País con Mayor Población: {pais_mayor_pob} ({mayor_pob:,.0f})")
            print(f"País con Menor Población: {pais_menor_pob} ({menor_pob:,.0f})")
            print(f"Promedio de Población: {promedio_pob:,.0f} habitantes")
            print(f"Promedio de Superficie: {promedio_sup:,.0f} km²")
            
            print("\n---  Conteo de Países por Continente ---")
            # Ordenamos el diccionario alfabéticamente por continente
            for continente, cantidad in sorted(conteo_continentes.items()):
                print(f" - {continente}: {cantidad} países")
        else:
            print("No se encontraron datos válidos para calcular estadísticas.")

    except FileNotFoundError:
        print(f"Error CRÍTICO: No se encontró el archivo '{archivo_csv}'")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante las estadísticas: {e}")

def filtro():

    archivo_entrada = "paises_info_espanol.csv"
    archivo_salida = "filtrado_de_paises.csv"
    paises_encontrados = 0  


    filtros = obtener_filtros_usuario()

    try:
        with open(archivo_entrada, mode='r', encoding="utf-8", newline='') as archivo_lectura:
            with open(archivo_salida, mode='w', encoding="utf-8", newline='') as archivo_escritura:
                
                lector_csv = csv.DictReader(archivo_lectura)
                
                if not lector_csv.fieldnames:
                    print(f"Error: El archivo '{archivo_entrada}' está vacío.")
                    exit()

                escritor_csv = csv.DictWriter(archivo_escritura, fieldnames=lector_csv.fieldnames)
                escritor_csv.writeheader()
                
                print(f"\n--- 2. Iniciando filtrado... ---")
                print(f"  Continente = {filtros['continente']}")
                print(f"  Población = {filtros['pob_min']} a {filtros['pob_max']}")
                print(f"  Superficie = {filtros['sup_min']} a {filtros['sup_max']}")
                print("---------------------------------")

                for fila in lector_csv:
                        poblacion_int = int(fila['población'])
                        superficie_int = int(fila['superficie'])
                        continente_str = fila['continente']
                        
                        filtro_continente = continente_str == filtros['continente']
                        filtro_poblacion = (poblacion_int >= filtros['pob_min']) and (poblacion_int <= filtros['pob_max'])
                        filtro_superficie = (superficie_int >= filtros['sup_min']) and (superficie_int <= filtros['sup_max'])

                        if filtro_continente and filtro_poblacion and filtro_superficie:
                            escritor_csv.writerow(fila)
                            paises_encontrados += 1
                
                print(f"\nFiltrado completado.")
                if paises_encontrados == 0:
                    print(">> No se encontraron países que coincidan con todos los criterios.")
                else:
                    print(f">> Se encontraron {paises_encontrados} países que coinciden.")
                    print(f"Resultados guardados en '{archivo_salida}'.")

    except FileNotFoundError:
        print(f"Error CRÍTICO: No se encontró el archivo '{archivo_entrada}'")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")