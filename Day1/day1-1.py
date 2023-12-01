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