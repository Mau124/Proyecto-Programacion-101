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

def readFromFile(fileName):
    """Función que lee los registros de un archivo y devuelve una matriz con ellos"""

    # Leemos el archivo
    file = open(fileName, "r")
    data = []
    for row in file:
        data.append(row)
    file.close()

    # Guardamos los registros dentro de una matriz
    matrixQuestions = []
    for row in data:
        matrixQuestions.append(row.strip().split(","))

    return matrixQuestions


def saveRecord(name, points, fileName):
    """Función que guarda los datos de un usuario"""
    with open(fileName, "a") as outputFile:
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


def printUsersRecords(record):
    """Función que imprime con formato los registros con nombre y puntos de los usuarios"""
    os.system("cls") 

    for i in range(len(record)):
        print(f"\t\t{record[i][0]}\t\t{record[i][1]}")   

    n = input("\n\tPresione enter para continuar: ")


def printInstructions():
    """Función que imprime las instrucciones del juego"""
    os.system("cls") 

    file = open("instructions.txt", "r")
    for row in file:
        print(row, end="")
    file.close()

    n = input("\n\tPresione enter para continuar: ")


def game(inputName, outputName, attemps, ):
    """Función que mantiene una sesión de un juego"""

    questions = readFromFile(inputName)
    auxAttemps = 0
    correct = 0
    exitGame = False

    name = input("\tColoque un nombre de usuario para comenzar: ")
    
    while len(questions)>0:
        os.system("cls") 

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
                exitGame = True
                break

        # Checha si la opción tecleada por el usuario no existe
        else:
            print("No existe la opción seleccionada. Intente otra vez")

        next = input("Presione enter para continuar: ")

    if not exitGame:
        print(f"Puntos obtenidos: {correct}")
        saveRecord(name, correct, outputName)


def gameMauricio():
    """Función que inicializa el juego"""
    """Realizado por: Mauricio Andrés Flores Pérez - A016300917"""

    # Inicializamos las variables
    opt = 0
    inputFile = "questions.csv"
    outputFile = "userPoints.csv"

    while opt!=4:
        os.system("cls")

        print("\t------------------------")
        print("\t-                      -")
        print("\t-     Juego PISA       -")
        print("\t-                      -")
        print("\t------------------------")
        print("\tBienvenido al juego PISA")
        print("\tEste juego te ayudará a mejorar tus habilidades en pruebas tipo PISA")
        print("\tSeleccione una opción del menú:\n")

        print("\t[1]. Iniciar una partida")
        print("\t[2]. Ver la sala de campeones")
        print("\t[3]. Ver instrucciones")
        print("\t[4]. Salir")

        opt = int(input("\tOpción: "))

        if opt==1:
            game(inputFile, outputFile, 2)
        elif opt==2:
            printUsersRecords(readFromFile(outputFile))
        elif opt==3:
            printInstructions()
        elif opt==4:
            print("\tAdiós. Gracias por participar")
        else:
            print("\tLa opción no existe. Intente otra vez")

gameMauricio()