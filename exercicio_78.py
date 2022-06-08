# ler 5 valores e guardar em uma lista
# mostrar o maior e o menor e suas respectivas posições

valores = list()
for v in range(1, 6):
    valores.append(int(input("Digite um valor: ")))
maior = max(valores)
menor = min(valores)
print(f'O maior valor é: {maior} e está na posição {valores.index(maior)+1}')
print(f'O menor valor é: {menor} e está na posição {valores.index(menor)+1}')