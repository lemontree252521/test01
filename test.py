from collections import deque

graph = [

#   1 2 3 4 5 6 7

    [0,1,1,0,0,0,0],  # 节点1
    [1,0,0,1,1,0,0],  # 节点2
    [1,0,0,0,0,1,1],  # 节点3
    [0,1,0,0,0,0,0],  # 节点4
    [0,1,0,0,0,0,0],  # 节点5
    [0,0,1,0,0,0,0],  # 节点6
    [0,0,1,0,0,0,0]   # 节点7
]


class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Treenode(1)


def bfs(graph, start=root):
    n = len(graph)
    visited = [False] * n
    





bfs(graph, start=0)