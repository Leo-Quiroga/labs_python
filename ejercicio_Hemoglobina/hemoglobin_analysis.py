#Script de análsis de Hemoglobina
from collections import Counter
import json

#Creo lista de aminoácidos para almacenar la secuencia de la proteína
aminoacidosList = []

#Leer la secuencia desde el fichero .txt y meter cada letra en una lista

with open("ejercicio_Hemoglobina/hemoglobin_clean.txt", "r") as file: 
      seq = file.read().strip()          # elimina posibles saltos de línea
aminoacidosList = list(seq)          # ['M','V','H','L', …]

# información sobre la secuencia
print(f"Longitud de la cadena: {len(aminoacidosList)} aminoácidos")
print(f"Primeros 10 residuos: {''.join(aminoacidosList[:10])}")

# conteo de cada aminoácido más común
counts = Counter(aminoacidosList) # cuenta la frecuencia de cada aminoácido
print("Frecuencias de residuos:", counts.most_common(19)) # muestra los 19 aminoácidos

# Calcular el peso molecular
# Diccionario con pesos moleculares de los aminoácidos

aminoacidos_pesos = {
    "A": 89.09,   # Alanine
    "R": 174.20,  # Arginine
    "N": 132.12,  # Asparagine
    "D": 133.10,  # Aspartic Acid
    "C": 121.16,  # Cysteine
    "E": 147.13,  # Glutamic Acid
    "Q": 146.15,  # Glutamine
    "G": 75.07,   # Glycine
    "H": 155.16,  # Histidine
    "I": 131.17,  # Isoleucine
    "L": 131.17,  # Leucine
    "K": 146.19,  # Lysine
    "M": 149.21,  # Methionine
    "F": 165.19,  # Phenylalanine
    "P": 115.13,  # Proline
    "S": 105.09,  # Serine
    "T": 119.12,  # Threonine
    "W": 204.23,  # Tryptophan
    "Y": 181.19,  # Tyrosine
    "V": 117.15   # Valine
}

#Función que calcula el peso molecular de la proteína sumando los pesos de cada aminoácido
def calcular_peso_molecular(secuencia): 
    peso_total = 0.0
    for aminoacido in secuencia:
        peso_total += aminoacidos_pesos.get(aminoacido, 0) # suma el peso del aminoácido, si no se encuentra devuelve 0
    return peso_total

peso = calcular_peso_molecular(aminoacidosList)
print(f"Peso molecular de la hemoglobina: {peso:.2f} Da")

# preparar datos para exportar a JSON
resultados = {
    "nombre_proteina": "hemoglobina",
    "longitud": len(aminoacidosList),
    "conteo_aminoacidos": dict(counts),
    "peso_molecular": peso
}
# exportar resultados a un archivo JSON
with open("ejercicio_Hemoglobina/hemoglobin_results.json", "w") as fh:# abre el archivo para escritura
    json.dump(resultados, fh, indent=2, ensure_ascii=False) # guarda los resultados en formato JSON con indentación para mejor legibilidad
print("Datos guardados en hemoglobin_results.json")

#Calcular aminiácidos hidrofóbicos
aminoacidos_hidrofobicos = ["A", "I", "L", "M", "F", "W", "V"]  # Lista de aminoácidos hidrofóbicos
conteo_hidrofobicos = sum(counts[aa] for aa in aminoacidos_hidrofobicos) # Suma el conteo de aminoácidos hidrofóbicos
print(f"Cantidad de aminoácidos hidrofóbicos: {conteo_hidrofobicos}")
#Calcular porcentaje de aminoácidos hidrofóbicos
porcentaje_hidrofobicos = (conteo_hidrofobicos / len(aminoacidosList)) * 100 # Calcula el porcentaje de aminoácidos hidrofóbicos
print(f"Porcentaje de aminoácidos hidrofóbicos: {porcentaje_hidrofobicos:.2f}%")