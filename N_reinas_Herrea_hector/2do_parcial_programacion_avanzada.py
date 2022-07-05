#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random 
import matplotlib.pyplot as plt


# In[2]:


class N_reinas:
    
    def __init__(self,n_reinas, n_pob_ini):
        self.n_reinas = n_reinas 
        self.n_pob_ini = n_pob_ini
        self.pob_ini = []
        self.lista_resu=[]
        self.lista_padres=[]
        self.padres=[]
        
    def gen_pob_inicial(self):
        '''Metodo encargado de generar la poblacion inicial'''
        pob_inicial=[]
        for i in range(self.n_pob_ini):
            individuo=random.sample(range(0,self.n_reinas),self.n_reinas) #genera una lista de valores unicos y aleatorios
            pob_inicial.append(individuo)
        self.pob_ini=pob_inicial
        
    def fitness(self):
        '''Metodo que evalua y clasifica a c/ individuo'''
        padres=[]                             #lista para guardar los individuos con mayor puntaje
        fitness=[]                            #lista para guardar la puntacion de c/ individuo de la la pob inicial
        for lista in self.pob_ini:
            for i,j in enumerate(lista,start=1):
                if i >= len(lista):               #chequea si alguna lista cumple las condiciones     
                    self.lista_resu=lista
                    return print("El primer resultado encontrado es: ",lista)
                else:
                    if lista[i] in (j+1,j-1):
                        fitness.append(i)             
                        break  

        max_puntaje=max(fitness)
        for k,l in enumerate(fitness):
            print(self.pob_ini[k])
            if l == max(fitness):
                padres.append(self.pob_ini[k])
        self.padres=padres
        self.cruzamiento()
           
    def cruzamiento(self):
        '''Metodo encargado de realizar la permutacion genetica de los individuos'''
        if len(self.padres)>1:
            padre_fuerte=[]
            for padre in self.padres:
                genes_fuertes=padre[:max_puntaje]
                genes_debiles=padre[max_puntaje:]
                print(genes_fuertes,genes_debiles)
                while len(genes_debiles)!=1:
                    j=random.choice(genes_debiles)
                    if j not in genes_fuertes:
                        genes_fuertes.append(j)
                        genes_debiles.remove(j)
                genes_fuertes.append(genes_debiles[0])
                padre_fuerte.append(genes_fuertes)
                print(genes_fuertes)
            self.pob_ini=padre_fuerte
            self.fitness()
        else:
            self.fitness()
            

    def mostrar_res(self):
        '''Metodo que imprime el primer individuo apto encontrado'''
        plt.scatter(x=[i for i in range(0,len(self.lista_resu))], y=self.lista_resu,s=250) #grafica los puntos
        plt.xlim(-0.5,len(self.lista_resu)-0.5)           #Expande la impresion del grafico para que los puntos queden centrados
        plt.ylim(-0.5,len(self.lista_resu)-0.5)
        for i in range(len(self.lista_resu)-1):           #Este bucle dibuja las lineas q corresponden a la cuadricula
            plt.axhline(y=i+0.5,c='black')      
            plt.axvline(x=i+0.5,c='black')


# In[3]:


test_uno = N_reinas(5,100)
test_uno.gen_pob_inicial()
test_uno.fitness()
test_uno.mostrar_res()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




