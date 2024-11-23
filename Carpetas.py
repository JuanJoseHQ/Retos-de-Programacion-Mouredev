import os

for i in range(5, 47):
    carpeta = str(i)
    os.makedirs(carpeta, exist_ok=True)
    with open(os.path.join(carpeta, "ejercicio.md"), "w") as archivo:
        archivo.write("")