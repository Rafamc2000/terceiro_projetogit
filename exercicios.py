import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#primero_numero = int(input("insira um numero: "))
#seg_num = int(input("insira outro numero: "))
#soma_resultado = int(primero_numero + seg_num)
#print(soma_resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#num = int(input("escolha numero:"))
#resultado_resto = (num // 5)
#divisao_5 = (f"O resto da divisão por 5 é:", resultado_resto)
#print(divisao_5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#num_um = int(input("digite numero: "))
#num_dois = int(input("digite numero dois: "))
#soma = num_um * num_dois
#print(soma)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#prim = int(input("prim: "))
#sec = int(input("sec :"))
#divi = int(prim // sec)
#if divi == 0:
 #   print("esse numero não pode ser divido por um numero menor que ele")
#else:
#    print(divi)


#numero_01 = int(input("Inserir um numero inteiro: "))
#numero_02 = int(input("Inserir outro numero inteiro: "))
#resultado = numero_01 // numero_02
#print(resultado)


# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#num = int(float(input("escolha um numero: ")))
#quad = str(num ** 2)
#print(quad)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#num = float(input("digite um numero: "))
#num2 = float(input("digite outro: "))
#res = num + num2
#print(res)


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#num = float(input("digite um numero: "))
#num2 = float(input("digite outro: "))
#media1 = float(num + num2) / 2 
#print(media1)


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#base = int(input("escolha : "))
#expoente = int(input("escolha: "))
#poten = int(base ** expoente)
#print("a potencia é igual" , poten)


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#FORMULA (0 °C × 9/5) + 32 = 32 °F
#celcius = float(int(input("quantos celsius: ")))
#farenhit = (celcius * 9) / 5 + 32
#print("convertendo o seu valor celcius para farenhit,fica  " , farenhit )

# python exercicios.py

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
##area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#string = input("digite uma frase: ")
#uper = string.upper()
#print(uper)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#string = input("digite uma frase: ")
#lower = string.lower()
#print(lower)

#### 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.





# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data = input("digite uma data no formato aa/aa/aaaa: ")
#texto_separado = data.slpit("/")
#print(texto_separado)

##data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
##lista_de_dia_mes_ano = data_do_usuario.split("/")
##print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
##print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
##print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

#python exercicios.py

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#primeira = input("frase1: ")
#segunda = input("frase2: ")
#prsc = primeira  + segunda
#print(prsc)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#n1 = float(input("ensira a temperatura: "))
#n2 = float(input("ensira outra temperatura: "))
#comparaçao = n1 > n2 and n1 <3
#print(comparaçao)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#n = int(input("digite: "))
#if n < 10 or n > 2 :
#    print("ta certo")
#else:
#    print("errado")


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#valor = True
#valor_boleano_invertido = not valor
#print(valor_boleano_invertido)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

#numero1 = input("numero: ")
#numero2 = input("numero2: ")
#igualdade = numero1 == numero2
#print("resultado da igualdade: ", igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
#nm = 3
#nm2 = 3
#rs = nm != nm2
#print(rs)

# #### try-except e if

#python exercicios.py

# 21: Conversor de Temperatura
#try:
#    celsius = float(input("Digite a temperatura em Celsius: "))
#    fahrenheit = (celsius * 9/5) + 32
#    print(f"{celsius}°C é igual a {fahrenheit}°F.")
#except ValueError:
#    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo(############NAO ENTENDI#######################)                     OLHAR NOVAMENTE

#entrada = input("Digite uma palavra ou frase: ")
#if isinstance(entrada, str):
#    formatado = entrada.replace(" ", "").lower()
#   if formatado == formatado[::-1]:                           
#        print("É um palíndromo.")
#    else:
#        print("Não é um palíndromo.")
#else:
#   print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
#n1 = float(input("n1: "))
#n2 = float(input("n2: "))
#res = float(n1 + n2)
#print(res)


# 24: Classificador de Números
n = 2.52
if isinstance(n, float):
    print("é um float")
else:
    print("Não é float")

# 25: Conversão de Tipo com Validação
