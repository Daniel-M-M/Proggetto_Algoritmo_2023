import networkx as nx
import numpy as np


# Funzione per verificare se il grafo è orientato o no
def is_transpose(adia_matrix):
    matrix_temp = np.array(adia_matrix)
    matrix_trans = matrix_temp.transpose()
    if np.array_equiv(matrix_temp, matrix_trans):
        return True
    else:
        return False


# Funzione per creare un grafo da una matrice
def create_graph(my_matrix):
    if is_transpose(my_matrix):
        my_graph = nx.Graph(my_matrix)
    else:
        my_graph = nx.DiGraph(my_matrix)
    return my_graph


if __name__ == '__main__':
    '''Salvo in una varriabile la letture da un file CSV'''
    myMatrix_nonOriented = np.loadtxt("graph1_directed_test2.CSV", delimiter=";")

    '''Verifico se il grafo è orientato o non'''
    if is_transpose(myMatrix_nonOriented):
        print("Il grafo non è orientato")
    else:
        print("Il grafo è orientato")

    print('Nodos: ', create_graph(myMatrix_nonOriented).nodes(), 'Edges: ', create_graph(myMatrix_nonOriented).edges())

    '''solo per confermare...'''
    print(create_graph(myMatrix_nonOriented).is_directed())
