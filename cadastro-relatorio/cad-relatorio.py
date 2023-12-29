dados = {}
lista = []
sig = ' '
media = soma = 0
while True:
    dados.clear()
    dados ["Nome"] = str(input("Digite o nome: "))
    dados ["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
    while dados["Sexo"] not in "MF":
        print("ERRO! Digite apenas F ou M")
        dados["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
        if dados ["Sexo"] in "MF":
            break
    dados ["Idade"] = int(input("Idade: "))
    soma += dados ["Idade"]
    lista.append(dados.copy())
    sig = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    while sig not in "NS":
        print("Opção inválida: Apenas S ou N")
        sig = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if sig == "N":
        break
media = soma / len(lista)
print("-="*30)
print(f"A)- No total foram cadastradas {len(lista)} pessoas!")
print(f"B)- A média de idade é igual a {media:5.2f} anos ")
print(f"C)- O nome de todas as Mulheres são: ", end="")
for p in lista:
    if p["Sexo"] in "F":
        print(f"{p['Nome']},",end=" ")
print()
print("D)- A lista das pessoas acima da média são: ",end=" ")
for n in lista:
    if n["Idade"] > media:
        print(f"{n['Nome']},", end=" ")