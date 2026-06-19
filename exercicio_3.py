lista = [*map(int, input("Digite a sua lista (separando os números por vírgula): ").split(","))]

impares = []

for numero in lista:
    if numero % 2 != 0:
        impares.append(numero)

print("Os números ímpares são", impares)
