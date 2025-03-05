def reverse_queue(q):
    stack=[]
    while q:
        stack.append(q.pop(0))
    while stack:
        q.append(stack.pop(0))
queue=[10,20,30,40]
reverse_queue(queue)
print(queue)
import heapq
pq=[]
heapq.heappush(pq,(1,"task1"))
heapq.heappush(pq,(3,"task3"))
heapq.heappush(pq,(2,"task2"))
print("Processing:",heapq.heappop(pq))
print("Processing:",heapq.heappop(pq))
print("Processing:",heapq.heappop(pq))