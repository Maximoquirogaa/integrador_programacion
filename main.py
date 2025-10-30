import os,funciones

if __name__=="__main__":
    # Cambiar el directorio actual al del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Directorio actual:", os.getcwd())

    while True:
        opcion=input("""
    Ingrese una opcion: 
    1. Buscar país por nombre
    2. Filtrar países
    3. Ordenar países
    4. Mostrar estadísticas
    5. Salir
    """)
        
        match opcion:
            
            case "1":
                while True:
                    busqueda=input("Ingrese el pais a buscar: ")
                    if funciones.BusquedaPais(busqueda)!=0:break

            case "2":
                funciones.filtro()

            case "3":
                while True:
                    opcion_m=input("""
    Ordenar por:
    1. Nombre
    2. Población -
    3. Superficie
    """)
                    match opcion_m:
                        case "1":
                            print("\nOrdenando por Nombre:")
                            funciones.Ordenar("nombre");break
                        
                        case "2":
                            print("Ordenando por Población: ")
                            funciones.Ordenar("poblacion");break
                        
                        case "3":
                            while True:
                                opcion_k=input(""" 
    1. Ascendente
    2. Descendiente
    """)
                                if opcion_k=="1":
                                    print("Ordenando por Superficie (Ascendente)")
                                    funciones.Ordenar("superficie_a");break
                                elif opcion_k=="2":
                                    print("Ordenando por Superficie (Descendente)")
                                    funciones.Ordenar("superficie_d");break
                                else: print("Opcion invalida")
                        
                        case _: print("\nOpcion invalida");continue
                    
                    break
            
            case "4":
                with open("paises_info_espanol.csv", "r", encoding="utf-8") as archivo:
                    funciones.menu_estadisticas("paises_info_espanol.csv")
                
            case "5":
                print("Saliendo...");break
            
            case _: print("\nOpcion invalida. ")

        
