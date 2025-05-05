# print(int(input("Digite um numero: ")) + int(input("Digite outro numero: ")))

# numero = 3 # int
# numero_decimal = 4.78 #float
#nome_de_usuario = "Rafael" #string
# verdadeiro = True #bool

#nome = input("Qual seu nome :")
#idade = input("Qual a sua idade?: ")
#Quantida_de_letras = len(nome)
#quantidade_de_numeros_idade = len(idade)
#print (Quantida_de_letras )
#print (quantidade_de_numeros_idade)


nome_usuario = input("Digite o seu nome: ")
valor_salario = int(input("Qual seu salario?: "))
valor_bonus = float(0.10)
valor_adiçao = int(1000)

bonus_final = valor_salario * valor_bonus
soma_com_bonus = bonus_final + valor_salario
salario_total = soma_com_bonus + valor_adiçao

print (f"Olá { nome_usuario} o seu salario sera de {salario_total}") 