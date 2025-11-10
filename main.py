import os,funciones, utilidades

if __name__=="__main__":
    # Cambiar el directorio actual al del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Directorio actual:", os.getcwd())

    lista_paises = utilidades.cargar_archivo_csv()

    while True:
        opcion=input("""
Ingrese una opcion: 
1. Buscar país por nombre
2. Filtrar países
3. Ordenar países (TAMBIEN CAMBIA EL ORDEN EN .CSV)
4. Mostrar estadísticas
5. Editar CSV
0. Salir
    """)
        
        match opcion:
            
            case "1":
                    funciones.BusquedaPais(lista_paises)

            case "2":
                funciones.manejar_submenu_filtros(lista_paises)

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
                            funciones.Ordenar(lista_paises,"nombre")
                        
                        case "2":
                            print("Ordenando por Población: ")
                            funciones.Ordenar(lista_paises,"poblacion")
                        
                        case "3":
                            while True:
                                opcion_k=input(""" 
1. Ascendente
2. Descendente
    """)
                                if opcion_k=="1":
                                    print("Ordenando por Superficie (Ascendente)")
                                    funciones.Ordenar(lista_paises,"superficie_a");break
                                elif opcion_k=="2":
                                    print("Ordenando por Superficie (Descendente)")
                                    funciones.Ordenar(lista_paises,"superficie_d");break
                                else: print("Opcion invalida")
                        
                        case _: print("\nOpcion invalida");continue
                    
                    break
            
            case "4":
                    funciones.menu_estadisticas(lista_paises)
                
            case "5":
                  while True:
                        print("""\n
-----EDICION DE CSV-----
1. Agregar pais 
2. Editar pais
3. Eliminar pais
0. Volver al menu principal\n
                              """)
                        opcion=input("Ingrese una opcion: ")
                        match opcion:
                            case "1":
                                funciones.crear_pais(lista_paises)
                            case "2":
                                funciones.editar_pais(lista_paises)
                            case "3":
                                funciones.eliminar_pais(lista_paises)
                            case "0":
                                  print("Volviendo...");break
                            case _: print("Opcion invalida, reintente...")

            case "0":
                print("Saliendo...");break
            
            case _: print("\nOpcion invalida. ")

        
