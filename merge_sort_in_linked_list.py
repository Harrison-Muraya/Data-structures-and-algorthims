# from . import linklist_reviws_linklist as linkedlist
# import linklist_reviws_linklist as linkedlist

from linklist_reviws_linklist import LinkedList

def merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # print(f"left: {left}")
    # print(f"right: {right}")

    
    return merge(left, right)

def split(linked_list):
    if linked_list == None or linked_list.head is None:
        left = linked_list
        right = None
        return left, right
    else:
        mid = linked_list.size()//2
        mid_node = linked_list.dataAtIndex(mid-1)
        # print(f"mid: {mid} Mid data: {mid_node.data}")
        left = linked_list
        right = LinkedList()
        right.head = mid_node.next_node
        mid_node.next_node = None
        return left, right

def merge(left, right):
    merged = LinkedList()

    # fake head
    merged.preappend(0)
    current = merged.head
    left_head = left.head
    right_head = right.head

    
    

h = LinkedList()
print(h.isEmpty())
print(h.search(90))
h.preappend(10)
h.preappend(30)
h.preappend(40)
h.preappend(150)
h.preappend(106)
h.append(890)
h.append(890)

# print(h)

merge_sort(h)
# print(f"Linked list test {LinkedList.size}")


