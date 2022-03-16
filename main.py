import os
os.system('clear')
print('Bienvenido al programa para descargar archivos Fasta de Uniprot')
print('---------------------------------------------------------------')
nombre = input('Indica el nombre del archivo final .Fasta: ')
opcion = input('Teclea (A) si quieres usar un archivo para utilizar un archivo de links, o (B) si deseas ingresar los links manualmente: ').upper()
contador = 0
if opcion == 'B':
    tamano = int(input('Indica el numero de links que quieres bajar: '))
    while contador < tamano:
        link = input('Ingresa el link de la proteina '+str(contador + 1)+': ')
        link = link +'.fasta'
        if contador == 0:
            command = 'curl '+link+' > ./descargas/'+nombre+'.fasta'
        else:
            command = 'curl '+link+' >> ./descargas/'+nombre+'.fasta'
        os.system(command)
        os.system('clear')
        contador = contador +1
if opcion == 'A':
    archivo = input('Ingresa el nombre del archivo: ')
    f = open(archivo, "r")
    for x in f:
        link = x.rstrip()
        link = link +'.fasta'
        print(link)
        if contador == 0:
            command = 'curl '+link+' > ./descargas/'+nombre+'.fasta'
        else:
            command = 'curl '+link+' >> ./descargas/'+nombre+'.fasta'
        os.system(command)
        os.system('clear')
        contador = contador +1
    print('Se descargaron '+str(contador)+' Archivos')
else:
    print('No selecciono ninguna opcion valida. Por favor vuelve a intentar.')