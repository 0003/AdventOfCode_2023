#wip
import heapq #need to learn about this
from math import inf 

class Djij():
    def __init__(self,coods,n,size):
        self.nodes = {(0,0) : 0} # (x,y) = values are ints
        self.coods = coods
        self.max_x = size[0]
        self.max_y = size[1]

        for x ,y in coods:
            self.nodes[(x,y)] = "#"

    def valid_move(self,x,y):
        if x < 0 or x > self.max_x or  y < 0 or y > self.max_y:
            return False
        elif self.nodes.get((x,y),"not a #") == "#": 
            return False
        else:
            return True
    
    def dprint(self):
        for y in range(self.max_y+1):
            for x in range(self.max_x+1):
                c = self.nodes.get((x,y),".")
                if isinstance(c,int):
                    c = c % 10
                print(f"{c}",end="")
            print("")

    def get_next_nodes(self,current_node):
        x, y = current_node[0], current_node[1]
        up = self.valid_move(x,y-1)
        right = self.valid_move(x+1,y)
        down = self.valid_move(x,y+1)
        left = self.valid_move(x-1,y)

        nodes_ = [up,right, down, left] #Truth condition
        possible_nodes = [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]

        next_nodes = [ _[1] for _ in list(zip(nodes_,possible_nodes)) if _[0] ]

        return next_nodes       

    def djik(self,x=0,y=0):
        visited = set() # (x,y)
        queue = [(x,y)]
        current_node = (x,y)
        while queue:
            next_nodes = []
            current_node_dist = self.nodes.setdefault(current_node,1)
            next_nodes.extend(self.get_next_nodes(current_node))

            for next_node in next_nodes:
                if next_node not in visited: #need to revisit this
                    queue.append(next_node)
                self.nodes[(next_node)] = min(self.nodes.get(next_node,inf),current_node_dist+1)

            current_node = queue.pop(0)
            visited.add(current_node)
            print(len(queue))

        print(f"{self.nodes[(self.max_x,self.max_y)] = }")
        return self.nodes[(self.max_x,self.max_y)]
            

def get_input(f):
    with open(f"2024/18/{f}") as fi:
        coods = []
        for line in fi.readlines():
            line = line.strip().split(',')
            coods.append(  (int(line[0]), int(line[1])) )
        return coods

def main(f,n,size=(6,6)):
    coods = get_input(f)[:n]
    print(coods)
    d = Djij(coods,n,size=size)
    d.dprint()
    d.djik()
    d.dprint()
    print(f"{d.nodes.get(size) = }")

    return
    

main('test.txt',12,(6,6))

#main('input.txt',1024, (70,70))

