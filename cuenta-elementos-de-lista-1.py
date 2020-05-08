# cuenta-elementos-de-lista-1.py

cadenaPalabras = ''
# Using readlines() 
file1 = open('intrusion.txt', 'r') 
Lines = file1.readlines() 

cont_p=0
# Strips the newline character 
for line in Lines: 
     cadenaPalabras += line
     #print("cadenaPalabras\n" + cadenaPalabras +"\n")
     #cont_p=cont_p+1
     #print(cont_p)
     //
Algoritmo SubProcesoContadorPalabras(texto,palabra)
    para cada palabra del texto
        averiguar si la palabra esta
        y si  estar, incrementar en 1 el contador
    retornar el valor del contador
FinAlgoritmo 

Algoritmo SubProcesoContadorPalabras(texto,palabra)
    para cada palabra del texto
        averiguar si la palabra esta
        y si  estar, incrementar en 1 el contador
    retornar el valor del contador
FinAlgoritmo 

listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

#print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
#print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
