# Experimentos – Conteo de Subarreglos con MEX Igual

Este proyecto contiene un **código de experimentación en Python 3** para validar y analizar el rendimiento del algoritmo de conteo de subarreglos con MEX igual en dos permutaciones.

---

## Descripción del Código

El código realiza lo siguiente:

1. **Pruebas de ejemplo**  
   - Ejecuta el algoritmo sobre distintos casos de prueba predefinidos.  
   - Imprime la **salida obtenida**, la **esperada** y si el resultado es **correcto** o **incorrecto**.  
   - Permite validar que el algoritmo funciona correctamente según la subestructura óptima y la función de recurrencia.

2. **Experimentos de rendimiento**  
   - Genera entradas aleatorias de distintos tamaños \(n\).  
   - Mide el **tiempo de ejecución** del algoritmo para cada tamaño de entrada.  
   - Grafica el **tiempo de ejecución en función del tamaño de la entrada**, permitiendo observar empíricamente cómo escala el algoritmo.

---

## Tecnologías Utilizadas

- **Python 3**  
- **Matplotlib** para la visualización de resultados

---

## Uso

Ejecutar el script principal:
```bash
python3 experimentacion.py
```
Se imprimirán los resultados de las pruebas y se generará un gráfico mostrando la relación entre el tamaño de la entrada y el tiempo de ejecución.

Objetivo

El código de experimentación permite:

Validar el correcto funcionamiento del algoritmo sobre ejemplos conocidos.

Analizar empíricamente la complejidad temporal del algoritmo y confirmar que coincide con la teoría.
