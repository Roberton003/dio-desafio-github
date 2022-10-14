###Desafio 1
#As Duas Torres
##Entrada
#A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

##aída
##Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais.

#distancia = int(input ("Digite uma valor da distância entre as duas torres com número inteiro n, 0 < n < 10000. "))
#diametro1 = int(input ("Digite uma valor do diâmetro da torre 1, número inteiro x, x > 0."))
#diametro2 = int(input ("Digite uma valor do diâmetro da torre 2, número inteiro y, y < 100."))

entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:

icm =  distancia / (diametro1+diametro2)
print(f"{icm:.2f}")