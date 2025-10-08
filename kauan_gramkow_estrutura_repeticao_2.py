# Faça um programa que leia 5 números e informe o maior número.
# Desenvolvido por Kauan Gramkow

n1 = int(input("Informe o seu primeiro número: "))
n2 = int(input("Informe o seu segundo número: "))
n3 = int(input("Informe o seu terceiro número: "))
n4 = int(input("Informe o seu quarto número: "))
n5 = int(input("Informe o seu quinto número: "))

if n1 > n2:
    print(f"{n1} é o maior.")
elif n2 > n3:
    print(f"{n2} é o maior.")
elif n3 > n4:
    print(f"{n3} é o maior.")
elif n4 > n5:
    print(f"{n4} é maior.")
else:
    print(f"{n5} é o maior.")