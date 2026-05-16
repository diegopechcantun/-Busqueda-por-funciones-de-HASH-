# Búsqueda por Funciones Hash
---
Sistema de búsqueda de números mediante una Tabla Hash en Python, diseñado para almacenar y localizar datos de forma rápida y eficiente.
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
---

## Estructura del Repositorio

```
*`Búsqueda por Funciones Hash`
│
├── *`metodo_hash.py`
├── *`datos.txt`
├── *`datos_ordenados.txt`
└── *`README.md`
```
---
## Video explicativo del codigo

### Video subido a YouTube 

[![Ver demostración del proyecto](https://img.shields.io/badge/▶%20Ver%20Video-Explicación-red?style=for-the-badge&logo=youtube)](https://youtu.be/aucYYLKTMn8)

---
## Análisis de Complejidad

El rendimiento del algoritmo Shell Sort depende principalmente de la secuencia de incrementos (gap) utilizada. En esta implementación, el gap se reduce dividiendo el tamaño del arreglo entre 2 en cada iteración.

### Complejidad Temporal

| Caso | Complejidad | Descripción |
|------|-------------|-------------|
| **Mejor caso** | **O(n log n)** |  Ocurre cuando el arreglo ya está ordenado o casi ordenado. |
| **Caso promedio** | **O(n log n)** | Depende de la secuencia de intervalos. |
| **Peor caso** | **O(n²)** |Se presenta cuando los datos están en el orden más desfavorable. |

### Complejidad del espacio

Shell Sort es un algoritmo de ordenamiento in-place, lo que significa que no requiere memoria auxiliar adicional para realizar el ordenamiento.

Por esta razón, su complejidad espacial es de O(1), ya que el algoritmo opera directamente sobre el arreglo original utilizando una cantidad constante de memoria.



---
## Casos de Uso

### Cuándo usar Shell Sort

- Cuando se trabaja con arreglos medianos (no tan grandes como para usar algoritmos más complejos).
- Cuando los datos están parcialmente ordenados.
- Cuando se necesita un algoritmo simple de implementar pero más eficiente que métodos básicos como Bubble Sort.
- Cuando se requiere bajo uso de memoria (ya que no usa memoria extra).

### Cuándo NO usar Shell Sort

- Se manejan grandes volúmenes de datos (como mas de 50,000 datos).
- Se requiere máxima eficiencia garantizada.
- Cuando se necesita un rendimiento predecible y consistente, ya que su eficiencia depende de la      secuencia de incrementos (gaps).
- Se necesita un algoritmo estable.
---


## Comparativa Teórica: Shell Sort vs Bubble Sort


| Característica      |   Shell Sort      |   Bubble Sort     |
|---------------------|-------------------|-------------------|
| Complejidad         | O(n²)             | O(n²)             |
| Comparaciones       | Reducidas         | Muy altas         |
| Intercambios        | Eficientes        | Ineficientes      |
| Uso real            | Práctico          | Educativo         |


#### **Análisis**


Bubble Sort compara elementos adyacentes repetidamente, lo que genera una gran cantidad de operaciones redundantes.

Shell Sort mejora esto al comparar elementos distantes, reduciendo drásticamente la cantidad de iteraciones necesarias.

  

---


## Comparativa Teórica: Shell Sort vs Quick Sort


| Característica        | Shell Sort  | Quick Sort     |
|-----------------------|-------------|----------------|
| Complejidad promedio  |  O(n log n) | O(n log n)     |
| Peor caso             | O(n^2)      | O(n^2)         |
| Rendimiento real      | Bueno       | Muy alto       |
| Localidad de cache    | Alta        | Alta           |
| Sensibilidad          | Baja        | Alta (pivote)  |


**Análisis**

Quick Sort es generalmente el algoritmo más rápido en la práctica debido a su complejidad promedio O(n log n). Sin embargo, su rendimiento depende de una buena elección del pivote.

Shell Sort:

- No depende de decisiones dinámicas (como pivote)

- Es más predecible en ejecución

- Menos propenso a degradarse por casos específicos


---
