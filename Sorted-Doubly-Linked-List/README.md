This is the implementation of a Sorted Doubly Linked List data structure that implements the List ADT (Abstract Data Type).

Each node holds a single value of type `int` and references to the next and previous nodes. The list sorts its elements in ascending order.

Used functions:
- `get_value(self, index)`: Returns the value of the element at specific list index position (0 ≤ index < size). If the index position
is not an int or out of range, a ValueError is raised.
- `search_value(self, val)`:Returns the index of the first occurrence of an element at val, or -1 if val is not contained in the list. If
val is not an int, a ValueError is raised.
- `insert(self, val)`: Adds a node containing val to the list, keeping the list sorted in ascending order. In case of duplicates
the new element is inserted either before or after the existing duplicates. If val is not an int, a ValueError
is raised.
- `remove_first(self, val)`: Removes the first occurrence of the value val from the list and returns True if successful, otherwise
returns False. If val is not an int, a ValueError is raised.
- `remove_all(self, val)`: Removes all occurrences of the value val from the list and returns True if successful, otherwise returns
false. If val is not an int, a ValueError is raised.
- `remove_duplicates(self)`: Removes all duplicate occurrences of values from the list.
- `filter_n_max(self, n)`: Filters the list to the n highest values (0 < n ≤ size). If n is not an int or out of range, a ValueError is
raised.
- `filter_odd(self)`: Removes all even values from the list, so that the resulting list only contains odd values.
- `filter_even(self)`: Removes all odd values from the list, so the resulting list only contains even values.