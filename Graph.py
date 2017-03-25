import math
class node:
    def __init__(self, x_loc, y_loc):
        self.x=x_loc
        self.y=y_loc
class edge:
    def __init__(self, first_node,second_node ,edge_cost):
        self.a = first_node
        self.b = second_node
        self.cost=edge_cost
class path:
    def __init__(self, all_edges,total_cost):
        self.edges=all_edges
        self.cost=total_cost




def dist(node1,node2):
    x1=node1.x
    y1=node1.y
    x2=node2.x
    y2=node2.y

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

