fechaNacimiento = input("Ingrese digito: ")

resultado = 0
for numero in fechaNacimiento: 
    resultado += int(numero) 

    if resultado > 9: 
        resultado = resultado % 10 + resultado // 10
  
print("El digito de la vida es : " + str(resultado))