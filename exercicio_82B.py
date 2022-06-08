lista = []
pares = []
impares = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar? [S/N] "))
    if opcao in "Nn":
        break
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'A lista completa é: {lista}')
print(f'Os números pares foram: {pares}')
print(f'Os números ímpares foram: {impares}')