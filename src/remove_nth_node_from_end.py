from linked_list_node import LinkedListNode
from linked_list import LinkedList


def remove_nth_node_from_end(head, n):
    size = 1
    iterator = head
    while iterator.next is not None:
        size = size + 1
        iterator = iterator.next

    index = size - n
    print("index", index)
    if index == 0:
        return head.next

    index = index - 1  # reach the previous node
    prev_node = head
    while index >= 0:
        index = index - 1
        prev_node = prev_node.next

    if prev_node is not None:
        target_node = prev_node.next
        target_next = target_node.next
        prev_node.next = target_next

    return head


if __name__ == "__main__":
    node_values = [69, 8, 49, 106, 116, 112]
    input_list = LinkedList()
    input_list.create_linked_list(node_values)
    new_head = remove_nth_node_from_end(input_list.head, 6)
    print(input_list.__str__())
