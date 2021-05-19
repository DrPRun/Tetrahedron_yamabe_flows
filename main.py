# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
import random

import scipy.sparse

from faces import Faces
from smeg_matrix import *

file_path = '/Users/ruslan/Code/GeometricalFlow/octahedron.txt'
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
for i in range(0, length_matrix.count_nonzero()):
    row, col = length_matrix.nonzero()  # список все индексов в строке, которые
    length_matrix[row[i], col[i]] = random.randrange(1, 10, 1) + 0.1*random.randrange(0, 9, 1)
# for j in range(0, gauss_curve.count_nonzero()):
#     row, col = gauss_curve.nonzero()
#     print(row[j], col[j], gauss_curve[row[j], col[j]])
# for i in range(0, VERTEX, 1):
#     for j in range(0, VERTEX, 1):
#         print(gauss_curve[i, j], end=' ')
#     print('\r')
# print(length_matrix)
# print(gauss_curve)
gauss_curve_calculate(length_matrix, VERTEX)
example_list = [(1,2),(2,3),(1,2)]
uniquexample = set(example_list)
print(uniquexample)