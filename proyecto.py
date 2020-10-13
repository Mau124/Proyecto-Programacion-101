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
import os

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
    # print(*matrixQuestions, sep="\n")

    return matrixQuestions

def saveRecord(name, points):
    """Función que guarda los datos de un usuario"""
    # Header del archivo
    headerUsers = "Name,Points\n"

    with open("userPoints.csv", "w") as outputFile:
        outputFile.write(headerUsers)
        outputFile.write(name+","+str(points)+"\n")


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
    """Función que mantiene una sesión de un juego"""
    questions = readQuestions("questions.csv")
    attemps = 2
    auxAttemps = 0
    correct = 0
    
    while len(questions)>0:
        # os.system("cls") sistemas windows
        os.system("clear") # sistemas unix

        # Si ya no quedan intentos, tomamos otra pregunta aleatoria
        if auxAttemps<=0:
            if len(questions)>1:
                index = random.randint(0, len(questions)-1)
            else:
                index = 0
            auxAttemps = attemps
            
        printQuestion(questions[index])
        ans = input("¿Coloque el inciso de la respuesta que crea correcta?: ")
        ans = ans.lower()

        # Checa si la opcion tecleada por el usuario es valida
        if ans in ("abcd"):

            # Checamos si la respuesta dada por el usuario corresponde a la respuesta correcta
            if ans==questions[index][7]:
                print(f"Respuesta Correcta. +{(100/(attemps/auxAttemps)):.2f} puntos")
                correct += (100/(attemps/auxAttemps))
                auxAttemps = 0
                del questions[index]
            else:
                auxAttemps -= 1
                print(f"Respuesta Incorrecta. Te quedan {auxAttemps} intentos para esta pregunta")
                if auxAttemps<=0:
                    del questions[index]

        # Checha si la opción tecleada por el usuario es salir del juego
        elif ans=='s':
            accept = input("¿Estás seguro de que deseas salir de la aplicación? s/n: ")
            accept = accept.lower()
            if accept=='s':
                break;

        # Checha si la opción tecleada por el usuario no existe
        else:
            print("No existe la opción seleccionada. Intente otra vez")

        next = input("Presione enter para continuar: ")

    print(f"Puntos obtenidos: {correct}")
    saveRecord("Juanito", correct)

game()