# Data Structures and Algorithms

# Arrays (Lists in python)

# my_list = [1,2,3,4]
# append (add at back)
# my_list.append(10)
# print(my_list) 

# pop (remove an item)
# item = my_list.pop()
# print(my_list, item)

# pop for a specific position like pop(0) will pop from front 
# my_list.pop(0)
# print(my_list)

# insert at position
# my_list.insert(2,5)
# print(my_list)


# ID of variable (address)
# num = 12
# print(id(num))

# stacks

# from collections import deque
# from queue import LifoQueue, Queue

# q = Queue(maxsize = 3)
# stack = deque()
# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.appendleft('z')
# stack.pop() 
# stack.popleft() 

# print(stack)

# s = [1,2,2,3,4]
# s.remove(2)
# print(s)

# custom comparators 

# from functools import cmp_to_key

# def cmp(a, b):
#     if a[0] < b[0]:
#         return True
#     elif a[0] == b[0] and a[1] < b[1]:
#         return False
#     elif a[0] == b[0] and a[1] > b[1]:
#         return True
#     else:
#         return False
    

# l = [[1,4], [1,3], [2,6], [2, 4]]
# ll = sorted(l, key=cmp_to_key(cmp))
# print(ll)

# heaps 

# import heapq
# l = [5, 7, 9, 1, 3]
# heapq.heapify(l) # for min heap
# heapq._heapify_max(l) # for max heap
# print(heapq.heappop(l))
# print(len(l))

# Arrays 

# use enumerate for fetching index along with values 

# l = [1,2,3,4]
# for index, val in enumerate(l):
#     print(index, val)
# l.count(1) count no of 1s

# map(function, list(iterable)) return map object use list() to convert into list
# filter(function, list(iterable)) return filter object

# Sets 
# s = set()
# s.add(1)
# s.remove(1)
# s.union(s)
# s.intersection(s)

# from itertools import groupby # forms groups for contiguos keys
# from collections import Counter

# sum all ele in list 
# sum(l)

# l.copy() 
# l.extend([num]) add all items in second list 

# Graphs

# directed graphs 

# for directed graphs, we have to use recursion stack to find a cycle
# another form is topological sort in which we calculate the indegrees
# topological sorting helps us to detect cycles in directed graphs









