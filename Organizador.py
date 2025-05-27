import os
import shutil

# Ruta a la carpeta que quieres organizar (usa "." para carpeta actual)
ruta = "."

# Categorías y extensiones
tipos = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Música': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Programación': ['.py', '.js', '.html', '.css', '.java', '.c'],
    'Comprimidos': ['.zip', '.rar', '.7z'],
    'Otros': []
}

# Crear carpetas si no existen
for carpeta in tipos.keys():
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)

# Revisar archivos en la carpeta
for archivo in os.listdir(ruta):
    if os.path.isfile(archivo):
        nombre, extension = os.path.splitext(archivo)
        movido = False

        # Ver en qué carpeta debe ir
        for categoria, extensiones in tipos.items():
            if extension.lower() in extensiones:
                shutil.move(archivo, os.path.join(categoria, archivo))
                movido = True
                break

        # Si no encaja en ninguna categoría
        if not movido:
            shutil.move(archivo, os.path.join('Otros', archivo))

print("¡Archivos organizados con éxito!")
