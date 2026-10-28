class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        minimum spannig tree
        '''
        n = len(points)
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        visited = set() # index

        result = 0

        for _ in range(n):
            node = -1
            curr_min_dist = float('inf')

            for current_node in range(n):
                if current_node not in visited and min_dist[current_node] < curr_min_dist:
                    node = current_node
                    curr_min_dist = min_dist[current_node]

            result += curr_min_dist
            visited.add(node)

            for next_node in range(n):
                if next_node not in visited:
                    dist = abs(points[node][0] - points[next_node][0]) + abs(points[node][1] - points[next_node][1])
                    if dist < min_dist[next_node]:
                        min_dist[next_node] = dist

        return result


        

        



        
        