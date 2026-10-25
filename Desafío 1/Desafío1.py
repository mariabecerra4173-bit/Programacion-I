#PALÍNDROMOS

import string
import unicodedata

def limpiar_cadena(texto: str) -> str:
    
    #Limpieza del texto eliminando acentos, espacios, signos de puntuación,
    #conversión a minúsculas para una comparación minuciosa.
    
    #1. Convertir a minúsculas
    texto = texto.lower()
    
    #2. Eliminar acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    
    #3. Eliminar puntuación y espacios usando librería string
    caracteres_validos = string.ascii_lowercase + string.digits
    texto_limpio = "".join(c for c in texto if c in caracteres_validos)
    
    return texto_limpio

def es_palindromo(texto: str) -> bool:
    
    #Determinar si una cadena es un palíndromo comparándola con su reverso.
    #Uso de slicing [::-1]
    
    cadena_procesada = limpiar_cadena(texto)
    
    #Cadena vacía o sin letras-números después de la limpieza no se evalúa
    if not cadena_procesada:
        return False
        
    return cadena_procesada == cadena_procesada[::-1]

def main():
    print("--- Detector de palíndromos CUCEA ---")
        
    #Bucle para asegurar que el usuario introduzca un dato válido
    while True:
        entrada = input("Ingresa una palabra o frase (o 'salir'): ").strip()
        
        if entrada.lower() == 'salir':
            print("Programa finalizado.")
            break
            
        if not entrada:
            print("Error: La entrada no puede estar vacía. Intenta de nuevo.\n")
            continue
            
        #Evaluación y resultado
        if es_palindromo(entrada):
            print(f'-> "{entrada}" SÍ es un palíndromo.\n')
        else:
            print(f'-> "{entrada}" NO es un palíndromo.\n')

if __name__ == "__main__":
    main()
    Mover Desafío 1 a su propia carpeta
