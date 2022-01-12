palabraOculta = input("Ingrese la palabra Buscar: ")
texto = input("Ingrese texto con la palabra oculta: ")

palabraOculta = palabraOculta.lower()
texto = texto.lower()

for letra in palabraOculta:
    encontrado = texto.find(letra)
    
    if encontrado == -1:
        resultado = False
        break

    resultado = True

if resultado == True:
   print("Si") 
else:
    print("No")