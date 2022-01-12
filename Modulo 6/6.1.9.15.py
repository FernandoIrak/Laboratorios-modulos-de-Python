from os import strerror

srcname = input("Cual es el nombre del archivo de origen?: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("No se puede abrir e archivo de origen: ", strerror(e.errno))
    exit(e.errno)	
dstname = input("Cual es el archivo de destino?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("No se pudo crear un destino para el archivo: ",
    strerror(e.errno))
    src.close()
    exit(e.errno)	


entrada=input("Introduce una cadena: ")
 
diccionario={}
 
for letra in entrada:
    if letra in diccionario:
        diccionario[letra]=diccionario[letra]+ 1
    else:
        diccionario[letra]= 1
 
print(diccionario)