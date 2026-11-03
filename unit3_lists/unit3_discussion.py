"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""
#from xxlimited_35 import Null


def insert_at(lst, index, value):
    # this function inserts a value at the specified index of a list
    # insert at index 0 will insert the value at the beginning of the list, which requires all other
    # items after it to be moved to the 'right' in the list. The speed of this operation is O(n), and will
    # become increasingly slower as the list becomes longer.
    # inserting at an index in the middle will work the same, shifting all elements at and after the index
    # to the right.
    # to insert a value at the end of the list with the insert method requires the use of len() to get the
    # number after the last index in the list. This is an O(1) operation because nothing has to shift, and
    # the use of len() is also O(1) because python lists store their length.
    lst.insert(index, value)


def delete_at(lst, index):
    # index validation is important to allow the app to 'fail gracefully' instead of throwing an error
    # safe deletion is important to make sure that only the intended value is being removed
    if not 0 <= index < len(lst):
        return None
    return lst.pop(index)

def search_value(lst, value):
    # using the .index() method is a linear search that scans sequentially because it takes the search value and
    # starting from the first value in the list, compares to every value in the list in order until it reaches the
    # first match. The worst case is O(n), if the search value does not exist it will check every value
    try:
        return lst.index(value)
    except ValueError:
        return -1

def search_results(lst, search_term):
    # I created this function in order to meet the requirement of "Display the search results with clear explanations."
    # while still meeting the requirement that the search_value function return -1 if value not found
    # this function takes the return of search_value and provides a user-readable output
    result = search_value(lst, search_term)
    if result == -1:
        return f"'{search_term}' not found, result: {result}"
    return f"'{search_term}' found at index: {result}"



def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    print("\n=== INSERTION TESTS ===")
    # 1. Create a list containing several values.
    trip_order = ["Germany", "Switzerland", "Italy", "Austria", "Czechia"]
    # 2. Display the original list.
    print(trip_order)
    # 3. Test insertion at:
    #   -the beginning
    insert_at(trip_order, 0, "France")
    print(trip_order)                                        # 4. Display the list after each insertion.
    #    - the middle
    insert_at(trip_order, 3, "Slovenia")
    print(trip_order)                                        # 4. Display the list after each insertion.
    #    - the end
    insert_at(trip_order, len(trip_order), "Poland")
    print(trip_order)                                        # 4. Display the list after each insertion.


    print("\n=== DELETION TESTS ===")
    # 1. Delete an item from:
    #    - the beginning
    print(delete_at(trip_order, 0))  # 2. Display the removed value.
    print(trip_order)                      # 3. Display the updated list after each deletion.
    #    - the middle
    print(delete_at(trip_order, 3))  # 2. Display the removed value.
    print(trip_order)                      # 3. Display the updated list after each deletion.
    #    - the end
    print(delete_at(trip_order, len(trip_order)-1))  # 2. Display the removed value.
    print(trip_order)                      # 3. Display the updated list after each deletion.


    print("\n=== SEARCH TESTS ===")
    # I created the search_results() function to meet the requirements of both the search_value() function and
    # the requirements of this search test section. search_results() calls search_value() to provide the index
    # 1. Search for a value that exists.
    print(search_results(trip_order, "Austria")) # 3. Display the search results with clear explanations.
    # 2. Search for a value that does not exist.
    print(search_results(trip_order, "England")) # 3. Display the search results with clear explanations.

    print("\n=== EDGE CASES ===")
    test_list = []                                       # create an empty list
    print(search_results(trip_order, None))   # search with null search term
    print("Searching an empty list with a Null value:")
    print(search_results(test_list, None))    # search with null search term
    #delete from an empty list
    print("\nAttempt delete from an empty list:")
    print(delete_at(test_list, 0))                 # attempt to delete from index 0 of the empty list


if __name__ == "__main__":
    main()