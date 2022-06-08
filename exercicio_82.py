# ler varios numeros e colocar numa lista
# criar duas listas adicionais  mostrando os valores pares e impares

lista = []
pares = []
impares = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n %2 == 0:
        pares.append(n)
    if n % 2 != 0:
        impares.append(n)
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar? [S/N] "))
    if opcao in "Nn":
        break
print(f'A lista completa é: {lista}')
print(f'Os números pares foram: {pares}')
print(f'Os números ímpares foram: {impares}')