import os

def count_file_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

def show_tree_dir(dir_path):
    total_lines = 0
    total_files = 0
    last_slash = 0
    for raiz, _, files in os.walk(dir_path):
        for filename in files:
            if filename.endswith('.py'):
                file_path = os.path.join(raiz, filename)
                lines = count_file_lines(file_path)
                total_lines += lines
                
                current_slash = file_path.rfind("\\")
                if last_slash != current_slash:
                    print()
                last_slash = current_slash
                
                treshold = lines > 75
                print(f"{file_path[len(dir_path)+1:]}: {lines} líneas", "***" if  treshold else "")
                total_files += 1
    print(f"\nTotal de líneas de código: {total_lines}")
    print(f"Total de Archivos: {total_files}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Explorando directorio: {current_dir}")
    show_tree_dir(current_dir)