import Graph
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

list_of_nodes=[]
list_of_edges=[]
list_of_paths=[]

def first_generation():
    edges = range(0, 30), range(0, 30), 0
    random.shuffle(edges[0])
    random.shuffle(edges[1])
    print edges[0]
    print edges[1]


first_generation()



def generate_random_graph():
    for i in range(0, 30):  # 30 Random Points
        randX = random.randint(1, 102400)
        randY = random.randint(1, 102400)
        node1 = Graph.node(randX, randY)
        list_of_nodes.append(node1)
        print 'Node ' + str(i) + ' Has been added at ' + str(randX) + ',' + str(randY)
generate_random_graph()
print '============\n\nDistance between A and B = ', Graph.dist(list_of_nodes[0], list_of_nodes[1])

x=range(0,30)
random.shuffle(x)
plt.scatter(x,x)
#plt.show()


print 'Edge#\tCost'
total_cost=0;
for i in range(0, 29):
    first_node = list_of_nodes[x[i]];
    second_node=list_of_nodes[x[i+1]];

    cost= Graph.dist(first_node,second_node)
    total_cost+=cost
    edge1=Graph.edge(first_node,second_node,cost)

    list_of_edges.append(edge1)
    print str(i)+'\t\t'+str(edge1.cost)
print total_cost
list_of_paths.append(list_of_edges,total_cost)








