###Desafio 3
#Cálculo de viagem
#calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro,
#  sendo que seu carro faz 12 KM/L. 
# Abaixo segue um exemplo de código que você pode ou não utilizar
#Entrada
#O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto 
# na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

#Saída
#Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal
valores = input().split()

velocidade_media = int(valores[0])
tempo_viagem = int(valores[1])
km_por_litro = 12

#Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal

quantidade_litros = (velocidade_media * tempo_viagem) / km_por_litro

print (f' {quantidade_litros:.3f}')