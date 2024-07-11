from rdkit import Chem

def merge_sdf_files(file1, file2, output_file):
    # Cargar moléculas del primer archivo SDF
    suppl1 = Chem.SDMolSupplier(file1)
    # Cargar moléculas del segundo archivo SDF
    suppl2 = Chem.SDMolSupplier(file2)
    
    # Crear un escritor para el archivo de salida
    writer = Chem.SDWriter(output_file)
    
    # Escribir todas las moléculas del primer archivo
    for mol in suppl1:
        if mol is not None:  # Verificar que la molécula se haya leído correctamente
            writer.write(mol)
    
    # Escribir todas las moléculas del segundo archivo
    for mol in suppl2:
        if mol is not None:  # Verificar que la molécula se haya leído correctamente
            writer.write(mol)
    
    # Cerrar el escritor
    writer.close()

# Nombres de los archivos de entrada y salida
file1 = 'archivo1.sdf'
file2 = 'archivo2.sdf'
output_file = 'archivo_fusionado.sdf'

# Fusionar los archivos SDF
merge_sdf_files(file1, file2, output_file)

print(f'Archivos {file1} y {file2} han sido fusionados en {output_file}')
