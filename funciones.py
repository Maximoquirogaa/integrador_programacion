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
def cargar_datos_csv(archivo_csv):
    lista_paises = []
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for i, row in enumerate(reader):
                try:
                    pais = {
                        'nombre': row['nombre'].strip(),
                        'poblacion': int(row['poblacion']),
                        'superficie': int(row['superficie']),
                        'continente': row['continente'].strip()
                    }
                    lista_paises.append(pais)
                except ValueError:
                    print(f"Error de formato en línea {i+2}: '{row}'. Saltando registro.")
                except KeyError as e:
                    print(f"Error: Falta la columna {e} en el CSV. Abortando carga.")
                    return [] 
                    
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado. Asegúrese de que '{archivo_csv}' exista.")
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        
    return lista_paises
def filtrar_por_continente(lista_paises, continente):
    """Filtra países por continente (no sensible a mayúsculas)."""
    continente = continente.lower()
    return [pais for pais in lista_paises if pais['continente'].lower() == continente]


def filtrar_por_rango_poblacion(lista_paises, min_pob, max_pob):
    """Filtra países dentro de un rango de población (inclusivo)."""
    return [pais for pais in lista_paises if min_pob <= pais['poblacion'] <= max_pob]
def filtrar_por_rango_superficie(lista_paises, min_sup, max_sup):
    
    """Filtra países dentro de un rango de superficie (inclusivo)."""
    return [pais for pais in lista_paises if min_sup <= pais['superficie'] <= max_sup]


def leer_entero(mensaje, min_val=None, max_val=None):
    while True:
        try:
            entrada = input(mensaje)
            valor = int(entrada)
            
            if min_val is not None and valor < min_val:
                print(f"Error: El valor debe ser como mínimo {min_val}.")
                continue
                
            if max_val is not None and valor > max_val:
                print(f"Error: El valor debe ser como máximo {max_val}.")
                continue
                
            return valor
            
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
def leer_opcion_valida(mensaje, opciones_validas):

    opciones_validas_lower = [op.lower() for op in opciones_validas]
    while True:
        entrada = input(mensaje).lower()
        if entrada in opciones_validas_lower:
            return entrada.upper() # Devolvemos en mayúscula para estandarizar
        else:
            print(f"Error: Opción no válida. Ingrese una de: {', '.join(opciones_validas)}")
def mostrar_lista_paises(lista_paises, titulo="Lista de Países"):

    print(f"\n--- {titulo} ---")
    
    if not lista_paises:
        print("No se encontraron países que coincidan con los criterios.")
        return
        
    # Imprimir encabezado
    print(f"{'Nombre':<30} | {'Continente':<15} | {'Población':>15} | {'Superficie (km²)':>18}")
    print("-" * 81)
    
    # Imprimir filas
    for pais in lista_paises:
        nombre = pais['nombre']
        continente = pais['continente']
        # Usamos f-strings con formato de comas (,) para miles y alineación (>)
        poblacion = f"{pais['poblacion']:,}"
        superficie = f"{pais['superficie']:,}"
        
        print(f"{nombre:<30} | {continente:<15} | {poblacion:>15} | {superficie:>18}")

    print(f"\nTotal: {len(lista_paises)} países mostrados.")