class CollectionOperations:
    def __init__(self):
        pass

    # List Operations
    def append_to_list(self, input_list, element):
        """Append an element to the list."""
        input_list.append(element)
        return input_list

    def remove_from_list(self, input_list, element):
        """Remove an element from the list."""
        input_list.remove(element)
        return input_list

    def extend_list(self, input_list, elements):
        """Extend the list by appending elements from another list."""
        input_list.extend(elements)
        return input_list

    def sort_list(self, input_list):
        """Sort the list in ascending order."""
        input_list.sort()
        return input_list

    # Tuple Operations
    def concatenate_tuples(self, tuple1, tuple2):
        """Concatenate two tuples."""
        return tuple1 + tuple2

    def repeat_tuple(self, input_tuple, times):
        """Repeat the tuple a given number of times."""
        return input_tuple * times

    def get_tuple_element(self, input_tuple, index):
        """Get an element from the tuple by index."""
        return input_tuple[index]

    def slice_tuple(self, input_tuple, start, end):
        """Get a slice from the tuple."""
        return input_tuple[start:end]

    # Dictionary Operations
    def add_to_dict(self, input_dict, key, value):
        """Add a key-value pair to the dictionary."""
        input_dict[key] = value
        return input_dict

    def remove_from_dict(self, input_dict, key):
        """Remove a key-value pair from the dictionary."""
        if key in input_dict:
            del input_dict[key]
        return input_dict

    def get_dict_value(self, input_dict, key):
        """Get a value from the dictionary by key."""
        return input_dict.get(key)

    def get_dict_keys(self, input_dict):
        """Get all keys from the dictionary."""
        return list(input_dict.keys())

    def get_dict_values(self, input_dict):
        """Get all values from the dictionary."""
        return list(input_dict.values())


if __name__ == "__main__":
    collection_ops = CollectionOperations()

    # List operations
    my_list = [1, 2, 3]
    print("Original List:", my_list)
    print("Append 4:", collection_ops.append_to_list(my_list, 4))
    print("Remove 2:", collection_ops.remove_from_list(my_list, 2))
    print("Extend with [5, 6]:", collection_ops.extend_list(my_list, [5, 6]))
    print("Sorted List:", collection_ops.sort_list(my_list))

    # Tuple operations
    my_tuple = (1, 2, 3)
    print("\nOriginal Tuple:", my_tuple)
    print("Concatenate with (4, 5):", collection_ops.concatenate_tuples(my_tuple, (4, 5)))
    print("Repeat 3 times:", collection_ops.repeat_tuple(my_tuple, 3))
    print("Get element at index 1:", collection_ops.get_tuple_element(my_tuple, 1))
    print("Slice from 1 to 3:", collection_ops.slice_tuple(my_tuple, 1, 3))

    # Dictionary operations
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("\nOriginal Dictionary:", my_dict)
    print("Add key 'd' with value 4:", collection_ops.add_to_dict(my_dict, 'd', 4))
    print("Remove key 'b':", collection_ops.remove_from_dict(my_dict, 'b'))
    print("Get value for key 'c':", collection_ops.get_dict_value(my_dict, 'c'))
    print("Get all keys:", collection_ops.get_dict_keys(my_dict))
    print("Get all values:", collection_ops.get_dict_values(my_dict))