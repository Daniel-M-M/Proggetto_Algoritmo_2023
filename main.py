import networkx as nx
import numpy as np
# from collections import deque


# Function per verifier se il graph è directed o no
def is_transpose(adia_matrix):
    matrix_temp = np.array(adia_matrix)
    matrix_trans = matrix_temp.transpose()
    if np.array_equiv(matrix_temp, matrix_trans):
        return True
    else:
        return False


# Function generate un graph da una matrices
def create_graph(my_matrix):
    if is_transpose(my_matrix):
        my_graph = nx.Graph(my_matrix)
        to_string(True)
    else:
        my_graph = nx.DiGraph(my_matrix)
        to_string(False)
    return my_graph


# Function per la ricerca di nodo BFV
def bfv(my_graph, my_node):
    visited = set()
    parents = [dict(my_graph[my_node])]

    while parents:
        if my_node not in visited:
            visited.add(my_node)
        for element in parents:
            for i in element:
                if i not in visited:
                    visited.add(i)
                    parents.append((my_graph[i]))
        parents.clear()
    return visited


def to_string(var):
    if var:
        print("Il graph non è orientate")
    else:
        print("Il graph è orientate")


if __name__ == '__main__':
    # Salvo in una variable la lecture da un file CSV
    myMatrix_nonOriented = np.loadtxt("graph1_not_directed_test.csv", delimiter=";")
    myMatrix_Oriented = np.loadtxt("graph2_directed_test.csv", delimiter=";")
    myMatrix_Oriented2 = np.loadtxt("graph3_directed_test.csv", delimiter=";")

    # Verifier se il graph è directed o non
    graph1 = create_graph(myMatrix_nonOriented)
    graph2 = create_graph(myMatrix_Oriented)
    graph3 = create_graph(myMatrix_Oriented2)

    # stamp i nodo ed i edge del graph
    print("BFV in graph2: ", bfv(graph2, 0))
    print("BFV in graph3: ", bfv(graph3, 0))
