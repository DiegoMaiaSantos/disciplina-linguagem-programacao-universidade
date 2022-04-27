print("")
print("Hello world!")

x = 10
nome = 'Aluno'
nota = 8.75
fez_inscricao = True

print("")
print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))
print("")

nome2 = input("Digite um nome: ")
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" % (nome2))
print("")

nome3 = input("Digite um nome: ")
print("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world".format(nome3))
print("")

# A melhor forma é a f-string

nome4 = input("Digite um nome: ")
print(f"Olá {nome4}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world")
print("")

calc1 = 2 + 3 * 5
calc2 = (2 + 3) * 5
calc3 = 4 / 2 ** 2
calc4 = 13 % 3 + 4

print(f"Resultado do calc1 = {calc1}")
print(f"Resultado do calc2 = {calc2}")
print(f"Resultado do calc3 = {calc3}")
print(f"Resultado do calc4 = {calc4}")
print("")

a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")

print(type(a))
print(type(b))
print(type(c))
print(type(x))
print("")

x = float(x)

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}.")
print("")

print(type(a))
print(type(b))
print(type(c))
print(type(x))
print("")