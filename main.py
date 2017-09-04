#***************************************************************************************************
#                        PROGRAMA PARA RESOLUÇÃO DE SISTEMAS LINEARES
#***************************************************************************************************
import sys
import numpy as np

def entrada(texto):
    try:
        a = int(input(texto))
        if (a < 0):
            print('O número de incógnitas não pode ser negativo.')
            sys.exit(0)
        return a
    except (ValueError, TypeError):
        print('Não foi digitado um número inteiro válido.')
        sys.exit(0)

def entrada_real(texto):
    try:
        a = float(input(texto))
        return a
    except (ValueError, TypeError):
        print('Não foi digitado um número inteiro ou real válido.')
        sys.exit(0)


print('RESOLUÇÃO DE SISTEMAS LINEARES.')
num_inc = entrada('Digite o número de incógnitas do sistema:')

num_equacao = np.zeros((num_inc,num_inc+1), dtype=np.float)  #Forma a matriz principal
resultado = np.zeros((num_inc), dtype=np.float)              #Forma o conjunto resultado

print('Obs: O último coeficiente de cada equação será o termo independente.')
count_eq = 0
while(count_eq < num_inc):                 #Localiza a equação atual
    count_inc = 0
    while(count_inc < num_inc+1):           #Localiza o coeficiente
        num_equacao[count_eq,count_inc] = entrada_real('Equação '+str(count_eq+1)+' - termo '+str(count_inc+1)+':')
        count_inc += 1
    count_eq += 1

cramer = np.zeros((num_inc+1, num_inc, num_inc), dtype=np.float)    #Cria matrizes de Cramer

#Cria cópias das matrizes cramer só com os coeficientes
count_cramer = 0
while(count_cramer <= num_inc):
    count_cramer_col = 0
    while(count_cramer_col < num_inc):
        count_cramer_row = 0
        while(count_cramer_row < num_inc):
            cramer[count_cramer, count_cramer_row, count_cramer_col] = num_equacao[count_cramer_row, count_cramer_col]
            count_cramer_row += 1
        count_cramer_col += 1
    count_cramer += 1

#Mtriz dos termos independentes
independente = np.zeros((num_inc), dtype=np.float)
count = 0
while(count < num_inc):
    independente[count] = num_equacao[count, num_inc]
    count += 1

#Modifica as matrizes de cramer substituindo as colunas pelos termos independentes
count = 0
count_cramer = 1
while(count_cramer <= num_inc):
    for i in independente:
        cramer[count_cramer, count, count_cramer-1] = i
        count += 1
    count = 0
    count_cramer += 1

#Cálculo das incógnitas
Det = np.linalg.det(cramer[0])  #Determinantes da matriz dos coeficientes
count = 1
while(count <= num_inc):
    resultado[count-1] = (np.linalg.det(cramer[count]))/Det
    count += 1

print('Matriz principal:')
print(num_equacao)
#print('Matriz de cramer:')
#print(cramer)
#print('Matriz dos termos independentes:')
#print(independente)
print('Matriz Resultados [x, y, z,...,n]')
print(resultado)



