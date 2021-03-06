class Node():
    def __init__(self, state, parent, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.g = 0
        self.h = 0
        # self.action = action
    def is_goal(self):
        for pack in self.state:
            if len(pack) == 0:
                continue
            else:
                color = pack[0][-1:]
                value = pack[0][:-1]
                for i in range(1,len(pack)):
                    # if i == len(pack):
                    #     break
                    if (pack[i][:-1] < value or pack[i][-1:] != color):
                        return False
                    value = pack[i][:-1]
        return True

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
