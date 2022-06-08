# digitar vario numeros e cadastrar em uma lista
# nao deixar adicionar numeros repetidos
# mostrar em ordem crescente

lista = []
while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    opcao = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    while opcao not in "SN":
        opcao = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    while opcao in "Ss":
        numero = int(input("Digite um número: "))
        while numero in lista:
            numero = int(input("O número já foi adicionado. Digite um novo número: "))
        else:
            lista.append(numero)
            opcao = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if opcao in "Nn":
        break

lista.sort()
print("Os números digitados foram: ", end = "")
for c in lista:
    print(f'{c}', end = " ")
