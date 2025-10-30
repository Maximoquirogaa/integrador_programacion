import csv, math, unicodedata


def quitar_tildes(texto): #Funcion para quitar tildes de los inputs
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto


def BusquedaPais(busqueda):
    # Prevenimos que no se ingresen números
    if any(c.isdigit() for c in busqueda):
        print("\nPor favor no ingrese números.\n")
        return 0

    # Normalizamos la búsqueda (quitamos tildes y pasamos a minúsculas)
    busqueda_normalizada = quitar_tildes(busqueda.lower())

    encontrado = False
    with open("paises_info_espanol.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea_normalizada = quitar_tildes(linea.lower()) #Por cada linea en el archivo, la normalizamos y metemos en una lista.
            if busqueda_normalizada in linea_normalizada:
                partes = linea.strip().split(",")
                print(f"\nPaís encontrado: {partes[0]}\nPoblación: {partes[1]}\nSuperficie: {partes[2]}\nContinente: {partes[3]}")
                encontrado = True

    if not encontrado:
        print("No se encontró ningún país.")


def Ordenar(tipo):
    if tipo=="nombre":
        parte=0
    elif tipo=="poblacion":
        parte=1
    elif tipo=="superficie_a" or tipo=="superficie_d":
        parte=2
    paises = []

    with open("paises_info_espanol.csv", "r", encoding="utf-8") as archivo:
        next(archivo)  # Saltar encabezado
        for linea in archivo:
            partes = linea.strip().split(",") #Cada linea se convierte en una lista con sus respectivos elementos sin espacios.
            try:
                nombre = partes[0]
                poblacion = int(partes[1]) #Partes[1] corresponde a el valor de poblacion en la lista
                superficie = int(partes[2]) #Partes[2] corresponde a el valor de superficie en la lista
                continente = partes[3]
                paises.append((nombre, poblacion, superficie, continente))
            
            except ValueError:
                print(f"Error con la línea: {linea}")

    if tipo=="superficie_d" or tipo=="poblacion":   
        paises_ordenados = sorted(paises, key=lambda x: x[parte], reverse=True)# Ordenar por valor de mayor a menor
    else:
        paises_ordenados = sorted(paises, key=lambda x: x[parte], reverse=False)# Ordenar por valor de menor a mayor

    for nombre, poblacion, superficie, continente in paises_ordenados:
        print(f"\n{nombre}: |  Poblacion: {poblacion} | Superficie: {superficie} | Continente: {continente}")


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
    while True:
        continente_input = input("Ingrese el nombre del continente (ej: América): ").strip()
        if any(c.isdigit() for c in continente_input):
            print("\nPor favor no ingrese números.\n")
            continue
        if continente_input == "":
            print("\nPor favor ingrese un nombre de continente válido.\n")
            continue
        break
    # Versión para mostrar (capitalizada) y versión normalizada (sin tildes, en minúsculas) para comparar
    continente_display = continente_input.capitalize()
    continente_norm = quitar_tildes(continente_input.lower())

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
        # 'continente' se usa para mostrar al usuario
        "continente": continente_display,
        # 'continente_norm' se usa internamente para comparar sin tildes ni mayúsculas
        "continente_norm": continente_norm,
        "pob_min": pob_min,
        "pob_max": pob_max,
        "sup_min": sup_min,
        "sup_max": sup_max
    }
    return filtros


def _leer_datos_estadisticas(archivo_csv):
    datos_limpios = []
    try:
        with open(archivo_csv, mode='r', encoding='utf-8', newline='') as f:
            lector = csv.DictReader(f)

            if not lector.fieldnames:
                print(f"Error (Estadísticas): El archivo '{archivo_csv}' está vacío.")
                return None  # Devuelve None si el archivo está vacío

            for fila in lector:
                try:
                    # Intenta convertir los datos de esta fila
                    datos_limpios.append({
                        "nombre": fila['nombre'],
                        "poblacion": int(fila['población']),
                        "superficie": int(fila['superficie']),
                        "continente": fila['continente']
                    })
                except (ValueError, KeyError, TypeError):
                    # Si una fila tiene datos malos (ej: 'N/A'), la ignora
                    pass 
            
            if not datos_limpios:
                print("No se encontraron datos válidos para calcular estadísticas.")
                return None

            return datos_limpios

    except FileNotFoundError:
        print(f"Error CRÍTICO: No se encontró el archivo de estadísticas '{archivo_csv}'")
        return None  # Devuelve None si el archivo no se encuentra
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer los datos: {e}")
        return None


def calcular_extremos_poblacion(datos):
    """Calcula y muestra el país con mayor y menor población."""
    try:
        # Usamos 'max' y 'min' con una 'key' para encontrar el país (diccionario)
        pais_mayor_pob = max(datos, key=lambda p: p['poblacion'])
        pais_menor_pob = min(datos, key=lambda p: p['poblacion'])
        
        print("\n--- 📈 Extremos de Población ---")
        print(f"País con Mayor Población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,.0f})")
        print(f"País con Menor Población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,.0f})")
    except Exception as e:
        print(f"Error al calcular extremos de población: {e}")


def calcular_promedios(datos):
    """Calcula y muestra los promedios de población y superficie."""
    try:
        # Usamos generadores para sumar las columnas
        total_poblacion = sum(p['poblacion'] for p in datos)
        total_superficie = sum(p['superficie'] for p in datos)
        conteo = len(datos)

        promedio_pob = total_poblacion / conteo
        promedio_sup = total_superficie / conteo
        
        print("\n--- 📊 Promedios ---")
        print(f"Promedio de Población: {promedio_pob:,.0f} habitantes")
        print(f"Promedio de Superficie: {promedio_sup:,.0f} km²")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero (no hay datos).")
    except Exception as e:
        print(f"Error al calcular promedios: {e}")


def contar_paises_por_continente(datos):
    """Cuenta y muestra cuántos países hay por continente."""
    try:
        conteo_continentes = {}
        for pais in datos:
            continente = pais['continente']
            conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
        
        print("\n--- 🌎 Conteo de Países por Continente ---")
        # Ordenamos por nombre de continente
        for continente, cantidad in sorted(conteo_continentes.items()):
            print(f" - {continente}: {cantidad} países")
    except Exception as e:
        print(f"Error al contar países por continente: {e}")


def menu_estadisticas(archivo_csv):
    """
    Función principal que muestra el menú de estadísticas.
    Reemplaza a la antigua 'mostrar_estadisticas'.
    """
    print("\n--- 📊 Módulo de Estadísticas ---")
    
    # 1. Cargar los datos UNA SOLA VEZ
    datos = _leer_datos_estadisticas(archivo_csv)
    
    # Si la carga de datos falló, no continuamos
    if datos is None:
        print("No se pueden mostrar las estadísticas.")
        return

    # 2. Bucle del Menú
    while True:
        print("\n¿Qué estadística deseas consultar?")
        print("  1. País con mayor y menor población")
        print("  2. Promedio de población y superficie")
        print("  3. Cantidad de países por continente")
        print("  4. Mostrar TODAS las estadísticas")
        print("  5. Salir del módulo de estadísticas")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            calcular_extremos_poblacion(datos)
        elif opcion == '2':
            calcular_promedios(datos)
        elif opcion == '3':
            contar_paises_por_continente(datos)
        elif opcion == '4':
            # Llama a las tres funciones
            print("\n--- Mostrando todas las estadísticas ---")
            calcular_extremos_poblacion(datos)
            calcular_promedios(datos)
            contar_paises_por_continente(datos)
        elif opcion == '5':
            print("Saliendo del módulo de estadísticas...")
            break  # Rompe el bucle while y termina la función
        else:
            print("Error: Opción no válida. Por favor, elige un número entre 1 y 5.")


def filtro(filtros_dict):

    paises_encontrados = 0
    
    print(f"\n--- 2. Iniciando búsqueda... ---")
    print(f"Buscando con los siguientes criterios:")
    # mostramos la versión para display
    print(f"  Continente = {filtros_dict['continente']}")
    print(f"  Población = {filtros_dict['pob_min']} a {filtros_dict['pob_max']}")
    print(f"  Superficie = {filtros_dict['sup_min']} a {filtros_dict['sup_max']}")
    print("---------------------------------")
    
    print("\n--- Países Encontrados ---")
        
    try:
        with open("paises_info_espanol.csv", mode='r', encoding="utf-8", newline='') as archivo_lectura:
            
            lector_csv = csv.DictReader(archivo_lectura)
            
            if not lector_csv.fieldnames:
                 print(f"Error: El archivo csv está vacío.")
                 return # Salir de la función

            for fila in lector_csv:
                try:
                    poblacion_int = int(fila['población'])
                    superficie_int = int(fila['superficie'])
                    continente_str = fila.get('continente', '').strip()
                    # normalizamos el continente leído del CSV para comparar
                    continente_csv_norm = quitar_tildes(continente_str.lower())
                    # comparamos con la versión normalizada que guardamos en filtros_dict
                    filtro_continente = (continente_csv_norm == filtros_dict.get('continente_norm', '').lower())
                    filtro_poblacion = (poblacion_int >= filtros_dict['pob_min']) and (poblacion_int <= filtros_dict['pob_max'])
                    filtro_superficie = (superficie_int >= filtros_dict['sup_min']) and (superficie_int <= filtros_dict['sup_max'])
                    if filtro_continente and filtro_poblacion and filtro_superficie:
                        print(f"  - Nombre: {fila['nombre']}   |   Población: {fila['población']}  |  Superficie: {fila['superficie']}")
                        paises_encontrados += 1   
                except (ValueError, KeyError) as e:
                    nombre_pais = fila.get('nombre', 'DESCONOCIDO')
                    print(f"Error en fila: Fila ignorada (país: {nombre_pais}). Error: {e}")
            
            # --- TERMINÓ EL BUCLE FOR ---
            print("------------------------------")
            print(f"\nBúsqueda completada.")
            if paises_encontrados == 0:
                print(">> No se encontraron países que coincidan con todos los criterios.")
            else:
                print(f">> Se encontraron y mostraron {paises_encontrados} países.")

    except FileNotFoundError:
        print(f"Error CRÍTICO: No se encontró el archivo csv")
    except Exception as e:
        print(f"Ocurrió un error inesperado en el filtrado: {e}")