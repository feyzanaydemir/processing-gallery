from Branch import *
from Leaf import *

class Tree(object):
    def __init__(self, leaf_count, max_distance):
        self.leaves = []
        self.branches = []
        
        for i in range(leaf_count):
            self.leaves.append(Leaf())
            
        # root branch is pointing directly up
        root_direction = PVector(0, -1)
        root_position = PVector(0, 0, 0)
        root = Branch(root_direction, root_position, None)
        self.branches.append(root)
        
        current_branch = root
        is_in_range = False
        
        for leaf in self.leaves:
            distance = PVector.dist(current_branch.position, leaf.position)
                
            if distance < max_distance:
                is_in_range = True
                break
            
        if not is_in_range:
            current_branch = current_branch.get_next()
            self.branches.append(current_branch)
    
    
    def show(self):
        for i, branch in enumerate(self.branches):
            val = map(i, 0, len(self.branches), 4, 0)
            strokeWeight(val)
            branch.show()
        
        for leaf in self.leaves:
            leaf.show()
    
    
    def grow(self, max_distance, min_distance):
        # find the closest branch to this leaf
        for leaf in self.leaves:
            closest_branch = None
            record_distance = max_distance
            
            for branch in self.branches:
                distance = PVector.dist(leaf.position, branch.position)
                
                # this branch is too close to leaf
                # stop searching for the closest branch to this leaf and go to the next leaf
                if distance < min_distance:
                    leaf.reached = True
                    closest_branch = None
                    break
                
                # update the currentBranch if distance is in range
                if distance < record_distance:
                    closest_branch = branch
                    record_distance = distance
                    
            # if a valid closestBranch exists
            if closest_branch:
                closest_branch.count += 1
                
                # update its direction vector to achieve the pull effect on drawing process
                new_direction = PVector.sub(leaf.position, closest_branch.position).normalize()
                closest_branch.direction.add(new_direction)
                
        # delete the reached leaves from the list
        self.leaves[:] = [leaf for leaf in self.leaves if not leaf.reached]
                
        for i in range(len(self.branches) - 1, -1, -1):
            # if this branch was connected to at least 1 leaf
            if self.branches[i].count > 0:
                # average the direction vector because this branch was added to itself "count" times
                self.branches[i].direction.div(self.branches[i].count + 1)
                self.branches.append(self.branches[i].get_next())
            
            self.branches[i].reset()
                
