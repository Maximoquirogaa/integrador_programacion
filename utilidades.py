import unicodedata,csv, math,re

def quitar_tildes(texto): #Funcion para quitar tildes de los inputs
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

def pedir_string(msg):
    
    while True:
        s=input(msg)
        # Prevenimos que no se ingresen números
        if any(c.isdigit() for c in s):
            print("\nPor favor no ingrese números.\n")
        else:
            s=normalizar_string(s)
            return s

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

def cargar_archivo_csv():
    lista_paises=[]
    with open("paises_info_espanol", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "edad", "pais"]
        lector = csv.DictReader(archivo, fieldnames=campos) #tomar campos del encabezado si no hay encabezado
        for fila in lector:
            lista_paises.append(fila)
        return lista_paises
    
def actualizar_csv(lista_paises):
    with open("paises_info_espanol", "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]  # nombres de columnas
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()  # escribe la primera fila con los encabezados
        escritor.writerows(lista_paises)  # escribe todas las filas del listado