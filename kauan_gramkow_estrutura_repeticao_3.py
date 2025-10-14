# Faça um programa que leia 5 números e informe a soma e a média dos números.
# Desenvolvido por Kauan Gramkow

n1 = int(input("Informe o seu primeiro número: "))
n2 = int(input("Informe o seu segundo número: "))
n3 = int(input("Informe o seu terceiro número: "))
n4 = int(input("Informe o seu quarto número: "))
n5 = int(input("Informe o seu quinto número: "))

soma = n1 + n2 + n3 + n4 + n5
media = (n1 + n2 + n3 + n4 + n5) / 5
print(f"A soma entre {n1}, {n2} , {n3}, {n4} e {n5} é = {soma}")
print(f"A média entre {n1}, {n2}, {n3}, {n4} e {n5} é = {media}")