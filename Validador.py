def validarDato(tipo, mensaje, rango=None): 
    while True:
        try:
            dato = tipo(input(mensaje))

            if tipo == int and rango:
                if not rango[0] <= dato <= rango[1]:
                    raise ValueError(f"El valor debe estar en el rango {rango}")

            if tipo == float and rango:
                if not rango[0] <= dato <= rango[1]:
                    raise ValueError(f"El valor debe estar en el rango {rango}")

            return dato
        except ValueError:
            print(f"Error: Ingresa un valor válido del tipo {tipo.__name__}")

# Ejemplos de uso
texto = validarDato(str, "Ingresa un texto: ")
entero = validarDato(int, "Ingresa un entero: ")
entero_rango = validarDato(int, "Ingresa un entero en el rango [1, 10]: ", (1, 10))
entero_positivo = validarDato(int, "Ingresa un entero positivo (excluyendo 0): ", (1, float('inf')))
entero_negativo = validarDato(int, "Ingresa un entero negativo (excluyendo 0): ", (-float('inf'), 0))
decimal = validarDato(float, "Ingresa un decimal: ")
decimal_rango = validarDato(float, "Ingresa un decimal en el rango [0.5, 2.5]: ", (0.5, 2.5))
decimal_positivo = validarDato(float, "Ingresa un decimal positivo (excluyendo 0): ", (0, float('inf')))
decimal_negativo = validarDato(float, "Ingresa un decimal negativo (excluyendo 0): ", (-float('inf'), 0))

# Imprimir los valores
print(f"Texto: {texto}")
print(f"Entero: {entero}")
print(f"Entero en rango: {entero_rango}")
print(f"Entero positivo: {entero_positivo}")
print(f"Entero negativo: {entero_negativo}")
print(f"Decimal: {decimal}")
print(f"Decimal en rango: {decimal_rango}")
print(f"Decimal positivo: {decimal_positivo}")
print(f"Decimal negativo: {decimal_negativo}")
