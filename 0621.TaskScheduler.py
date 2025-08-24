# 0621.Task_Scheduler
# https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [] 
        for cnt in count.values():
            heapq.heappush(maxheap, -cnt)
        
        queue = deque()
        time = 0
        while maxheap or queue:
            time += 1
            
            if maxheap:
                cnt = heapq.heappop(maxheap) + 1
                if cnt != 0:       # add back to queue if there are still remaining tasks
                    queue.append((cnt, time + n))

            if queue and queue[0][1] == time:
                cnt, runtime = queue.popleft()
                heapq.heappush(maxheap, cnt)

        return time 