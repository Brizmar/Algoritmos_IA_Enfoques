import os

def crear_archivos(num_archivos, ruta=r'C:\Users\brizu\OneDrive\Documentos\GitHub\IA_Enfoques\Probabilidad (Incertidumbre)'):
    for i in range(46, num_archivos + 1):
        nombre_archivo = f"{i:03d}__RPT.py"
        ruta_completa = os.path.join(ruta, nombre_archivo)
        with open(ruta_completa, 'w') as f:
            f.write(f"# Archivo {nombre_archivo}\n")
        print(f"Creado: {nombre_archivo}")

crear_archivos(53)
