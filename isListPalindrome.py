class ListNode:
  def __init__(self,value):
    self.val = value
    self.next = None


def print_node(head):
    curr = head
    while curr is not None:
        print(curr.val, end="->")
        curr = curr.next

def isPalindrome(head):
        slow_curr = head
        fast_curr = head
        stack = []
        count = 0
        
        while fast_curr and fast_curr.next:
            stack.append(slow_curr.val)
            slow_curr = slow_curr.next
            fast_curr = fast_curr.next.next

    # if the linked list is odd, curr_fast will be None, or else not None. If its odd, we advance
    # iterator one more node   
        if fast_curr:
            slow_curr = slow_curr.next
            
        # while slow_curr:
        #     if len(stack) == 0:
        #         return True
        #     ele = stack.pop()
        #     if ele == slow_curr.val:
        #         slow_curr = slow_curr.next
        #     else:
        #         return False
        
        while stack:    # This implementation is better
            val = stack.pop()
            print (val, slow_curr.val)
            if val != slow_curr.val:
                return False
            slow_curr = slow_curr.next

        return True


f1 = ListNode(2)
f2 = ListNode(3)
f3 = ListNode(1)
f4 = ListNode(4)
f5 = ListNode(1)
f6 = ListNode(3)
f7 = ListNode(2)
f1.next = f2
f2.next = f3
f3.next = f4
f4.next = f5
f5.next = f6
f6.next = f7

print_node(f1)
print()
print(isPalindrome(f1))
