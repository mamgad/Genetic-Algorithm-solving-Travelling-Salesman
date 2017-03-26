import Graph
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

list_of_nodes = []
list_of_edges = []
list_of_paths = []
new_gen_paths = []
best_path=None
r_map=None
crossover_mapping=None

def crossover():
    for i in range(0,20):
        list_of_paths[crossover_mapping[0]].edges
def random_map():#CROSS OVER RATE !!
    global r_map
    global crossover_mapping
    r_map=random.sample(range(30), 8),random.sample(range(30), 8)
    #print r_map
    crossover_mapping=random.sample(range(100), 20),random.sample(range(100), 20)
    #print crossover_mapping
def generate_random_graph():
    global list_of_nodes
    print "Node#\tX-axis\tY-axis"
    for i in range(0, 30):  # 30 Random Points
        randX = random.randint(1, 102400)
        randY = random.randint(1, 102400)
        node_number=i
        node1 = Graph.node(randX, randY,node_number)
        list_of_nodes.append(node1)

        print str(node_number) + '\t\t' + str(randX) + '\t' + str(randY)
def show_paths_costs():
    print "\n===================\nPATH#\tPATH COST"
    for i in range(0, 100):
        print str(i)+'\t\t'+str(sorted_pathes[i].cost)
    print "\n==================="
def traverse():
    global list_of_nodes
    global list_of_edges
    global list_of_paths
    x = range(0, 30)
    random.shuffle(x)
    #plt.scatter(x, x)
    # plt.show()


    #print 'Edge#\tCost'
    total_cost = 0;
    i=0
    for i in range(0, 29):
        first_node = list_of_nodes[x[i]];
        second_node = list_of_nodes[x[i + 1]];

        cost = Graph.dist(first_node, second_node)
        total_cost += cost
        edge1 = Graph.edge(first_node, second_node)

        list_of_edges.append(edge1)
        #print str(i) + '\t\t' + str(edge1.cost)
    #print 'total cost\t' + str(total_cost)

    path1 = Graph.path(list_of_edges, total_cost)
    list_of_paths.append(path1)
    print "Test\t"+str(path1.cost)+'\t'+str(path1.getCost())

    list_of_edges = []



generate_random_graph()
def mutate_generation():
    for i in range(0,len(list_of_paths)):
        if(random.random<0.2):#20% Mutation Rate
            list_of_paths[i].mutate()

def generate():
    for j in range(0, 100):  # Find 100 Random path
        global list_of_paths
        global min_of_generation
        global best_path

        traverse()
        sorted_pathes = sorted(list_of_paths, key=lambda x: x.cost, reverse=False)
        min_of_generation = sorted_pathes[0]
        print sorted_pathes[0].cost
        if (best_path is None or best_path.cost > min_of_generation):
            best_path = min_of_generation  # UPDATE BEST PATH

        '''NEW GENERATION STARTS'''
        random_map()
    print "Count is " + str(len(list_of_paths))

generate()
list_of_paths[0].dump()
print "Mutation Test"
list_of_paths[0].mutate()
list_of_paths[0].dump()
show_paths_costs()