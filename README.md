# Programación I - Desafío 1: Palíndromos

Este repositorio contiene la solución al "Desafío 1" y consiste en un programa para determinar si la palabra o frase ingresada por el usuario es un palíndromo.

## Palíndromos
Un palíndromo es aquella palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda.

## Características del programa
Para cumplir con los criterios de robustez y funcionalidad requeridos, el programa:
- Ignora por completo las mayúsculas y minúsculas.
- Elimina espacios en blanco y signos de puntuación (.,!?¡¿).
- Normaliza caracteres para eliminar acentos (por ejemplo, "ó" se evalúa como "o").
- Incluye control de errores para evitar entradas vacías.

## Casos de prueba evaluados
El programa se ejecutó exitosamente con las siguientes cadenas:
1. `Anita lava la tina` -> SÍ es un palíndromo (elimina espacios en blanco, ignora mayúculas y minúsculas).
2. `luz azul` -> SÍ es un palíndromo.
3. `Dábale arroz a la zorra el abad` -> SÍ es un palíndromo
4. `programación` -> NO es un palíndromo.
5. `oso` -> SÍ es un palíndromo.
6. `anita lava la Tina` -> SÍ es un palíndromo.
7. `se es o no se es` -> SÍ es un palíndromo.
8. `buenos días` -> NO es un palíndromo.
9. `reconocer` -> -> SÍ es un palíndromo.
10. `UdG` -> NO es un palíndromo.