# Búsqueda por Funciones Hash
---
## Integrantes

- **Balam Castillo Pedro**
- **Pech Cantun Diego**
- **Loreto Huerta Filiberto**
---

## Proyecto Académico
- Institución: Instituto Tecnológico de Mérida
- Materia: Estructura de Datos
- Carrera: Ingeniería en Sistemas Computacionales

---

## Descripción  
El proyecto consiste en implementar en Python un sistema que lea un archivo de texto con 50,000 números, los ordene y permita realizar búsquedas de números utilizando el método de búsqueda Hash, además de medir el tiempo que tarda cada proceso.

---


## ¿Qué es?

La búsqueda hash es un algoritmo de búsqueda que utiliza una función hash para mapear claves a posiciones en una tabla hash. Esta técnica permite un acceso rápido y directo a los elementos almacenados, basándose en sus claves únicas.

Una tabla hash es una estructura de datos que se utiliza para almacenar información en forma de pares clave–valor. Su funcionamiento se basa en una función hash, la cual toma una clave y la transforma en un índice dentro de un arreglo. En esa posición se guarda el valor correspondiente.


---
##  Funcionamiento
---

## Estructura del Repositorio
```
Búsqueda por Funciones Hash
│
├── metodo_hash.py
├── datos.txt
├── datos_ordenados.txt
└── README.md

```
---
## Video explicativo del codigo

### Video subido a YouTube 

[![Ver demostración del proyecto](https://img.shields.io/badge/▶%20Ver%20Video-Explicación-red?style=for-the-badge&logo=youtube)](https://youtu.be/aucYYLKTMn8)

---
## Análisis de Complejidad

El rendimiento de la búsqueda en una tabla hash depende principalmente de la función hash utilizada y de la cantidad de colisiones que se generen. En esta implementación, la clave se transforma para obtener un índice directo dentro de la tabla. 

### Complejidad Temporal

| Caso | Complejidad | Descripción |
|------|-------------|-------------|
| **Mejor caso** | **O(1)** |  El tiempo de búsqueda es constante, independientemente del tamaño de los datos. |
| **Caso promedio** | **O(1)** |Con una buena función hash, los datos se distribuyen correctamente y las colisiones son mínimas |
| **Peor caso** | **O(n)** |Ocurre cuando todos los elementos generan el mismo hash (mala función hash o muchas colisiones).|

### Complejidad del espacio

La complejidad espacial de una tabla hash es de O(n), donde n es la cantidad de elementos almacenados. 

Esto se debe a que cada elemento necesita espacio en la estructura principal y, en caso de colisiones, también puede ocupar espacio adicional en las listas internas. Sin embargo, este crecimiento es lineal y controlado, ya que cada elemento se almacena una sola vez dentro de la estructura.


---
## Casos de Uso

### Cuándo usar HASH

- Cuando se requiere un acceso rápido a los elementos basado en claves únicas. 
- En compiladores y intérpretes, la búsqueda hash se emplea para buscar rápidamente identificadores y variables.
- La búsqueda hash permite un acceso rápido a los datos almacenados en caché.
- Las funciones hash se utilizan en la generación de huellas digitales y firmas digitales.

### Cuándo no usar HASH

- Datos que requieren orden específico.
- Memoria muy limitada.
- Se necesita acceso ordenado por clave mínima o máxima.
- Cuando necesitas operaciones de rango o secuenciales.
---


## Comparativa Teórica: Búsqueda Hash vs Búsqueda Binaria


| Característica       |         Hash        |     Búsqueda Binaria  |
|----------------------|---------------------|-----------------------|
| Complejidad Promedio | O(1)                | O(log n)              |
| Complejidad Promedio | O(n)                | O(log n)              |
| Requiere Orden       | No                  | Sí                    |
| Espacio Extra        | O(n)                | O(1)                  |
| Mejor Para           | Búsquedas frecuentes| Datos ordenados, rango|
#### **Análisis**


* `Búsqueda Binaria:` Divide el espacio de búsqueda por la mitad repetidamente, comparando el elemento objetivo con el punto medio. Requiere que los datos estén previamente ordenados.

* ` Búsqueda Hash:`  Calcula un índice mediante una función hash, permitiendo acceso directo a los datos. Realiza un acceso aleatorio al almacenamiento mediante transformación de clave.
  

---


## Comparativa Teórica: Búsqueda Hash vs Búsqueda Secuencial


| Característica       |         Hash        |  Búsqueda Secuencial  |
|----------------------|---------------------|-----------------------|
| Complejidad Promedio | O(1)                |   O(n)                |
| Complejidad Peor caso| O(n)                |   O(n)                |
| Requiere Orden       | No                  |   No                  |
| Espacio Extra        | O(n)                |   O(1)                |
| Mejor Para           | Búsquedas frecuentes|  Datos sin ordenar    |


**Análisis**

*`Búsqueda Secuencial:` Examina cada elemento uno por uno desde el inicio hasta encontrar el objetivo o agotar la colección. Requiere múltiples comparaciones y accesos secuenciales.

*`Búsqueda Hash:` 
Obtiene el índice directamente mediante función hash. Un acceso de O(1) en promedio, sin necesidad de comparaciones múltiples.


---
