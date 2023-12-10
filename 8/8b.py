"""--- Day 8: Haunted Wasteland ---"""
#works
import re
import math
import copy

#methods to find solution
class Solution:
    def __init__(self):
        pass
        self.d = None # set during Main()
        self.cycle_length = None #set during Main()
        self.nodes = None #added during main
        self.a_nodes = None # appended during Main()

    def get_steps_to_z(node_obj):
        a = copy.deepcopy(node_obj)
        step = 0
        for d in Solution.cycle_1d(Solution.d):
            if a.name[-1] == "Z":
                raise Exception("this is caught at wrong time ")
            step +=1
            a = a.get_next(d)
            if a.name[-1] == "Z":
                print(f"{node_obj.name} found it's exist at {a.name} it's step {step}")
                return step
            else:
                pass
        return #won't hit

    def get_solution():
        #returns dict of {visited_node:step}p
        steps_to_z_list = []

        for a in Solution.a_nodes:
            steps_to_z_list.append(Solution.get_steps_to_z(a))
        lcm = steps_to_z_list[0]

        for n in steps_to_z_list[1:]:
            lcm = lcm * n // math.gcd(lcm, n)
        print(f'The lcm step is {lcm} of the exit point leg')

        return lcm

    def cycle_1d(s,step=0):
        while True:
            old = s
            s =  s[1:] + s[:1]
            yield old[0] #yielding old because next time it is called will be post ecm

class Node:
    def __init__(self,n,l,r):
        self.name = n
        self.left = l
        self.right = r
    
    def get_next(self,d):
        cursor = Solution.nodes[self.name]
        if d == "L":
            return   Solution.nodes[self.left]
        else:
            return  Solution.nodes[self.right]

def get_input(fi):
    with open(fi) as f:
        return f.readlines()

def main(fi):
    print(f'{fi}')
    inp = get_input(fi)
    directions = inp[0].strip()
    Solution.d = directions # store this in the class object for memory footprint
    Solution.cycle_length = len(Solution.d) #store this in the class object for memory footprint
    a_nodes_ = []
    nodes = {}
    for i,e in enumerate(inp[2:]):
        n_p = re.compile(r'([1-9]{2}[A-Z]|[A-Z]{3})') #so test case works
        n,l,r = n_p.findall(e)
        if n[-1] == "A":
            a_nodes_.append(Node(n,l,r))
        nodes[n] = Node(n,l,r)
    Solution.a_nodes = a_nodes_
    Solution.nodes = nodes
    
    print(Solution.get_solution())
    return 
    

#main('8/test.txt')
#main('8/test2.txt')
#main('8/test3.txt')
main('8/input.txt')

"""for a in Solution.cycle_1d("12345"):
    print(a)"""