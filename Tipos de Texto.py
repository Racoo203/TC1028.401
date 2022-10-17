import random

def generarPreguntaTexto():
    # Ejercicios de figuras retóricas
    Texto = open("Tipos de Texto P4.csv","r",encoding="utf-8") #Abrirb el docunto con las preguntas
    preguntas = []

    for linea in Texto: #Sacar las preguntas del documento 
        temp = linea.split("/") #Divididrlas si es necesario
        preguntas.append(temp)#Agregar a la varable preguntas

    Texto.close()

    # Selección de ejercicio
    num = random.randint(0,len(preguntas)-1)
    ejercicio = preguntas[num] #De todas las preguntas escoge una aleatoria  


    # Respuestas de los ejercicios
    Texto = open("Texto R.csv", encoding="utf-8") #Para abriri el documento con las respuestas
    respuestas = [] 

    for linea in Texto: #Igual sacar todas las respuestas del documento
        txt = linea.replace("\n","") #Verificar las respuestas y remplazar si es necesario
        temp = txt.split("/")
        respuestas.append(temp) #Agregar las respuestas en una variable

    Texto.close()

    # GUI
    for i in range(len(ejercicio)):# Ya es para enseñar la pregunta
        print(ejercicio[i])

    correcto = False
    
    
    respuesta = input("Indica la respuesta correspondientes:").lower() #Input para poner tu respuesta

    for i in range(len(respuestas[num])): 
        if respuesta == respuestas[num][i].lower(): #Verifica si la respuesta es la misma que la de la pregunta 
            correcto = True #Nos dice que pasa si es correcto

    if correcto:
        print("CORRECTO!") #Imprime Esto cuando es correcto
    else:
        print("Incorrecto, La respuesta correcta es:") #Imprime esto si esta incorrecta

    for i in range(len(respuestas[num])):
        print(respuestas[num][i]) #Aquí ya imprime la respuesta


generarPreguntaTexto()