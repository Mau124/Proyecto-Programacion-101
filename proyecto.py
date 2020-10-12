"""
Proyecto integrador
Materia: Pensamiento computacional para ingeniería
Alumno: Mauricio Andrés Flores Pérez
Matricula: A01639917

Descripcion del programa:
Programa que realiza preguntas tipo PISA a estudiantes para mejorar su rendimiento en este 
tipo de examenes.
"""
import random

def readQuestions(fileName):
    """Función que lee las preguntas desde un archivo csv y retorna una matriz con ellas"""

    # Leemos el archivo
    file = open(fileName, "r")
    questions = []
    for row in file:
        questions.append(row)
    file.close()

    # Guardamos las preguntas dentro de una matriz
    matrixQuestions = []
    for row in questions:
        matrixQuestions.append(row.strip().split(","))
    
    # Imprimiendo la matriz para comprobar que los datos han sido guardados
    print(*matrixQuestions, sep="\n")

    return matrixQuestions

def printQuestion(question):
    """Función que imprime con formato una pregunta"""
    opt = ['a', 'b', 'c', 'd']
    cont = 0
    
    print(f"{question[1]}")
    print(f"{question[2]}")
    for i in range(3, len(question)-1):
        print(f"{opt[cont]}) {question[i]}")
        cont += 1
    

def game():
    """Función que inicializa una partida de juego y mantiene la sesión de un juego"""
    questions = readQuestions("questions.csv")
    correct = 0
    
    while correct<10:
        if len(questions)>1:
            index = random.randint(0, len(questions)-1)
        else:
            index = 0
            
        printQuestion(questions[index])
        next = input()
        del questions[index]
        
        correct += 1

game()