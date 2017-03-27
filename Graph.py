import math
import random
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
        rand_i=random.randint(0,10)
        #print "rand_i is "+str(rand_i)
        for i in range (0,rand_i):
            rand1=random.randint(0,29)
            rand2=random.randint(0,29)
            #print "Swapping "+str(rand1)+" with "+str(rand2)
            temp_node=self.nodes[rand1]; '''Swapping nodes (mutating)'''
            self.nodes[rand1]=self.nodes[rand2]
            self.nodes[rand2]=temp_node
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

