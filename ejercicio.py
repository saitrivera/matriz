import numpy as np 
matriz = np.array([[2,4,5],
                   [5,6,7],
                   [7,8,0],
                   [5,6,7]])

while matriz.shape[1]>0:
    print(matriz)
    seleccion = input("elige la columa que quieres eliminar:1,2,3")
    if seleccion =='q':break
    if seleccion.isdigit() and 0 <= int(seleccion) <matriz.shape[1]:
        matriz = np.delete(matriz, int (seleccion) - 1,axis=1)
print("matriz final")
print(matriz)