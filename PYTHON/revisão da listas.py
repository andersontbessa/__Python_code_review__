import math


lista = [1,2,3,4,5,6]

#para chamar um número da lista
print (lista[3])

#increntar um valor no último espaço
lista= lista + [9]
print(lista)

#somar elementos contidos na lista
lista [4] + lista[2] 
print(lista [4] + lista[2])

#inserir um número em alguma posição da lista
lista[2] = 7.7
print(lista)

#criar lista através de uma variável
a=1
b=2
c=5

lista = [a,b,c]
print (lista)

#slice
lista[1:3] #quer dizer que vai de tal elemento até tal elemento. Ou seja, nesse exemplo vai do elemento da posição 1 até a posição 3-1, ou seja, é como o for in range, e insere dentro de outra lista
print(lista[1:3])
lista[:] #percorre do primeiro ao último
print(lista[:])
#obs: lista[3:2] por exemplo retorna uma lista fazia. Só funciona se for lista[2:-1], um positivo na frente maior e um negativo menos atrás.
lista [::] #significa percorrer o elemento tal até o elemento tal, com passo e tal tipo de 2 a 2 etc.
lista [::-1] #inverte a lista
lista [::-2] #inverte a lista e percorre do último de dois a dois


#para obter um número dentro da lista tendo em vista duas listas juntas
listazinha= [1,2,3,4,[1,2,3,4]]
print (listazinha[4][2]) #4 é a posição da lista que está dentro, e o 2 é a posição que está dentro da lista interna.
listazinhaoutra =[[[1,2],[3,4]],[5,6]]
print (listazinhaoutra[1])# acha a segunda lista dentro dessa lista. a segunda lista seria o [5,6], pois as duas outras listas estão dentro de uma só.
print (listazinhaoutra[0][1]) #o 0 é a lista[1,2],[3,4] e o 1 é a lista [3,4] mais interna.
print (listazinhaoutra[0][1][0])



#Append() serve para inserir valores dentro de uma lista
linst = [] #logo aqui nessa lista vai reter os valores de 1 a 6
for i in range(1,6+1):
    linst.append(i)
print(linst)

#len() serve para saber o número de elementos dentro de uma lista
listit = [1,5,8,9,79,8,79]
print (len(listit)) #ou seja, tem 7 elementos dentro da list "listit"

#o count() fala quantos números iguais aparecem na lista
linst4 = [1,1,1,2,4,4]
print (linst4.count(1)) #vai dizer que o 1 aparece três vezes.

#for loops e listas
numeros = [1,2,"c",4]
for i in numeros: # faz isso para percorrer todos os números dentro da lista.
    print("vai percorrer",i) 

#split() -> dividir uma string #str. Pega strings e separa e coloca em uma lista elas separadas.
num = "olá tudo bem bem bem"
print(num.split())

ae = num.split()

for i in ae:
    print (i,"->" ,ae.count(i))

#sum() --> O sum pega todos os valores que estão dentro da lista e soma todos.
#obs: pode ser valores em lista ou não. Se fosse só num =1, 2, 3, 4 ele somaria.   
#num = [1,2,3,4]
#print(sum(num)

#max() escolhe o maior número de uma lista. Mas necessita ser uma lista.
#import math
#lista=['aeeee']
#print (max(lista))

#min() escolhe o menor
#import math
#lista=['aeee']
#print (max(lista))

#List Comprehensions --> uma forma de encurtar o código com listas
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1] #coloca os valores de "l1" em uma variável chamada "variável" e criando uma nova lista
print("os números que vão para variável são",l2,"\n")



l2 = [variavel * 2 for variavel in l1] #multiplica por 2 cada elemento da lista variável
print(l2)

#zip () --> #acompanha o for loop até a menor lista, listando as duas listas ao mesmo tempo
l1 = [5,1,7,9,5,6,7,8,9]
l2 = [21,42,4]

for x1, x2 in zip(l1, l2): #acompanha o for loop até a menor lista, listando as duas listas ao mesmo tempo
    print(x1,x2)




