import heapq

class SmallestInfiniteSet:

    def __init__(self):
        # 'current' tracks the smallest number that has NEVER been popped
        self.current = 1
        
        # 'min_heap' stores numbers that were popped and then added back
        self.min_heap = []
        
        # 'added_back_set' ensures we don't add duplicates to the min_heap
        self.added_back_set = set()

    def popSmallest(self):
        # If we have any numbers that were added back, they are guaranteed 
        # to be smaller than 'current'. We pop the smallest one from the heap.
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.added_back_set.remove(smallest)
            return smallest
        
        # Otherwise, the smallest number is just our 'current' counter.
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num):
        # We only care about adding the number back if it was actually popped 
        # (meaning num < self.current) AND if it isn't already in our heap.
        if num < self.current and num not in self.added_back_set:
            self.added_back_set.add(num)
            heapq.heappush(self.min_heap, num)