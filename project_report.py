import os

def contar_lineas_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        return sum(1 for linea in f)

def mostrar_arbol_directorio(directorio):
    total_lineas = 0
    last_slash = 0
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith('.py'):
                ruta_archivo = os.path.join(raiz, archivo)
                lineas = contar_lineas_archivo(ruta_archivo)
                total_lineas += lineas
                
                current_slash = ruta_archivo.rfind("\\")
                if last_slash != current_slash:
                    print()
                last_slash = current_slash
                
                treshold = lineas > 75
                print(f"{ruta_archivo[len(directorio)+1:]}: {lineas} líneas", "***" if  treshold else "")
    print(f"\nTotal de líneas de código: {total_lineas}")

if __name__ == "__main__":
    directorio_actual = os.getcwd()
    print(f"Explorando directorio: {directorio_actual}\n")
    mostrar_arbol_directorio(directorio_actual)