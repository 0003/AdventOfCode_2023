from collections import deque


arrowkeypad = {
            "A" : [ "^", ">"],
            "^" : [ "V", "A"],
            "V" : [ "<", ">"],
            "<" : [ "V",],
            ">" : ["A", "V"]
            }

class Robot():

    def __init__(self,pad : dict,target_pad : dict,initial_key = "A"):
        self.pad = pad
        self.current_key = initial_key
        self.log =  []
        self.target_pad = target_pad

    def find_path(self,start, end):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            # Check if we reached the target
            if current == end:
                return path

            # Explore neighbors
            for neighbor in self.pad.get(current, []):
                queue.append((neighbor, path + [neighbor]))
        #should not happen
        return