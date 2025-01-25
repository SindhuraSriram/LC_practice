class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hashmap = {}
        for i in range(len(equations)):
            x, y = equations[i]
            if x not in hashmap:
                hashmap[x] = {}
            hashmap[x][y] = values[i]
            if y not in hashmap:
                hashmap[y] = {}
            hashmap[y][x] = 1 / values[i]
        
        def bfs(query):
            q = deque()
            visited = set()
            val = 1
            startVar, endVar = query
            q.append((startVar, val))
            while q:
                currentVar, currentVal = q.popleft()
                if currentVar not in hashmap:
                    return -1
                elif currentVar == endVar:
                    return currentVal
                else:
                    visited.add(currentVar)
                    for nextVar in hashmap[currentVar].keys():
                        if nextVar not in visited:
                            q.append((nextVar, currentVal * hashmap[currentVar][nextVar]))
            return -1
        
        output = []
        for query in queries:
            output.append(bfs(query))
        return output
        