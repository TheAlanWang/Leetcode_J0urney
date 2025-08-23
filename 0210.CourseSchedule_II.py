# 210.CourseSchedule_II
# https://leetcode.com/problems/course-schedule-ii/description/
# time complexity: O(V + E) | space complexity: O(V + E)

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        
        queue = deque()
        for idx, count in enumerate(in_degree):
            if count == 0:
                queue.append(idx)
        
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for nei in graph[course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return res if len(res) == numCourses else []