

class Solution:
    def remainingMethods(self, n, k, invocations):
        # Step 1: Build the graph of method calls
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Step 2: Use DFS to find all suspicious methods starting from k
        suspicious = {k}
        stack = [k]

        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)

        # Step 3: Check if any normal (non-suspicious) method calls a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # If an outside method invokes a suspicious method, no methods can be removed
                return list(range(n))

        # Step 4: Otherwise, return all methods that are not suspicious
        return [i for i in range(n) if i not in suspicious]