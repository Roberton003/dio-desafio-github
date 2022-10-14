### Desafio 2
#Cachorros-Quentes
# escrever um programa para determinar o número médio de cachorros-quentes consumidos pelos participantes.

#Entrada
#A entrada consiste de uma única linha que contém dois inteiros H e P (1 ≤ H, P ≤ 1000)
#  indicando respectivamente o número total de cachorros-quentes consumidos e o número 
# total de participantes na competição.

#Saída
#Seu programa deve produzir uma única linha com um número racional representando
#  o número médio de cachorros-quentes consumidos pelos participantes. 
# O resultado deve ser escrito como um número racional com exatamente dois dígitos
#  após o ponto decimal, arredondado se necessário.

 #DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split() 
cachorros_quentes_consumidos = int(valores[0])
participantes = int(valores[1])


#Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.
media_cachorros_quentes_participante =  cachorros_quentes_consumidos/ participantes
print(f"{media_cachorros_quentes_participante:.2f}")

cachorro_quentes_consumidos = int(input ("Digite uma quantidade de cachorros-quentes com número inteiro h,1 ≤ h: "))
participantes = int(input ("Digite uma valor uma quantidade de participantes com  número inteiro p,  p ≤ 1000:"))


media_cachorros_quentes_consumidos =  cachorro_quentes_consumidos/ participantes
print(f"Valor de médio de cachorros-quentes consumidos: {media_cachorros_quentes_consumidos:.2f}")