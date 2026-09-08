class Solution:
    def deleteMiddle(self, head):
        if head.next is None:
            return None

        slow = head
        fast = head
        previous = None

        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = slow.next

        return head