def misplit(strng):
    palabras = []
    temp = ""
    for letra in strng:
        if letra == " ":
            palabras.append(temp)
            temp = ""
        else:
            temp += letra
    if temp:
        palabras.append(temp)
    return palabras    


print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))