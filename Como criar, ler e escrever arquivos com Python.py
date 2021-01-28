file = open ('abc.txt', 'w+') #cri um arquivo na mesma pasta que está esse arquivo do python
file.write('mew \n')#para escrever coisas dentro do arquivo
file.write('si py')

#lê todas as linhas
file.seek(0,0) 
print(file.read())

#lê de uma por uma
file.seek(0,0)
print (file.readline(), end='')
print (file.readline(), end='')

#lê e automaticamente transforma em uma lista
file.seek(0,0)
print (file.readlines())

#ou assim, mas sem transformar em listas.
file.seek(0,0)
for linha in file.readlines():
    print(linha, end='')

file.close() #fecha o arquivo

#outra forma de criar, ler e escrever.
try:
    file = open ('abc.txt', 'w+') 
    file.write('ola \n')
    file.seek(0,0)
    print(file.read())
finally:
    file.close()


#criar, ler e escrever com um gerenciador de texto, sem precisar fechar com close()
with open('abcde.txt', 'w+') as file:
    file.write('aqui estou usando o gerenciador de texto \n')
    file.seek(0,0)
    print(file.read())

#Arquivos em csv
#o csv separa os strings que estão dentro de uma lista ou de tuplas, em vírgulas, e joga no excel. Essa vírgulas justamente separa os elementos lá no excel para organzar.
import cv2
import csv
lista=['olá','3,4,8'] #se colocar "," entre as strigs, fica um abaixo da outra lá no excel.


with open('tabela.csv', 'w') as outfile: 
    writer = csv.writer(outfile)
    writer.writerows(lista) #o writerows recebe uma lista ou uma tupla contendo strings.



#w+ lê e continua a salvar as coisas que já estavam
#'r' lê o arquivo
#'a+' lê e adiciona coisas no arquivo sem apagar por completo. Ou seja, adiona coisas ao final do arquivo, conservando o que já estava. Cada vez que eu apertar f5 vai salvar o que já estava e acrescentaras mesmas coisas novamente ou coisas novas.
#
