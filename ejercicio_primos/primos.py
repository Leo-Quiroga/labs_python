# Script para imprimir los números primos del 1 al 250
# y guardar el resultado en un archivo

# Función que define si un número es primo

def es_primo(n):
        if n < 2:
                return False
        for i in range (2, n):
                if  n % i == 0:
                        return False
        return True

# Lista que guarda lo números primos encontrados

primos = []

# Este for toma cada número del 1 al 250, lo pasa por la función
# Si es primo, lo guarda en la lista primos

for numero in range(1, 251):
        if es_primo(numero):
                primos.append(numero)

# Guardar el resultado en un archivo

with open("result.txt", "w") as archivo:
        for p in primos:
                archivo.write(str(p) + "\n")

print("Proceso terminado.")
print("Se encontraron", len(primos), "números primos.")
print("Resultados guardados en result.txt")
