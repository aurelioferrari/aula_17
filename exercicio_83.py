# verificar se os parêntesis de uma expressão estão fechados corretamente

exp = str(input("Digite a expressão matemática: "))
lista = []

for i in exp:
    if i == "(":
        lista.append("(")
    if i == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")

if len(lista) == 0:
    print("Está correto.")
else:
    print("Não está correto.")