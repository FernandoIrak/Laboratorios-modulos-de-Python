igual = 0
aux = 0
textoSinEspacios = []
texto = input("Ingrese la palabra que desea evaluar: ")

for letra in texto:
    if letra != " ":
        textoSinEspacios.append(letra)

texto = textoSinEspacios[:]

for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("El texto es palindromo!")
else:
  print("El texto no es palindromo!")