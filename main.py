# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
import random

import scipy.sparse

from faces import Faces
from smeg_matrix import *


file_path = '/Users/ruslanpepa/PycharmProjects/testrin-pycharm/octahedron.txt'
VERTEX = 6  # количество вершин в многограннике
EDGES = 12  # количество ребер в многограннике
FACES = 8  # количестов граней в многограннике
TIMES = 10000  # количество шагов по времени
list_faces = []  # список, который будет содержать все грани
with open(file_path) as fl_wth_fs:  # выгрузим из файла все номера вершин
    lines = fl_wth_fs.readlines()
for line in lines:  # все номера вершин загоним в списко файлов
    ns_vx = line.rstrip('\n').split('\t')  # получили только числа из каждой строки
    a = int(ns_vx[0])
    b = int(ns_vx[1])
    c = int(ns_vx[2])
    list_faces.append(Faces(a, b, c))
conformal_weights = np.zeros((VERTEX, TIMES), float)  # конформные веса в вершинах
gauss_curve = adjacency_matrix(list_faces, VERTEX)  # гауссова кривизна в вершинах многогранника
length_matrix = adjacency_matrix(list_faces, VERTEX)  # матрица смежности длин рёбер
for i in range(0, VERTEX):
    conformal_weights[i, 0] = 1
# заполним матрицу длин рёбер случайными наборами чисел
# for i in range(0, length_matrix.count_nonzero()):
#     row, col = length_matrix.nonzero()  # список все индексов в строке, которые
#     length_matrix[row[i], col[i]] = random.randrange(1, 10, 1) + 0.1*random.randrange(0, 9, 1)
# # print('hello')
caley_menger = None
while caley_menger != None:
    for i in range(0, length_matrix.count_nonzero()):
        row, col = length_matrix.nonzero()  # список все индексов в строке, которые
        length_matrix[row[i], col[i]] = random.randrange(1, 10, 1) + 0.1 * random.randrange(0, 9, 1)
    caley_menger = gauss_curve_calculate(length_matrix)
print(sum(gauss_curve_calculate(length_matrix)))
print(сayley_menger_determinant(length_matrix, VERTEX) )
# print(length_matrix, VERTEX)p
# print(length_matrix.toarray())
# print('len_matrix', len(length_matrix))
# print(caley_menger(length_matrix))
# for i in range(0, VERTEX):
#     for j in range(0, VERTEX):
#         print(length_matrix[i,j],  ' ')
#     print('\n')
