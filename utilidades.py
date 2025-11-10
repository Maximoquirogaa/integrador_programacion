import unicodedata,csv, math,re

#-----------------UTILIDADES------------------

def quitar_tildes(texto): #Funcion para quitar tildes de los inputs
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

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

def pedir_string(msg):
    
    while True:
        s=input(msg)
        # Prevenimos que no se ingresen números
        if any(c.isdigit() for c in s):
            print("\nPor favor no ingrese números.\n")
        else:
            return s
        
def pedir_int(msg):
    while True:
        try:
            n=int(input(msg))
            if n<0:
                print("No se permiten numeros negativos, reintente... ")
            else:
                return n
        except ValueError:
            print("Ingreso invalido, solo se permiten numeros enteros, reintente...")

def normalizar_string(t: str) -> str:
    # Normalizamos el string (quitamos tildes y pasamos a minúsculas)

    t = t.strip().lower()                       # quita espacios y pasa a minúsculas
    t = unicodedata.normalize("NFKD", t)        # separa tildes
    t = "".join(c for c in t if not unicodedata.combining(c))  # quita tildes
    t = re.sub(r"[^a-zñáéíóúü\s]", "", t)       # elimina signos o números
    t = " ".join(t.split())                     # unifica espacios
    """
    Devuelve el nombre normalizado para comparación.
    Requisitos:
    - Quitar espacios sobrantes intermedios y extremos.
    - Pasar a minúsculas.
    implementar y devolver el string normalizado.
    """
    return t

#-----------------PARA FUNCIONES------------------

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
        poblacion = f"{pais['poblacion']:,}"
        superficie = f"{pais['superficie']:,}"
        
        print(f"{nombre:<30} | {continente:<15} | {poblacion:>15} | {superficie:>18}")

    print(f"\nTotal: {len(lista_paises)} países mostrados.")

def filtrar_por_rango_poblacion(lista_paises, min_pob, max_pob):
    return [pais for pais in lista_paises if min_pob <= pais['poblacion'] <= max_pob]
    
def filtrar_por_rango_superficie(lista_paises, min_sup, max_sup):
    return [pais for pais in lista_paises if min_sup <= pais['superficie'] <= max_sup]


#-----------------PARA ARCHIVO------------------
def cargar_archivo_csv():
    lista_paises=[]
    with open("paises_info_espanol.csv", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        lector = csv.DictReader(archivo, fieldnames=campos) #tomar campos del encabezado si no hay encabezado
        next(lector)
        for fila in lector:
            fila["poblacion"]=int(fila["poblacion"])
            fila["superficie"]=int(fila["superficie"])
            lista_paises.append(fila)
        return lista_paises
    
def actualizar_csv(lista_paises):
    with open("paises_info_espanol.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]  # nombres de columnas
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()  # escribe la primera fila con los encabezados
        escritor.writerows(lista_paises)  # escribe todas las filas del listado