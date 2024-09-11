from my_list_node import MyListNode


class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    # The following methods have to be implemented.

    def get_value(self, index: int) -> int:
        """Return the value (elem) at position 'index' without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            (int): Retrieved value.

        Raises:
            ValueError: If the passed index is not an int or out of range.
        """
        if not isinstance(index, int) or not (0 <= index < self._size):
            raise ValueError(f"Invalid index: index should be an integer in the range of 0 to {self._size}.")

        curr_node = self._head

        for _ in range(index):
            curr_node = curr_node.next_node

        return curr_node.elem

    def search_value(self, val: int) -> int:
        """Return the index of the first occurrence of 'val' in the list.

        Args:
            val (int): Value to be searched.

        Returns:
            (int): Retrieved index.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("The value must be an integer.")

        curr_node = self._head
        index = 0

        while curr_node:
            if curr_node.elem == val:
                return index
            curr_node = curr_node.next_node
            index += 1

        return -1

    def insert(self, val: int) -> None:
        """Add a new node containing 'val' to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("val is not an integer")

        new_node = MyListNode(val)

        if self._size == 0:  # Empty list
            self._head = self._tail = new_node
        elif val < self._head.elem:  # Insert at the head
            new_node.next_node = self._head
            self._head.prev_node = new_node
            self._head = new_node
        elif self._tail.elem < val:  # Insert at the tail
            new_node.prev_node = self._tail
            self._tail.next_node = new_node
            self._tail = new_node
        else:  # Insert in the middle
            curr_node = self._head
            while curr_node and curr_node.elem < val:
                curr_node = curr_node.next_node
            new_node.next_node = curr_node
            new_node.prev_node = curr_node.prev_node
            curr_node.prev_node.next_node = new_node
            curr_node.prev_node = new_node

        self._size += 1

    def remove_first(self, val: int) -> bool:
        """Remove the first occurrence of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether an element was successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("The value must be an integer.")

        curr_node = self._head

        while curr_node:
            if curr_node.elem == val:
                if curr_node == self._head:  # Removing the head
                    self._head = curr_node.next_node
                    self._head.prev_node = None
                elif curr_node == self._tail:  # Removing the tail
                    self._tail = curr_node.prev_node
                    self._tail.next_node = None
                else:  # Removing from the middle
                    curr_node.prev_node.next_node = curr_node.next_node
                    curr_node.next_node.prev_node = curr_node.prev_node
                self._size -= 1
                return True
            curr_node = curr_node.next_node

        return False

    def remove_all(self, val: int) -> bool:
        """Remove all occurrences of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether elements were successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("The value must be an integer.")

        removed = False
        curr_node = self._head
        prev_node = None

        while curr_node:
            if curr_node.elem == val:
                if prev_node:
                    prev_node.next_node = curr_node.next_node
                else:
                    self._head = curr_node.next_node
                self._size -= 1
                removed = True
            else:
                prev_node = curr_node
            curr_node = curr_node.next_node

        return removed

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        seen = set()
        curr_node = self._head
        prev_node = None

        while curr_node:
            if curr_node.elem in seen:
                prev_node.next_node = curr_node.next_node
                self._size -= 1
            else:
                seen.add(curr_node.elem)
                prev_node = curr_node
            curr_node = curr_node.next_node

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the 'n' highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            ValueError: If the passed value n is not an int or out of range.
        """
        if not isinstance(n, int) or not (0 < n <= self._size):
            raise ValueError(f"Invalid value: 'n' should be an integer in the range of 1 to {self._size}.")

        curr_node = self._head
        cutoff_index = self._size - n
        index = 0

        while curr_node and index < cutoff_index:
            self._head = curr_node.next_node
            curr_node = self._head
            self._size -= 1
            index += 1

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        curr_node = self._head

        while curr_node:
            if curr_node.elem % 2 == 0:
                if curr_node == self._head:  # Removing the even head node
                    self._head = curr_node.next_node
                    if self._head:
                        self._head.prev_node = None
                elif curr_node == self._tail:  # Removing the even tail node
                    self._tail = curr_node.prev_node
                    if self._tail:
                        self._tail.next_node = None
                else:  # Removing an even node from the middle
                    curr_node.next_node.prev_node = curr_node.prev_node
                    curr_node.prev_node.next_node = curr_node.next_node
                self._size -= 1
            curr_node = curr_node.next_node

    def filter_even(self) -> None:
        """Filter the list to only contain even values."""
        curr_node = self._head

        while curr_node:
            if curr_node.elem % 2 != 0:
                if curr_node == self._head:  # Removing the odd head node
                    self._head = curr_node.next_node
                    if self._head:
                        self._head.prev_node = None
                elif curr_node == self._tail:  # Removing the odd tail node
                    self._tail = curr_node.prev_node
                    if self._tail:
                        self._tail.next_node = None
                else:  # Removing an odd node from the middle
                    curr_node.next_node.prev_node = curr_node.prev_node
                    curr_node.prev_node.next_node = curr_node.next_node
                self._size -= 1
            curr_node = curr_node.next_node
