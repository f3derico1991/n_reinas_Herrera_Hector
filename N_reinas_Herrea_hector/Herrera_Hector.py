#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import random 
import matplotlib.pyplot as plt


# In[3]:


class N_reinas:
    
    def __init__(self,n_reinas, n_pob_ini):
        self.n_reinas = n_reinas 
        self.n_pob_ini = n_pob_ini
        self.pob_ini = []
        self.lista_resu=[]
        self.lista_padres=[]
        
    def gen_pob_inicial(self):
        lista_valores = [i for i in range(self.n_reinas)]   #lista con tantos valores unicos como reinas
        lista=lista_valores
        for i in range(self.n_pob_ini):                     #se crean n listas aleatorias a partir de mezclar "lista_valores"
            for i in range(self.n_reinas):
                lista_valores = [i for i in range(self.n_reinas)]
                lista=lista_valores
                indice_aleatorio = random.randint(0, self.n_reinas - 1)
                temporal = lista[i]
                lista[i] = lista[indice_aleatorio]
                lista[indice_aleatorio] = temporal
            self.pob_ini.append(lista)
            self.pob_ini.append([2 ,4, 1, 3, 0])
        print(self.pob_ini)
        return self.pob_ini
        
    def fitness(self):
        padres=[]
        fitness=[]
        for lista in self.pob_ini:
            for i,j in enumerate(lista,start=1):
                if i >= len(lista):                     #si la lista cumple con todas las condiciones es la respuesta
                    self.lista_resu=lista
                    return print("El primer resultado encontrado es: ",lista)
                else:
                    if lista[i] in (j+1,j-1):
                        fitness.append(i)             #Se guarda el indice(puntaje) hasta que la lista cumple la condicion 
                        break  

        max_puntaje=max(fitness)               #Este bucle guarda los individuos con mayor puntaje
        for k,l in enumerate(fitness):
            print(self.pob_ini[k])
            if l == max(fitness):
                padres.append(self.pob_ini[k])
        padre_fuerte=[]

        if len(padres)>1:
            for padre in padres:
                genes_fuertes=padre[:max_puntaje]
                genes_debiles=padre[max_puntaje:]
                print(genes_fuertes,genes_debiles)
                while len(genes_fuertes)<self.n_reinas:
                    j=random.choice(genes_debiles)
                    if j not in genes_fuertes:
                        genes_fuertes.append(j)
                padre_fuerte.append(genes_fuertes)
                print(genes_fuertes)
            self.pob_ini=padre_fuerte
            self.fitness()
        else:
            self.fitness()
            

    def mostrar_res(self):
        plt.scatter(x=[i for i in range(0,len(self.lista_resu))], y=self.lista_resu,s=250) #grafica los puntos
        plt.xlim(-0.5,len(self.lista_resu)-0.5)           #Expande la impresion del grafico para que los puntos queden centrados
        plt.ylim(-0.5,len(self.lista_resu)-0.5)
        for i in range(len(self.lista_resu)-1):           #Este bucle dibuja las lineas q corresponden a la cuadricula
            plt.axhline(y=i+0.5,c='black')      
            plt.axvline(x=i+0.5,c='black')


# In[4]:


test_uno = N_reinas(5,)
test_uno.gen_pob_inicial()
test_uno.fitness()
test_uno.mostrar_res()


# In[ ]:




