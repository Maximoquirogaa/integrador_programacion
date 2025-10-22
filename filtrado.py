import csv
import funciones_filtrado
archivo_entrada = "paises_info_espanol.csv"
archivo_salida = "filtrado_de_paises.csv"
paises_encontrados = 0
filtros = funciones_filtrado.obtener_filtros_usuario()

try:
    with open(archivo_entrada, mode='r', encoding="utf-8") as archivo_lectura:
        with open(archivo_salida, mode='w', encoding="utf-8") as archivo_escritura:
            
            lector_csv = csv.DictReader(archivo_lectura)
            escritor_csv = csv.DictWriter(archivo_escritura, fieldnames=lector_csv.fieldnames)
            escritor_csv.writeheader()
            
            for fila in lector_csv:
                try:
                    #Asignar tipos de datos
                    poblacion_int = int(fila['población'])
                    superficie_int = int(fila['superficie'])
                    continente_str = fila['continente']
                    
                    # Filtros
                    filtro_continente = continente_str == filtros['continente']
                    filtro_poblacion = (poblacion_int >= filtros['pob_min']) and (poblacion_int <= filtros['pob_max'])
                    filtro_superficie = (superficie_int >= filtros['sup_min']) and (superficie_int <= filtros['sup_max'])

                    if filtro_continente and filtro_poblacion and filtro_superficie:
                        escritor_csv.writerow(fila)
                        paises_encontrados += 1
                except ValueError:

                    print(f"Error de tipo: Fila ignorada (datos no numéricos): {fila['nombre']}")
            if paises_encontrados == 0:
                print(">> No se encontraron países que coincidan con todos los criterios.")
            else:
                print(f">> Se encontraron {paises_encontrados} países que coinciden.")
                print(f"Resultados guardados en '{archivo_salida}'.")
                        
    print(f"\nFiltrado completado.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_entrada}'")


