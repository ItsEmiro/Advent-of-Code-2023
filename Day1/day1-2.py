from input import processedInput

def unir(cadenas:list) -> list:
    resultados = []

    for cadena in cadenas:
        primero = None
        ultimo = None
        for caracter in cadena:
            if caracter.isdigit():
                if primero is None:
                    primero = caracter
                ultimo = caracter
            elif caracter.isalpha():
                if 'one' in cadena:
                    if primero is None:
                        primero = '1'
                    ultimo = '1'
                elif 'two' in cadena:
                    if primero is None:
                        primero = '2'
                    ultimo = '2'
                elif 'three' in cadena:
                    if primero is None:
                        primero = '3'
                    ultimo = '3'
                elif 'four' in cadena:
                    if primero is None:
                        primero = '4'
                    ultimo = '4'
                elif 'five' in cadena:
                    if primero is None:
                        primero = '5'
                    ultimo = '5'
                elif 'six' in cadena:
                    if primero is None:
                        primero = '6'
                    ultimo = '6'
                elif 'seven' in cadena:
                    if primero is None:
                        primero = '7'
                    ultimo = '7'
                elif 'eight' in cadena:
                    if primero is None:
                        primero = '8'
                    ultimo = '8'
                elif 'nine' in cadena:
                    if primero is None:
                        primero = '9'
                    ultimo = '9'
                
        if primero is not None and ultimo is not None:
            resultado = int(primero + ultimo)
            resultados.append(resultado)
        else:
            resultados.append(None)

    return resultados

def sumar(numeros:list) -> int:
    suma = 0

    for numeros in numeros:
        suma += numeros

    return suma



cadena = unir(processedInput)
print(cadena)
print(sumar(cadena))