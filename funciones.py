import utilidades,csv


#Funciones de busqueda y ordenado
def BusquedaPais(lista_paises):
    
    busqueda=utilidades.pedir_string("Ingrese el pais a buscar: ")

    encontrado = False
    for i in lista_paises:
        if busqueda in utilidades.quitar_tildes(i["nombre"]).lower():
            print(f"\nPaís encontrado: {i["nombre"]}\nPoblación: {i["poblacion"]}\nSuperficie: {i["superficie"]}\nContinente: {i["continente"]}")
            encontrado = True
            idx=lista_paises.index(i)
            return idx
    if not encontrado:
        print("No se encontró ningún país.")
        return -1


def Ordenar(lista_paises,tipo):
    
    if tipo=="nombre":
        parte=0
    elif tipo=="poblacion":
        parte=1
    elif tipo=="superficie_a" or tipo=="superficie_d":
        parte=2
    paises = []

    for pais in lista_paises:
        try:
            nombre = pais["nombre"]
            poblacion = pais["poblacion"] #pais["poblacion"] corresponde a el valor de poblacion en el diccionario
            superficie = pais["superficie"] #pais["superficie"] corresponde a el valor de superficie en el diccionario
            continente = pais["continente"]
            paises.append((nombre, poblacion, superficie, continente))
            
        except ValueError:
            print(f"Error con la línea: {pais}")

    if tipo=="superficie_d" or tipo=="poblacion":   
        paises_ordenados = sorted(paises, key=lambda x: x[parte], reverse=True)# Ordenar por valor de mayor a menor
    else:
        paises_ordenados = sorted(paises, key=lambda x: x[parte], reverse=False)# Ordenar por valor de menor a mayor
    lista_paises=[]
    for nombre, poblacion, superficie, continente in paises_ordenados:
        print(f"\n{nombre}: |  Poblacion: {poblacion} | Superficie: {superficie} | Continente: {continente}")
        lista_paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
        utilidades.actualizar_csv(lista_paises)

#Funciones de edicion
def crear_pais(lista_paises):
    print("Seleccionaste Creacion de Pais...")
    while True:
        encontrado=False
        nombre=utilidades.pedir_string("Ingrese el nombre del pais: ").title()
        for i in range(len(lista_paises)):
            if utilidades.quitar_tildes(lista_paises[i]["nombre"]).lower()==utilidades.quitar_tildes(nombre.lower()):
                print("Nombre de pais ya existente.")
                encontrado=True
        if not encontrado:break

    poblacion=utilidades.pedir_int("Ingrese la poblacion del pais: ")
    superficie=utilidades.pedir_int("Ingrese la superficie del pais en km²: ")
    while True:
        ingreso=input("Ingrese el continente al que pertenece: América, Asia, Oceanía, África, Europa: ").title()
        continentes=["América","Asia","Oceania","África","Europa"]
        continente=""
        for i in range(5):
            if utilidades.quitar_tildes(ingreso) in utilidades.quitar_tildes(continentes[i]):
                continente=continentes[i]
                break
        if continente=="": 
            print("Continente invalido, reintente...")
        else: break
    while True:
        print(f"Datos del pais a ingresar: Nombre: {nombre} | Poblacion: {poblacion} | Superficie: {superficie} | Continente: {continente}")
        c=input("Confirmar ingreso (si/no)")
        if c == "si":
            lista_paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
            utilidades.actualizar_csv(lista_paises)
            print("Pais ingresado correctamente. ")
            break
        elif c=="no":
            print("Ingreso cancelado. ")
            break
        else:
            print("Opcion invalida.")

def editar_pais(lista_paises):
    while True:
        idx=BusquedaPais(lista_paises)
        if idx: break
    while True:
        opcion=input("""
Que quiere editar del pais?: 
1. Nombre
2. Poblacion
3. Superficie
4. Continente
                    """)
        match opcion:
            case "1":
                while True:
                    encontrado=False
                    nombre=utilidades.pedir_string(f"Ingrese el nuevo nombre para {lista_paises[idx]["nombre"]}: ")
                    for i in range(len(lista_paises)):
                        if utilidades.quitar_tildes(lista_paises[i]["nombre"]).lower()==utilidades.quitar_tildes(nombre.lower()):
                            print("Nombre de pais ya existente.")
                            encontrado=True
                    if not encontrado:
                        lista_paises[idx]["nombre"]=nombre.title()
                        break
                break
            case "2":
                poblacion=utilidades.pedir_int(f"Ingrese la nueva poblacion para {lista_paises[idx]["nombre"]}: ")
                lista_paises[idx]["poblacion"]=poblacion
                break
            case "3":
                superficie=utilidades.pedir_int(f"Ingrese la lueva superficie para {lista_paises[idx]["nombre"]}: ")
                lista_paises[idx]["superficie"]=superficie
                break
            case "4":
                while True:
                    ingreso=input(f"Ingrese el nuevo continente de {lista_paises[idx]["nombre"]}: América, Asia, Oceanía, África, Europa: ").title()
                    continentes=["América","Asia","Oceania","África","Europa"]
                    continente=""
                    for i in range(5):
                        if utilidades.quitar_tildes(ingreso) in utilidades.quitar_tildes(continentes[i]):
                            continente=continentes[i]
                            break
                    if continente=="": 
                        print("Continente invalido, reintente...")
                    else: break
                lista_paises[idx]["continente"]=continente
                break
            case _: print("Opcion invalida, reintente... ")
    
    utilidades.actualizar_csv(lista_paises)
    print("Modificacion exitosa")
    print(f"Pais actualizado: Nombre: {lista_paises[idx]["nombre"]} | Poblacion: {lista_paises[idx]["poblacion"]} | Superficie: {lista_paises[idx]["superficie"]} | Continente: {lista_paises[idx]["continente"]}")

def eliminar_pais(lista_paises):
    while True:
        idx=BusquedaPais(lista_paises)
        if idx!=-1: break
    c=input("\nConfirmar eliminacion de pais ingresando 'Y', ingrese cualquier letra para cancelar: ")
    if c == "Y":
        del lista_paises[idx]
        utilidades.actualizar_csv(lista_paises)
        print("Eliminado con éxito. ")
    else:
        print("Se cancelo la operacion, no se ha eliminado el pais.")

#Funciones de estadisticas
def calcular_extremos_poblacion(datos):
    try:
        pais_mayor_pob = max(datos, key=lambda p: p['poblacion'])
        pais_menor_pob = min(datos, key=lambda p: p['poblacion'])
        
        print("\n--- 📈 Extremos de Población ---")
        print(f"País con Mayor Población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,.0f})")
        print(f"País con Menor Población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,.0f})")
    except Exception as e:
        print(f"Error al calcular extremos de población: {e}")

def calcular_promedios(datos):
    try:
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
    try:
        conteo_continentes = {}
        for pais in datos:
            continente = pais['continente']
            conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
        
        print("\n--- 🌎 Conteo de Países por Continente ---")

        for continente, cantidad in sorted(conteo_continentes.items()):
            print(f" - {continente}: {cantidad} países")
    except Exception as e:
        print(f"Error al contar países por continente: {e}")

def menu_estadisticas(datos): 
    print("\n--- 📊 Módulo de Estadísticas ---")

    if not datos:
        print("No se pueden mostrar las estadísticas (lista vacía).")
        return
    
    while True:
        print("\n¿Qué estadística deseas consultar?")
        print("  1. País con mayor y menor población")
        print("  2. Promedio de población y superficie")
        print("  3. Cantidad de países por continente")
        print("  4. Mostrar TODAS las estadísticas")
        print("  5. Salir del módulo de estadísticas")
        
        opcion = input("Elige una opción (1-5): ")
        match opcion:
            case "1":
                calcular_extremos_poblacion(datos)

            case "2":
                calcular_promedios(datos)

            case "3":
                contar_paises_por_continente(datos)
            case "4":
                print("\n--- Mostrando todas las estadísticas ---")
                calcular_extremos_poblacion(datos)
                calcular_promedios(datos)
                contar_paises_por_continente(datos)
            case "5":
                print("Saliendo del módulo de estadísticas...")
                break
            case _:
                print("Error: Opción no válida. Por favor, elige un número entre 1 y 5.")

#Funciones de filtrado

def filtrar_por_continente(lista_paises, continente_input):

    input_normalizado = utilidades.quitar_tildes(continente_input.lower())
    
    lista_filtrada = []
    for pais in lista_paises:
        continente_del_pais_norm = utilidades.quitar_tildes(pais['continente'].lower())
        if continente_del_pais_norm == input_normalizado:
            lista_filtrada.append(pais)
    return lista_filtrada

def manejar_submenu_filtros(lista_paises):
    while True:
        print("  1. Filtrar por continente")
        print("  2. Filtrar por rango de población")
        print("  3. Filtrar por rango de superficie")
        print("  0. Volver al menú principal")

        opcion_filtro = utilidades.leer_entero("  Seleccione una opción de filtro: ", 0, 3)
        match opcion_filtro:
            case 1:
                continente = input("  Ingrese el nombre del continente: ")
                filtrados = filtrar_por_continente(lista_paises, continente)
                utilidades.mostrar_lista_paises(filtrados, f"Países en {continente}")
       
            case 2:
                min_pob = utilidades.leer_entero("  Ingrese la población mínima: ", 0)
                max_pob = utilidades.leer_entero("  Ingrese la población máxima: ", min_pob)
                filtrados = utilidades.filtrar_por_rango_poblacion(lista_paises, min_pob, max_pob)
                utilidades.mostrar_lista_paises(filtrados, f"Países entre {min_pob} y {max_pob} hab.")

            case 3:
                min_sup = utilidades.leer_entero("  Ingrese la superficie mínima (km²): ", 0)
                max_sup = utilidades.leer_entero("  Ingrese la superficie máxima (km²): ", min_sup)
                filtrados = utilidades.filtrar_por_rango_superficie(lista_paises, min_sup, max_sup)
                utilidades.mostrar_lista_paises(filtrados, f"Países entre {min_sup} y {max_sup} km²")

            case 0:
                print("  Volviendo al menú principal...")
                break
            case _: print("Opcion invalida.")
