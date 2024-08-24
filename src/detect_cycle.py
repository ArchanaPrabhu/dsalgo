from linked_list import LinkedList


def detect_cycle(head):
    fast_ptr = head
    slow_ptr = head

    while fast_ptr.next and fast_ptr.next.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            return True
    return False

if __name__ == "__main__":
    head = None
    detect_cycle(head)