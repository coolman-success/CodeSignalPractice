class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        # # Bruteforce: low efficiency
        # from itertools import permutations
        # for p in permutations(self.names, len(self.names)):
        #     print(p)
        #     check = any([p[i][0].upper() != p[i - 1][-1].upper() for i in range(1, len(p))])
        #     if not check:
        #         return True
        # return False
        
        n = len(self.names)
        edges = []
        degree, visited, adjc = {}, {}, {}
        for name in self.names:
            s, e = name[0].upper(), name[-1].upper()
            edges.append((s, e))
            degree[s] = degree[s] + 1 if s in visited else 1
            degree[e] = degree[e] - 1 if e in visited else -1
            visited[s] = False
            visited[e] = False
            adjc[s] = adjc[s] + [e] if s in adjc else [e]
            adjc[e] = adjc[e] + [s] if e in adjc else [s]
        
        if any(abs(degree[v])>1 for v in degree):
            return False
        if sum(degree[v] == 1 for v in degree) > 1 or sum(degree[v] == -1 for v in degree) > 1:
            return False
        
        stack = [edges[0][0]]
        visited[edges[0][0]] = True
        while len(stack):
            v = stack.pop()
            for w in adjc[v]:
                if not visited[w]:
                    stack.append(w)
                    visited[w] = True
        
        return all(visited[v] for v in visited)

def solution(team):
    return bool(Team(team))
