# Projeto conclusão Voitto

#Criar vetor X de valor aleatório usando bibli random.
#Criar cópia de vetores; Plotar o gráfico histograma;
#Ordenar valores em uma lista e criar um algoritmo de sort()
#Calculo media, mediana, moda, desvio padrao e variância
#Armazenar as medidas de tendência central em um dict.
#Armazenar conteúdo do dict em um arquivo.

#Lista de 30 valores aleatórios entre 1 e 50.

import random

lista_aleatoria = [random.randint(1, 50) for i in range(30)]
print(lista_aleatoria)

la = list() #copia lista aleat. (n é o mesmo objeto)
for i in lista_aleatoria:
    la.append(i)
print(la)

import matplotlib.pyplot as plt #instalado numpy e matplotlib pelo terminal

plt.hist(lista_aleatoria)
plt.show()

def ordena_lista(lista):
    for i in range(1, len(lista)):
        eleito = lista[i]
        k = i
        while k > 0 and eleito < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
        lista[k] = eleito
    return lista
print(lista_aleatoria) #continua a mesma

lista_ordenada = ordena_lista(lista_aleatoria) #agora aplicando o algoritmo
print(lista_ordenada)

#Medidas de tendencia central

soma = 0                   #média
for l in lista_aleatoria: #agora ordenada
    soma += l
media = soma/len(lista_aleatoria)
print(media)
#media = sum(lista_aleatoria)/len(lista_aleatoria)

lista_aleatoria.sort()      #mediana
metade = len(lista_aleatoria) // 2
if len(lista_aleatoria) % 2 == 0:
    mediana = (lista_aleatoria[metade-1] + lista_aleatoria[metade]) / 2
else:
    mediana = lista_aleatoria[metade]
print(len(lista_aleatoria), metade, mediana)

val_atual = la[0]
moda = la[0]
cont = 1
max_cont = 0

for x in la[1:]:      #moda
    if x == val_atual:
        cont += 1
        if cont > max_cont:
            max_cont = cont
            if x != moda:
                moda = x
    else:
        cont = 1
        val_atual = x

print(max_cont, moda)

from collections import Counter
print(Counter(la))

import math as mt
media = sum(la)/len(la)        #desvio padrao
dif_media = [(media - x)**2 for x in la]
dev_padrao = mt.sqrt(sum(dif_media)/len(dif_media))
print(dev_padrao)

var = dev_padrao**2 #variancia
print(var)

inf = {'media': media,
       'mediana': mediana,
       'moda': moda,
       'desvio padrao': dev_padrao,
       'variancia': var}

print(inf)

arquivo = open('informações.txt', 'w')
arquivo.write(str(inf))
arquivo.close()





