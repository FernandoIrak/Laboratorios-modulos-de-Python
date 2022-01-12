def esAnagrama(a, b):
    if sorted(a.lower())==sorted(b.lower()) :
        return "Anagramas"
    else:
        return "No son Anagramas"


def quitarEspacios(texto):
    textoSinEspacios = ""
    for letra in texto:
        if letra != " ":
            textoSinEspacios += letra

    return textoSinEspacios


palabra_1 = input("Ingrese una palabra")
palabra_2 = input("Ingrese otra palabra")
palabra_1 = quitarEspacios(palabra_1)
palabra_2 = quitarEspacios(palabra_2)

resultado = esAnagrama(palabra_1, palabra_2)

print(resultado)
