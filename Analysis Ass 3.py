from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_cycles(self, node, visited, stack, parent, cycles):
        visited[node] = True
        stack.append(node)
    
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.print_cycles(neighbor, visited, stack, node, cycles)
            elif neighbor != parent and stack:
                cycle = []
                while stack and stack[-1] != neighbor:
                    cycle.append(stack.pop())
                cycle.append(neighbor)
                cycle.append(node)
                cycles.append(cycle)
    
        if stack:
            stack.pop()


    def find_cycles(self):
        visited = [False] * (max(self.graph, default=0) + 1)
        cycles = []
    
        def dfs_cycle(node, parent, current_cycle):
            visited[node] = True
            current_cycle.append(node)
    
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs_cycle(neighbor, node, current_cycle)
                elif neighbor != parent and neighbor in current_cycle:
                    cycle_start = current_cycle.index(neighbor)
                    cycle = current_cycle[cycle_start:]
                    cycles.append(cycle)
    
            current_cycle.pop()
    
        for node in self.graph:
            if not visited[node]:
                dfs_cycle(node, -1, [])
    
        # Filter out duplicate cycles
        unique_cycles = []
        for cycle in cycles:
            if cycle not in unique_cycles:
                unique_cycles.append(cycle)
    
        return unique_cycles




    def bfs(self, start_node, order='left'):
        visited = [False] * (max(self.graph) + 1)
        queue = deque([start_node])
        visited[start_node] = True

        while queue:
            current_node = queue.popleft()
            print(current_node, end=' ')

            neighbors = sorted(self.graph[current_node])
            if order == 'right':
                neighbors = reversed(neighbors)

            for neighbor in neighbors:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, node, visited, order='left'):
        visited[node] = True
        print(node, end=' ')

        neighbors = sorted(self.graph[node])
        if order == 'right':
            neighbors = reversed(neighbors)

        for neighbor in neighbors:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, order)

    def is_bipartite(self):
        colors = {}
        visited = set()

        for start_node in self.graph:
            if start_node not in visited:
                queue = deque([(start_node, 0)])

                while queue:
                    current_node, color = queue.popleft()

                    if current_node in visited:
                        continue

                    visited.add(current_node)

                    if current_node not in colors:
                        colors[current_node] = color

                    for neighbor in self.graph[current_node]:
                        if neighbor not in visited:
                            queue.append((neighbor, 1 - color))
                        elif colors[neighbor] == color:
                            return False

        return True

# Example Usage:
graph = Graph()
edges = [(1, 3), (1, 4), (2, 1), (2, 3), (3, 4), (4, 1), (4, 2)]

for edge in edges:
    graph.add_edge(*edge)

print("DFS:")
visited = [False] * (max(graph.graph) + 1)
graph.dfs(1, visited)
print("\nBFS (Left Order):")
graph.bfs(1, order='left')
print("\nBFS (Right Order):")
graph.bfs(1, order='right')

cycles = graph.find_cycles()
if cycles:
    print("\nCycles in the graph:")
    for cycle in cycles:
        print(' '.join(map(str, cycle)))

if graph.is_bipartite():
    print("\nThe graph is bipartite.")
else:
    print("\nThe graph is not bipartite.")

