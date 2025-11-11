# Proyecto: Gestión de Países

## Descripción del programa

Este programa permite **gestionar información de países** a partir del archivo CSV llamado `paises_info_espanol.csv`.

Se ejecuta desde la consola (terminal) y ofrece un menú interactivo con distintas opciones para **buscar, filtrar, ordenar** y **visualizar estadísticas** de los países.

El programa está compuesto por dos archivos principales:

* `main.py`: contiene el menú principal y la interacción con el usuario.
* `funciones.py`: define las funciones que realizan la búsqueda, filtrado, ordenamiento y cálculo de estadísticas.

El archivo de datos `paises_info_espanol.csv` debe encontrarse en el mismo directorio

---

## Instrucciones de uso

1. Colocar los archivos `main.py`, `funciones.py` y `paises_info_espanol.csv` en la  **misma carpeta** .
2. Abrir una **terminal o consola** en esa carpeta.
3. Ejecutar el programa con:
   ```
   python main.py
   ```
4. En pantalla aparecerá un **menú principal** con las siguientes opciones:

```
1. Buscar país por nombre
2. Filtrar países
3. Ordenar países
4. Mostrar estadísticas
5. Salir
```

Selecciona una opción escribiendo su número y presionando  **Enter** .

---

## Detalle de las opciones

### 1️⃣ Buscar país por nombre

Permite buscar un país escribiendo su nombre o parte del nombre.

El programa muestra todos los países que coincidan.

**Ejemplo:**

```
Ingrese el país a buscar: chile
```

**Salida esperada:**

```
País encontrado:
Chile, 19100000 habitantes, 756102 km², América del Sur
```

---

### 2️⃣ Filtrar países

Permite filtrar países según:

* **Continente**
* **Rango de población (mínima y máxima)**
* **Rango de superficie (mínima y máxima)**

**Ejemplo de entrada:**

```
Ingrese continente: América
Ingrese población mínima: 10000000
Ingrese población máxima: 50000000
Ingrese superficie mínima: 500000
Ingrese superficie máxima: 3000000
```

**Salida esperada:**

```
Países que cumplen el filtro:
Argentina, 45300000 habitantes, 2780400 km², América del Sur
Chile, 19100000 habitantes, 756102 km², América del Sur
```

---

### 3️⃣ Ordenar países

Permite ordenar los países por:

* **Nombre (A-Z)**
* **Población (mayor a menor)**
* **Superficie (mayor o menor)**

**Ejemplo de entrada:**

```
Seleccione tipo de orden:
1. Nombre
2. Población
3. Superficie ascendente
4. Superficie descendente
```

**Salida esperada (orden por población descendente):**

```
China, 1400000000, 9596961, Asia
India, 1366000000, 3287263, Asia
Estados Unidos, 331000000, 9833520, América del Norte
```

---

### 4️⃣ Mostrar estadísticas

Muestra información estadística sobre los países:

* País con mayor y menor población.
* Promedio de población y superficie.
* Cantidad de países por continente.

**Ejemplo de salida:**

```
País con mayor población: China (1,400,000,000)
País con menor población: Islandia (366,000)
Promedio de población: 250,000,000
Promedio de superficie: 3,000,000 km²
Conteo por continente:
América: 20
Europa: 15
Asia: 12
África: 10
Oceanía: 5
```

---

### 5️⃣ Salir

Finaliza la ejecución del programa.

---

## Ejemplo de archivo CSV

```
nombre,población,superficie,continente
Argentina,45300000,2780400,América del Sur
Chile,19100000,756102,América del Sur
Brasil,212600000,8515770,América del Sur
Canadá,38000000,9984670,América del Norte
España,47350000,505990,Europa
```

---

## VIDEO TUTORIAL

https://drive.google.com/file/d/12QG0krHJrNK4xpXgxiKaDZoE2GVXzsud/view?usp=sharing

## VIDEO DE LA CORRECCIÓN

https://drive.google.com/file/d/16QPQcw3lEvOEUOfHLfJ_t3zR7xh6mZ8g/view?usp=drive_link

---



📚 **Autores:** Santino Barone, Maximo Quiroga

🕹️ **Ejecución:** `python main.py`

---
