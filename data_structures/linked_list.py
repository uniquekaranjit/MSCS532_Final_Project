"""
Module for LinkedList implementation and operations.

This module provides a basic singly linked list implementation
and related utility functions for performance testing.
"""

class Node:
    """A node in a singly linked list."""
    
    def __init__(self, value: int) -> None:
        """
        Initialize a new node.

        Args:
            value (int): The value to store in the node.
        """
        self.value = value
        self.next = None

def create_linked_list(size: int) -> Node:
    """
    Create a linked list of specified size.

    Args:
        size (int): Number of nodes to create.

    Returns:
        Node: Head of the created linked list.

    Raises:
        ValueError: If size is negative.
    """
    if size < 0:
        raise ValueError("Size cannot be negative")
        
    head = Node(0)
    curr = head
    for i in range(1, size):
        curr.next = Node(i)
        curr = curr.next
    return head

def traverse_and_sum_linked_list(head: Node) -> int:
    """
    Traverse the linked list and sum all values.

    Args:
        head (Node): Head of the linked list.

    Returns:
        int: Sum of all values in the linked list.
    """
    total = 0
    curr = head
    while curr:
        total += curr.value
        curr = curr.next
    return total 