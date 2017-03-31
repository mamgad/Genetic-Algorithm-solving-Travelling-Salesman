import Graph
import random
import copy
import time
import matplotlib.pyplot as plt
import matplotlib
start_time=time.time()
detection_time=start_time
time_list=[]
cost_list=[]
list_of_nodes = []
list_of_edges = []
list_of_paths = []
least_cost=0.0
xaxis=[]
yaxis=[]
best_path=None
r_map=None
crossover_mapping=None
generation_size=1000
number_of_selected_gens=400

def nodes_swap():
    global best_path
    global list_of_paths
    if (random.random()<0.05 and (best_path is not None)):
        print "Swapping"
        path = copy.deepcopy(best_path)
        iterations =len(best_path.nodes)
        for i in range (iterations):
            for j in range(iterations):
                path.nodes[i],path.nodes[j]=path.nodes[j],path.nodes[i]
                list_of_paths.append(path)
    print "lenth in swap is "+str(len(list_of_paths))
def crossover():
    global list_of_paths
    list_of_paths=list_of_paths[:number_of_selected_gens]#Select specific number of genes

    for j in range(0,(generation_size-number_of_selected_gens)/2):
        rand1 = random.randint(0, (len(list_of_paths)/3)-1)
        rand2 = random.randint(0, len(list_of_paths)-1)
        if (random.random()<1):
            #list_of_paths.append(Graph.crossover(list_of_paths[rand1], list_of_paths[rand2]))
            result=Graph.crossover(list_of_paths[rand1], list_of_paths[rand2])
            list_of_paths.append(result[0])
            list_of_paths.append(result[1])
            #print 'in'+str(len(list_of_paths))
        else:
            list_of_paths.append(list_of_paths[rand1])
            list_of_paths.append(list_of_paths[rand2])


def random_map():#CROSS OVER RATE !!
    global r_map
    global crossover_mapping
    r_map=random.sample(range(30), 8),random.sample(range(30), 8)
    #print r_map

    #print crossover_mapping
def generate_square():#for debugging
    global list_of_nodes
    global xaxis
    global yaxis
    for i in range (8):
        y=20000;
        x=20000+(70000/8)*i
        node1 = Graph.node(x, y, i)
        xaxis.append(x)
        yaxis.append(y)
        list_of_nodes.append(node1)
    for i in range (8,22,2):
        y=20000+((70000/12)*(i-8))
        x=20000
        node1 = Graph.node(x, y, i)
        xaxis.append(x)
        yaxis.append(y)
        list_of_nodes.append(node1)
        y = 20000+((70000/12)*(i-8))
        x = 90000
        node1 = Graph.node(x, y, i+1)
        xaxis.append(x)
        yaxis.append(y)
        list_of_nodes.append(node1)
    for i in range (22,30):
        y=90000;
        x=20000+(70000/8)*(i-22)
        node1 = Graph.node(x, y, i)
        xaxis.append(x)
        yaxis.append(y)
        list_of_nodes.append(node1)

def generate_random_graph():
    global list_of_nodes
    global xaxis
    global yaxis
    print "Node#\tX-axis\tY-axis"
    for i in range(0, 30):  # 30 Random Points
        randX = random.randint(1, 102400)
        randY = random.randint(1, 102400)
        node_number=i
        node1 = Graph.node(randX, randY,node_number)
        xaxis.append(randX)
        yaxis.append(randY)
        list_of_nodes.append(node1)

        print str(node_number) + '\t\t' + str(randX) + '\t' + str(randY)
def show_paths_costs():
    print "\n===================\nPATH#\tPATH COST"
    for i in range(0, len(list_of_paths)-1):
        print str(i)+'\t\t1 '+str(list_of_paths[i].cost)+'\t\t2 '+str(list_of_paths[i].getCost())+'\t' +str(list_of_paths[i].getCost()-list_of_paths[i].cost)
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


    list_of_edges = []



#generate_random_graph()
generate_square()
def mutate_generation():
    global list_of_paths
    global best_path
    global min_of_generation
    print "LEN IS "+str(len(list_of_paths))

    for i in range(10,len(list_of_paths)-11):
        #print len(list_of_paths)
        rand=random.random()
        if(rand<0.03):#20% Mutation Rate
            #print "mut"
            list_of_paths[i]=list_of_paths[i].mutate()#TEMPROAARY!!!



    #print ""+str(best_path.getCost())

def generate():
    for j in range(0, generation_size):  # Find 1000 Random path
        global list_of_paths
        global min_of_generation
        global best_path

        traverse()
        #sorted_pathes = sorted(list_of_paths, key=lambda x: x.cost, reverse=False)
        #min_of_generation = sorted_pathes[0]
        #print sorted_pathes[0].cost
        #if (best_path is None or best_path.cost > min_of_generation):
        #    best_path = min_of_generation  # UPDATE BEST PATH

        '''NEW GENERATION STARTS'''
        random_map()
    #print "Count is " + str(len(list_of_paths))

generate()


show_paths_costs()
plt.show()

loc_avg=0
for j in range(10000):



    plt.scatter(xaxis, yaxis)
    plt.pause(0.01)
    plt.clf()
    plt.subplot(5,1,(1,4))
    plt.plot(xaxis, yaxis)
    plt.subplot(5, 1, 5)
    plt.plot(time_list, cost_list)
    plt.subplot(5, 1, (1,4))
    sorted_pathes = sorted(list_of_paths, key=lambda x: x.cost, reverse=False)
    list_of_paths = sorted_pathes

    mutate_generation()
    #nodes_swap()
    crossover()
    plt.title("Length of Current Route " +str(least_cost)+ " at " + str(detection_time)+"\n"+str(time.time()-start_time))
    min_of_generation = sorted_pathes[0]
    if (best_path is None):
        best_path = min_of_generation


    print "Min is :"+str(best_path.getCost())
    for i in range(len(best_path.nodes)):
        xaxis[i]=best_path.nodes[i].x
        yaxis[i]=best_path.nodes[i].y



    localmin = min_of_generation.getCost()

    loc_avg=(loc_avg+localmin)
    print "len is "+str(len(list_of_paths))

    print "loc ="+str(localmin)+"loc_avg ="+str(loc_avg/(j+1))
    #globalmin = best_path.getCost()
    globalmin =best_path.cost
    if (globalmin > localmin):
        best_path = copy.deepcopy(min_of_generation)
        detection_time=time.time()-start_time
        time_list.append(detection_time)
        cost_list.append(best_path.cost)
        least_cost=best_path.cost


print "Xaxis\tYaxis"
for i in range(0,len(best_path.nodes) - 1):

    print str(best_path.nodes[i].x)+"\t"+str(best_path.nodes[i].y)
plt.show()
#list_of_paths[0].dump()
#print "return"
#print Graph.crossover(list_of_paths[0],list_of_paths[1]).dump()
#print "--"
#list_of_paths[0].dump()


