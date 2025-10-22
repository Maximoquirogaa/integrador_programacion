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
            #codigo
            break

        case "2":
            opcion_m=input("""
            Filtrar por:
            1. Continente
            2. Rango de poblacion
            3. Rango de superficie
            """)
            match opcion_m:
                case "1":
                    print("Filtrando países por continente: ")
                    #codigo
                case "2":
                    print("Filtrando países por Rango de Poblacion: ")
                    #codigo
                case "3":
                    print("Filtrando países por Rango de Superficie: ")
                    #codigo
        case "3":
            opcion_m=input("""
            Ordenar por:
            1. Nombre
            2. Población 
            3. Superficie
            """)
            match opcion_m:
                case "1":
                    print("Ordenando por Nombre: ")
                    #codigo
                case "2":
                    print("Ordenando por Población: ")
                    #codigo
                case "3":
                    opcion_k=input(""" 
                    1. Ascendente
                    2. Descendiente
                    """)
                    if opcion_k=="1":
                        print("Ordenando por Superficie (Ascendente)")
                        #codigo
                    else:
                        print("Ordenando por Superficie (Descendiente)")
                        #codigo
        case "4":
            #codigo
            break
        case "5":
            break

    
