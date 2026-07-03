nome=str(input("Escreva o seu nome: "))
sal=int(input(f"Sr(a) {nome} digite seu salario de forma arredondada: "))
emp=int(input("Digite o valor do emprestimo: "))

if sal*0.3>=emp:
    print(f"Sr(a) {nome}, sua transacao foi aprovada!")
else:
    print(f"Sr(a) {nome}, sua transacao foi negada!")
