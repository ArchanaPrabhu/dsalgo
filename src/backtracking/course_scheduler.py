class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = { c : [] for c in range(numCourses)}

        # let us represent the courses in adj list format
        for a, b in prerequisites:
            adj_list[a].append(b)
        # print(adj_list)
        visited = set()

        def dfs(course):
            # print("dfs start", course, visited, course in visited)
            if course in visited:
                # print("False")
                return False

            if len(adj_list[course]) == 0:
                # print("True")
                return True

            visited.add(course)
            for c in adj_list[course]:
                if not dfs(c): 
                    # print("False")
                    return False
            visited.remove(course)
            # this means that we can prevent further traversals 
            # by marking possible paths as [] so that we hit the base case sooner
            adj_list[course] = [] 
            return True

        for course in range(numCourses):
            # print("initial", course)
            # visited = set()
            if not dfs(course):
                return False
        
        return True
        

# 1 -> 0 
# 2 -> 6
# 1 -> 7
# 6 -> 4
# 7 -> 0
# 0 -> 5


