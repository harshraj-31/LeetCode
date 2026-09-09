class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            # Temporarily store the next node
            next_node = current.next
            
            # Reverse the current node's pointer
            current.next = prev
            
            # Move the pointers one step forward
            prev = current
            current = next_node

        # prev will be the new head at the end
        return prev