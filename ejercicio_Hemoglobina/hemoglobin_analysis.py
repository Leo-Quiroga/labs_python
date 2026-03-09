#Script de análsis de Hemoglobina
from collections import Counter

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
print("Frecuencias de residuos (parcial):", counts.most_common(5)) # muestra los 5 aminoácidos más comunes