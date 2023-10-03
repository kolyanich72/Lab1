from typing import Union
import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
     # c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    pred, dist = nx.dijkstra_predecessor_and_distance(graph, 0)

    return dist[len(dist)-1]


def iter_f(stairway):
    n = len(stairway)
    if n == 1:
        return stairway[0]
    elif n == 2:
        return  min(stairway[0] + stairway[1], stairway[1])
    coast = []
    coast.append(stairway[0])
    coast.append(stairway[1])
    for i in range(2, n):
        coast.append(min(coast[i-1] + stairway[i], coast [i-2] + stairway[i]))
    return coast[-1]


def tree_creator(stairway):
    stairway_graph = nx.Graph()
    ebunch = []

    for i in range(1, len(stairway) + 1):
        if i == 1:
            ebunch.append((i - 1, i, stairway[i - 1])
        else:
            ebunch.append((i - 1, i, stairway[i - 1]))
            ebunch.append((i - 2, i, stairway[i - 1]))
    stairway_graph.add_weighted_edges_from(ebunch)
 #   print(ebunch)
    return  stairway_graph

if __name__ == '__main__':
    stairway = (1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3)  #(5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = tree_creator(stairway)


 #   print(stairway_graph.edges)

#    print(iter_f(stairway))

   #  записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
