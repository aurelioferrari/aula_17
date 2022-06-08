# ler vários números
# A) quantos numeros foram digitados
# B) lista ordenada de forma decrescente
# C) se o valor 5 foi inserido

count = 0
lista = []
while True:
    n = int(input("Digite um número: "))
    count += 1
    lista.append(n)
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while opcao not in "SsNn":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao in "Nn":
        break
lista.sort(reverse=True)
print(f'Foram digitados {count} números.')
print(f"A lista na ordem inversa é: {lista}")
if 5 in lista:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")