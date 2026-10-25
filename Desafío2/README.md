# Programación I - Desafío 2: Histograma

Este repositorio contiene la solución al "Desafío 2" y consiste en un programa que toma una lista de números y genera un histograma basado en asteriscos.

## Histograma
Representación gráfica de una distribución de frecuencias por medio de barras, cuyas alturas representan las correspondientes frecuencias.

## Características del programa
Para cumplir con los criterios de robustez y funcionalidad requeridos, el programa:
- Permite que el usuario capture los datos mediante valores separados por comas.
- Realiza la validación de tipos de datos (detecta errores si el usuario introduce letras en lugar de números).
- Gestiona de forma controlada casos de números negativos y el cero.
- Utiliza operaciones de cadenas (`"*" * num`) para optimizar el rendimiento.

## Ejemplo de uso en consola
**Prueba de funcionalidad**
Ingrese los números (o escriba 'salir'): 5, 3, 7

*Resultado*
--- Resultado del histograma ---
Valor  5 | *****
Valor  3 | ***
Valor  7 | *******
--------------------------------
**Prueba de protección** (ignora palabras)
Ingrese los números (o escriba 'salir'): 9, lunes, 5, 2

*Resultado*
--- Resultado del histograma ---
Valor  9 | *********
Valor  5 | *****
Valor  2 | **
--------------------------------
**Prueba de casos especiales**
Ingrese los números (o escriba 'salir'): -7, 2, 0, 8, 4

*Resultado*
--- Resultado del histograma ---
Valor -7 | (No se admiten negativos)
Valor  2 | **
Valor  0 | 
Valor  8 | ********
Valor  4 | ****
--------------------------------