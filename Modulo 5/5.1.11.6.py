import string

textoEncriptar = input("Cual es tu texto a encriptar? ")
cambio = int(input("cual es tu valor de cambio? "))

def caesar(textoEncriptar, cambio): 
  textoCifrado = ""
  for caracter in textoEncriptar:
    if caracter.isalpha():
      alfabeto = ord(caracter) + cambio 
      if alfabeto > ord('z'):
        alfabeto -= 26
      resultado = chr(alfabeto)
      textoCifrado += resultado
  print("Tu texto cifrado es: ", textoCifrado)
  return textoCifrado
    
caesar(textoEncriptar, cambio)