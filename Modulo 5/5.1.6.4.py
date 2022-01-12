def readint(prompt, min, max):
    esValido = False
    while not esValido:
        try:
            numero = int(input(prompt))
            esValido = True
        except ValueError:
            print("Error: entrada incorrecta")
        if esValido:
            esValido = numero >= min and numero <= max
        if not esValido:
            print("Error: el valor no está dentro del rango permitido", str(min), "..", str(max))
    
    return numero       


v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)