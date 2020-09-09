import os
from PyPDF2 import PdfFileMerger
from unicodedata import normalize

print('Hecho por Bruno Stefoni en Python 3.7.3')

nombre_archivo = 'zlista_pdfs.txt'
if not os.path.isfile(nombre_archivo):
    print('No existe el archivo ' + nombre_archivo + '. CHAO')
    para_salir = input("Apreta cualquier tecla para salir")
    exit()

with open(nombre_archivo) as file:
    lista_pdf = [line.rstrip('\n') for line in file]

carpeta = lista_pdf.pop(0)

for i in range(len(lista_pdf)):
    if lista_pdf[i][-4:] != ('.pdf'):
        lista_pdf[i] = lista_pdf[i] + '.pdf'


if not os.path.isdir(carpeta):
    print('No existe carpeta ' + carpeta + '. CHAO')
    para_salir = input("Apreta cualquier tecla para salir")
    exit()


os.chdir(carpeta)

merger = PdfFileMerger()


if not lista_pdf:

    lista_pdf = [a for a in os.listdir() if a.endswith(".pdf")]

else:

    lista_pdf_2 = [normalize('NFC', a) for a in os.listdir() if a.endswith(".pdf")]

    for pdf in lista_pdf:

        if pdf not in lista_pdf_2:

            print(pdf + " no existe en la lista. CHAO")
            para_salir = input("Apreta cualquier tecla para salir")
            exit()


print("Hola, ahora voy a unir los archivos:")

print(" ")

print(lista_pdf)

try:
    for pdf in lista_pdf:
        merger.append(open(pdf, 'rb'), import_bookmarks=False)
    with open("Documentos " + carpeta + ".pdf", "wb") as fout:
        merger.write(fout)

except Exception as e:
    print(repr(e))
    print("Ok esto es serio, pide ayuda a alguien cercano, saca un pantallazo del mensaje de arriba")
    input("Apreta cualquier tecla para salir")

print(" ")
print("Todo listo, revisa el archivo 'Documentos " + carpeta + ".pdf' (en la carpeta que me dijiste :) ")

para_salir = input("Apreta cualquier tecla para salir, gracias por su preferencia")
