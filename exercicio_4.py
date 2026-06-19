primeira_lista = [*map(int, input("Digite a sua primeira lista (separando os números por vírgula): ").split(","))]
segunda_lista = [*map(int, input("Digite a sua segunda lista (separando os números por vírgula): ").split(","))]

maior_primeira = max(primeira_lista)
maior_segunda = max(segunda_lista)

if maior_primeira > maior_segunda:
    print("Primeira")
elif maior_segunda > maior_primeira:
    print("Segunda")
else:
    print("Ambas")
