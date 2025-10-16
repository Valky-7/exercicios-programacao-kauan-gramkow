# Faça um programa que leia 5 números e informe a soma e a média dos números.
# Desenvolvido por Kauan Gramkow

soma = 0
for i in range(1, 6):
    numero = int(input(f"Informe o {i}º número: "))
    soma += numero
media = soma / 5
print(f"A soma dos números é = {soma}")
print(f"A média dos números é = {media}")