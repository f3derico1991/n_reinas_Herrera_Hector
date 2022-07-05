# *2ª Parcial Programacion avanzada*
## Algoritmo Genetico N-Reinas
### Alumno: *Herrera Hector Federico*

1. [Planteo del problema](#id1)
2. [Patron de diseño](#id2)
3. [Diagrama de UML](#id3)
4. [Documentacion de lo codificado](#id4)
5. [Publicacion del codigo](#id5)

## 1. Planteo del problema <a name="id1"></a>
Consigna: Generar un programa en lenguaje de programacion python que a partir de un parametro definido por el usuario de N reinas, coloque estas n reinas en un tablero de NxN de tal forma que no se puedan comer entre si.

_Ejemplo: Posible manera en que podrian disponerse 5 reinas en un tablero de 5x5:_

<img src="https://github.com/f3derico1991/n_reinas_Herrera_Hector/blob/main/N_reinas_Herrea_hector/imagenes/CincoReinas.png" width=300 height=300>:

## 2. Patron de diseño <a name="id2"></a>
Para este punto en particular no fue posible encontrar un patron que de correspondiera al porgrama elaborado. Considero que quizas _Chain of Responsibility_ podria haberse adaptado.

## 3. Diagrama de UML <a name="id3"></a>
<img src="https://github.com/f3derico1991/n_reinas_Herrera_Hector/blob/main/N_reinas_Herrea_hector/imagenes/2022-07-04-10-51-app.diagrams.net.png" width=300 height=300>:

## 4. Documentacion de lo codificado <a name="id4"></a>
 ### Explicacion de la lógica del algoritmo elaborado:
 #### Aclaraciones:
 - Individuo: Estara compuesta de n_pob_ini individuos lo que resulta en una la lista de listas.
 - Poblacion: Sera representado por una lista con valores de 0 a n_reinas, estos valores seran únicos y estaran ordenados de manera aleatoria dentro de la lista. Por ejemplo un posible individuo para un caso de 5 reinas podria ser [4,2,0,1,3].
 
 *Utilizacion del programa:*
 - El usuario inicializa la clase `N_reinas(n_reinas,n_pob_ini)`, en esta paso es necesario definir la cantidad de reinas como asi tambien de poblacion inicial con la que el algoritmo debe comenzar a trabajar. Por ejemplo para 5 reinas y 10 individuos la instanciasion seria la siguiente: `test_uno = N_reinas(5,10)`

 - Instancioado el programa, el usuario debe ejecutar el metodo  comienza por debinir de manera aleatoria la problacion inicial, esto se realiza mediante el metodo 
`test_uno.gen_pob_inicial()`.
 
 - Generada la poblacion inicial, para obtener una de la posibles soluciones al problema se debe invocar la el metodo `test_uno.fitness()`.
 Este metodo evaluara a cada individuo y los puntuara segun el nivel de adaptacion a la consigna planteda. Posteriormente se seleccionaran los individuos con mayor puntaje los cuales formaran la poblacion padre. Concluido esto se ejecutara internamente el metodo `self.cruzamiento()`, este se encargada de que a cada induviduo de esta nueva problacion se le intercambiaran de manera aleatoria aquellos genes que no les permita cumplir las condiciones planteadas, posteriormente volveran a sometidos a evaluacion. Este proceso se repetira hasta que uno de los individuos cumpla la consigna inicial y retornara la lista correspondiente de la siguiente manera: `El primer resultado encontrado es: [3, 0, 2, 5, 1]`
 
 - Por ultimo se puede ejecutar opcionalmente el metodo `test_uno.mostrar_res()`, este metodo genera una grafica a partir de la lista encontrada como solucion. Para el ejemplo del paso anterior retornaria la siguiente imagen: 

<img src="https://github.com/f3derico1991/n_reinas_Herrera_Hector/blob/main/N_reinas_Herrea_hector/imagenes/print_solucion.png" width=400 height=300>:



## 5. Codigo en Python de la resolucion: <a name="id5"></a>
El siguiente link redirecciona al codigo:

[Codigo del algoritmo en Python de N-reinas](https://github.com/f3derico1991/n_reinas_Herrera_Hector/blob/main/N_reinas_Herrea_hector/2do_parcial_programacion_avanzada.py)
