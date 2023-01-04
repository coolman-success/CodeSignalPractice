class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        # this problem is equal to checking if there is an Eulerian path
        # in the graph made from edges with vertices which are the first
        # and the last characters of each name of team players
        degree, visited, adjc = {}, {}, {}
        for name in self.names:
            s, e = name[0].upper(), name[-1].upper()
            
            # calculate degrees (indegree - outdegree) of each node
            degree[s] = degree[s] + 1 if s in visited else 1
            degree[e] = degree[e] - 1 if e in visited else -1
            
            # this list will be used to check the connectivity of vertices
            visited[s] = False
            visited[e] = False
            # make adjacent node list to check connectivity later
            adjc[s] = adjc[s] + [e] if s in adjc else [e]
            adjc[e] = adjc[e] + [s] if e in adjc else [s]

        # at most one vertex can degree of 1 or -1
        if sum(degree[v] == 1 for v in degree) > 1 or sum(degree[v] == -1 for v in degree) > 1:
            return False
        # all remaining vertices should have degree of 0
        if any(abs(degree[v])>1 for v in degree):
            return False
        
        # check the connectivity of graph
        stack = [self.names[0][0].upper()]
        visited[stack[0]] = True
        while len(stack):
            v = stack.pop()
            for w in adjc[v]:
                if not visited[w]:
                    stack.append(w)
                    visited[w] = True
        
        return all(visited[v] for v in visited)

def solution(team):
    return bool(Team(team))
