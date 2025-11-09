from collections import deque

def assign_good_and_evil(graph):
    color = {}

    def bfs(start):
        color[start] = True
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph.neighbors(u):
                if v not in color:
                    color[v] = not color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
        return True

    for node in graph.nodes:
        if node not in color:
            if not bfs(node):
                return None

    return {node: ('good' if color[node] else 'evil') for node in color}