import Graph
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

list_of_nodes=[]
list_of_edges=[]
list_of_paths=[]



def generate_random_graph():
    global list_of_nodes
    for i in range(0, 30):  # 30 Random Points
        randX = random.randint(1, 102400)
        randY = random.randint(1, 102400)
        node1 = Graph.node(randX, randY)
        list_of_nodes.append(node1)
        print 'Node ' + str(i) + ' Has been added at ' + str(randX) + ',' + str(randY)
generate_random_graph()
print '============\n\nDistance between A and B = ', Graph.dist(list_of_nodes[0], list_of_nodes[1])
def traverse():
    global  list_of_nodes
    global  list_of_edges
    global list_of_paths
    x = range(0, 30)
    random.shuffle(x)
    plt.scatter(x, x)
    # plt.show()


    print 'Edge#\tCost'
    total_cost = 0;
    for i in range(0, 29):
        first_node = list_of_nodes[x[i]];
        second_node = list_of_nodes[x[i + 1]];

        cost = Graph.dist(first_node, second_node)
        total_cost += cost
        edge1 = Graph.edge(first_node, second_node, cost)

        list_of_edges.append(edge1)
        print str(i) + '\t\t' + str(edge1.cost)
    print 'total cost\t' + str(total_cost)
    path1 = Graph.path(list_of_edges, total_cost)
    list_of_paths.append(path1)

    list_of_nodes = []
    list_of_edges = []









