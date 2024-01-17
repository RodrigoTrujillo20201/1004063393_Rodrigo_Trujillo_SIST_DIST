#Ordenamiento burbuja
import random
def ordenamiento_burbuja(lista):
    for n in range(len(lista) -1, 0, -1): 
        for i in range(n): 
            if lista [i] > lista [i + 1]: 
                temp = lista[i]  
                lista[i] = lista [i + 1] 
                lista [i + 1] = temp 

numeros = random.sample(range(100), 100)
print("Lista desordenada")
print(numeros)
print("Lista ordenada")
ordenamiento_burbuja(numeros)
print(numeros)
