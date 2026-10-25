#HISTOGRAMA

def validar_entrada(entrada_usuario: str) -> list[int]:
    
    #A partir de una cadena de texto ingresada por el usuario separada por comas,
    #se limpia y convierte en una lista de enteros válidos.
    #Filtra cualquier entrada que no sea un número.
    
    numeros_validos = []
    
    #Si el usuario no escribe nada, se regresa la lista vacía:
    if not entrada_usuario.strip():
        return numeros_validos
        
    #Se separa la cadena por comas:
    elementos = entrada_usuario.split(",")
    
    for elemento in elementos:
        try:
            #Eliminar espacios y convertir a entero:
            numero = int(elemento.strip())
            numeros_validos.append(numero)
        except ValueError:
            #Si contiene letras o símbolos, ignorar ese elemento:
            continue
            
    return numeros_validos

def generar_histograma(numeros: list[int]) -> str:
    
    #Se genera el formato visual del histograma usando asteriscos.
    #Regresa una cadena de texto con el resultado estructurado.
    
    if not numeros:
        return "No hay números válidos para generar el histograma."
        
    lineas_histograma = []
    
    for num in numeros:
        #Tratamiento especial de números negativos o cero:
        if num < 0:
            barra = f"Valor {num:2d} | (No se admiten negativos)"
        elif num == 0:
            barra = f"Valor {num:2d} | "  #Barra vacía para el cero:
        else:
            barra = f"Valor {num:2d} | " + ("*" * num)
            
        lineas_histograma.append(barra)
        
    return "\n".join(lineas_histograma)

def main():
    print("--- Generador de histograma CUCEA ---")
    print("Introduzca una lista de números separados por comas.")
    print("Ejemplo: 4, 1, 8, 5, 3\n")
    
    while True:
        entrada = input("Ingrese los números (o escriba 'salir'): ").strip()
        
        if entrada.lower() == 'salir':
            print("Programa finalizado.")
            break
            
        #Procesar y validar la lista de números:
        lista_numeros = validar_entrada(entrada)
        
        if not lista_numeros:
            print("Error: No se ingresó ningún número válido. Intente de nuevo.\n")
            continue
            
        #Generar y mostrar el histograma:
        print("\n--- Resultado del histograma ---")
        print(generar_histograma(lista_numeros))
        print("-" * 32 + "\n")

if __name__ == "__main__":
    main()