"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""
from xxlimited_35 import Null


def insert_at(lst, index, value):
    #this function inserts a value at the specified index of a list
    #insert at index 0 will insert the value at the beginning of the list, which requires all other
    #items after it to be moved to the 'right' in the list. The speed of this operation is O(n), and will
    #become increasingly slower as the list becomes longer.
    #inserting at an index in the middle will work the same, shifting all elements at and after the index
    #to the right.
    #to insert a value at the end of the list with the insert method requires the use of len() to get the
    #number after the last index in the list. This is an O(1) operation because nothing has to shift, and
    #the use of len() is also O(1) because python lists store their length.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if not 0 <= index < len(lst):
        return None
    return lst.pop(index)

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    try:
        return lst.index(value)
    except ValueError:
        return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    print("\n=== INSERTION TESTS ===")
    # 1. Create a list containing several values.
    tripOrder = ["Germany", "Switzerland", "Italy", "Austria", "Czechia"]
    # 2. Display the original list.
    print(tripOrder)
    # 3. Test insertion at:
    #   -the beginning
    insert_at(tripOrder, 0, "France")
    print(tripOrder)
    #    - the middle
    insert_at(tripOrder, 3, "Slovenia")
    print(tripOrder)
    #    - the end
    insert_at(tripOrder, len(tripOrder), "Poland")
    print(tripOrder)



    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    print(delete_at(tripOrder, -1))



    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    print(search_value(tripOrder, "Germany"))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")



if __name__ == "__main__":
    main()