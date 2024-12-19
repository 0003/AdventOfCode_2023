#works
import heapq 
from math import inf 

class Djij():
    def __init__(self,coods,n,size,i):
        self.nodes = {(0,0) : 0} # (x,y) = values are ints
        self.coods = coods[:i+1]
        self.max_x = size[0]
        self.max_y = size[1]
        self.i = i

        for x ,y in self.coods:
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

    def djik(self,i,x=0,y=0):
        coods = self.coods
        #print(f"Djik {i = } and {coods = }")
        visited = set() # (x,y)
        queue = [ (0, (x,y)) ]
        while queue:
            current_node_dist, current_node = heapq.heappop(queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            next_nodes =  self.get_next_nodes(current_node)
            for next_node in next_nodes:
                if next_node not in visited: 
                    next_dist =  current_node_dist + 1
                    if next_dist < self.nodes.get(next_node,inf):
                        self.nodes[next_node] = next_dist
                        heapq.heappush(queue, (next_dist, next_node))
                        #self.dprint()
                        #print(" ")
        #print(f"{i = } {coods[-1]}")     
        if (self.max_x,self.max_y) in self.nodes.keys():
            if self.nodes[(self.max_x,self.max_y)] != "#":
                return True
            else: 
                return False
        return False
            

def get_input(f):
    with open(f"2024/18/{f}") as fi:
        coods = []
        for line in fi.readlines():
            line = line.strip().split(',')
            coods.append(  (int(line[0]), int(line[1])) )
        return coods

def main(f,size):
    coods = get_input(f)
    for i, cood in enumerate(coods):
        d = Djij(coods,len(coods),size,i)
        res = d.djik(i)
        if res == False:
            print(f"Final {i = }{cood = }")
            break
    return
    

#main('test.txt',(6,6))

main('input.txt', (70,70))

