# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:15:56 2021

@author: T440p
"""

from numpy import *
from numpy import random
import numpy as np


print("Bienvenido a MEMORICE\nIngrese el número de cartas a jugar: \n")
cards = int(input())

# lista de variables a usar
player1 = 1
player2 = 2
random_list = []
c = 0

# se crean los tableros, el que está con los valores ocultos y el que se muestra incógnito,
# primero, como matrices llenas de ceros que serán reemplazadas con valores aleatorios.

hidden_board = np.zeros((cards,2))
board = np.zeros((cards,2))

# se desordena la primera columna y se inserta en el tablero.
for i in range(cards):
    random_list.append(i+1)
random.shuffle(random_list)
for i in hidden_board:
    i[0] = random_list[c]
    c += 1
# mismo proceso con la segunda columna.
c = 0
random.shuffle(random_list)
for i in hidden_board:
    i[1] = random_list[c]
    c += 1

# se imprime el tablero incógnito, llamado board
c = 0
print("   1  2 ")
for n in board:
    print(c,n)
    c += 1

#------------------------------------------------------------------------------------------------------------------    
# comienza el juego
print("\nEL JUEGO HA COMENZADO\nPor favor seleccione la carta que desea voltear(Use de referencia las coordenadas indicadas, eje: 0,1)\n")

# se definen los contadores
c = 0
c1 = 0
c2 = 0

# se inicia un ciclo que termina cuando todos los valores son adivinados.
while True:
    # Esta condición es para cuando ya se ha adivinado el total de los números pares y se pueda
    # definir un ganador, o si hay un empate. Su ubicación de debe a que el juego puede acabar
    # luego del turno del jugador 2 o el jugador 1, por tanto se repite en esta línea y en la
    # linea 104 para que no pregunte de más el programa.
    if (board == hidden_board).all() == True:
        if c1 == c2:
            print("\nEMPATE")
            break
        if c1 < c2:
            print("\nEL JUGADOR 2 HA GANADO")
            break
        if c1 > c2:
            print("\nEL JUGADOR 1 HA GANADO")
            break
    # Aquí se inicia el juego, comenzando el jugador 1 y preguntando por ambas cartas
    print("---------------------")    
    print("|TURNO DEL JUGADOR",player1,"|")
    print("---------------------")
    move1 = input("Ingrese la coordenada de la primera carta: ")
    move1 = move1.split(",")
    print("   0  1 ")
    board[int(move1[0])][int(move1[1])] = hidden_board[int(move1[0])][int(move1[1])]
    for b in board:
        print(c,b)
        c += 1
    c = 0
    move2 = input("Ingrese la segunda coordenada de la segunda carta: ")
    move2 = move2.split(",")
    print("   0  1 ")
    board[int(move2[0])][int(move2[1])] = hidden_board[int(move2[0])][int(move2[1])]
    for b in board:
        print(c,b)
        c += 1
    # si el jugador adivina, se le suma 1 punto a su contador y muestra los marcadores de ambos
    # y además se mantienen aa la vista los valores adivinados (Decidí dejar esto así, debido a
    # que al ser una matriz de floats, no logré reemplazar los números adivinados por espacios
    # vacíos)    
    if hidden_board[int(move1[0])][int(move1[1])] == hidden_board[int(move2[0])][int(move2[1])]:
        c1 += 1
        print("\nACERTASTE","\nC1 = ",c1,"\nC2 = ",c2)
        continue
    # si falla, las cartas vuelven a 0 para ocultarse
    else:
        print("\nFALLASTE","\nC1 = ",c1,"\nC2 = ",c2)
        
        board[int(move1[0])][int(move1[1])] = 0
        board[int(move2[0])][int(move2[1])] = 0
#------------------------------------------------------------------------------------------------------        
# Esta condición está repetida en la línea 54, ya que el juego puede acabar tanto en el turno del
# player 1 como el player 2.

    if (board == hidden_board).all() == True:
        if c1 == c2:
            print("Empate")
            break
        if c1 < c2:
            print("El jugador 2 ha ganado")
            break
        if c1 > c2:
            print("El jugador 1 ha ganado")
            break
#------------------------------------------------------------------------------------------------------
# Esta parte del código repite el proceso anterior. Pregunta cuales cartas voltear al jugador 2,
# para luego ver si son iguales
    c = 0
    print("---------------------")    
    print("|TURNO DEL JUGADOR",player2,"|")
    print("---------------------")
    move1 = input("Ingrese la coordenada de la primera carta: ")
    move1 = move1.split(",")
    print("   0  1 ")
    board[int(move1[0])][int(move1[1])] = hidden_board[int(move1[0])][int(move1[1])]
    for b in board:
        print(c,b)
        c += 1
    c = 0
    move2 = input("Ingrese la segunda coordenada de la segunda carta: ")
    move2 = move2.split(",")
    print("   0  1 ")
    board[int(move2[0])][int(move2[1])] = hidden_board[int(move2[0])][int(move2[1])]
    for b in board:
        print(c,b)
        c += 1
    c = 0
    if hidden_board[int(move1[0])][int(move1[1])] == hidden_board[int(move2[0])][int(move2[1])]:
        c2 += 1
        print("\nACERTASTE","\nC1 = ",c1,"\nC2 = ",c2)
        continue
    else:
        print("\nFALLASTE","\nC1 = ",c1,"\nC2 = ",c2)
        board[int(move1[0])][int(move1[1])] = 0
        board[int(move2[0])][int(move2[1])] = 0
    c = 0
    


    