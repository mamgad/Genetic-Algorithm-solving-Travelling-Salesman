import math
import random
import copy
def crossover(path1,path2):


    rand1 = random.sample(range(30), 3)
    rand2 = copy.deepcopy(rand1)
    random.shuffle(rand2)

    #print rand1
    #print rand2
    temp_path1=copy.deepcopy(path1)
    temp_path2 =copy.deepcopy(path2)
    #print 'BEFORE'
    #print "path1"
    #temp_path1.dump()
    #print 'path2'
    #temp_path2.dump()
    #print "\n"
    for i in range (3):

        for j in range (0,len(path1.nodes)):
            if (path1.nodes[j].number==rand1[i]):
                node1_index=j
                break
        for k in range (0,len(path2.nodes)):
            if (path2.nodes[k].number==rand2[i]):
                node2_index=k
                break

        temp_path1.nodes[node1_index]=copy.deepcopy(path2.nodes[node2_index])
        temp_path2.nodes[node2_index]=copy.deepcopy(path1.nodes[node1_index])

        #print"swapping "+str(node1_index)+","+str(node2_index)
        path1.getCost()
        #print 'after'
        #print "path1"
        #temp_path1.dump()
        #print 'path2'
        #temp_path2.dump()
        #print "\n"

    return temp_path1,temp_path2


class node:
    def __init__(self, x_loc, y_loc,number):
        self.x=x_loc
        self.y=y_loc
        self.number=number
class edge:
    def __init__(self, first_node,second_node):
        self.a = first_node
        self.b = second_node
        self.cost=dist(first_node,second_node)
class path:
    def __init__(self, all_edges,total_cost):
        self.edges=all_edges
        self.cost=total_cost
        self.nodes=[]
        for i in range(0,len(self.edges)):
            self.nodes.append(self.edges[i].a)
        last_node =self.edges[len(self.edges)-1].b
        self.nodes.append(last_node)
    def dump(self):


        for i in range(len(self.nodes)):
            print str(i)+'\t'+str(self.nodes[i].number)
    def mutate(self):
        rand_i=random.randint(1,4)
        #print "rand_i is "+str(rand_i)
        for i in range (0,rand_i):
            rand1=random.randint(0,29)
            rand2=random.randint(0,29)
            #print "Swapping "+str(rand1)+" with "+str(rand2)
            #temp_node=self.nodes[rand1]; '''Swapping nodes (mutating)'''
            self.nodes[rand1],self.nodes[rand2] = self.nodes[rand2],self.nodes[rand1]
            #self.nodes[rand1]=self.nodes[rand2]
            #self.nodes[rand2]=temp_node
            self.getCost()

        return self
    def getCost(self):
        total_cost=0
        for i in range(0, len(self.nodes)-1):
            first_node = self.nodes[i];
            second_node = self.nodes[i + 1];

            ab_cost = dist(first_node, second_node)
            total_cost += ab_cost
        #print str(total_cost)+" TC"
        self.cost = total_cost
        return total_cost






def dist(node1,node2):
    x1=node1.x
    y1=node1.y
    x2=node2.x
    y2=node2.y

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

