"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    linear_count = 0                        # this is for counting the number of loops so that I can compare the

    if target is None :                     # if target is None return -1 for the index and 0 for loop count
        return -1, 0
                                            # efficiency of linear search to binary search
    for index, value in enumerate(lst) :
        linear_count = linear_count + 1     # loop count is incremented each time the loop runs
        if value == target :
            return index, linear_count      # the index and loop count are returned as a tuple
    return -1, linear_count                 # if the target is not found then return -1 and the loop count


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    binary_count = 0                        # this is for counting the number of loops so that I can compare the
                                            # efficiency of linear search to binary search
    low = 0
    high = len(lst) - 1

    if target is None :                     # if target is None return -1 for the index and 0 for loop count
        return -1, 0

    while high >= low :
        binary_count = binary_count + 1     #loop count is incremented each time the loop runs
        mid = (high +low) // 2
        if lst[mid] < target :
            low = mid + 1
        elif lst[mid] > target :
            high = mid - 1
        else :
            return mid, binary_count        # the index and loop count are returned as a tuple
    return -1, binary_count                 # if the target is not found then return -1 and the loop count


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    small_set = [10, 20, 30, 40, 50, 60, 70]
    print(f"Dataset: {small_set}")

    #linear search results
    print("\nLinear Search Results:")

    target = 50
    search_index, loop_count = linear_search(small_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    target = 100
    search_index, loop_count = linear_search(small_set, target)
    print(f"\nSearch Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    #binary search results
    print("\nBinary Search Results:")
    target = 50
    search_index, loop_count = binary_search(small_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    target = 100
    search_index, loop_count = binary_search(small_set, target)
    print(f"\nSearch Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")



    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n\n=== LARGE DATASET TEST ===")

    large_set = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 31, 32, 33, 34, 35, 36, 37, 38, 39, 51, 52, 53, 54, 55, 56, 57]
    print(f"Dataset: {large_set}")

    print("\nLinear Search Results:")

    target = 16
    search_index, loop_count = linear_search(large_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    target = 100
    search_index, loop_count = linear_search(large_set, target)
    print(f"\nSearch Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    #binary search results
    print("\nBinary Search Results:")
    target = 16
    search_index, loop_count = binary_search(large_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    target = 100
    search_index, loop_count = binary_search(large_set, target)
    print(f"\nSearch Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")



    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n\n=== EDGE CASE TESTS ===")

    print("\nLinear Search of an Empty List:")
    test_set = []
    print(f"Dataset: {test_set}")
    target = 10
    search_index, loop_count = linear_search(test_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    print("\nBinary Search of an Empty List:")
    test_set = []
    print(f"Dataset: {test_set}")
    target = 10
    search_index, loop_count = binary_search(test_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    print("\nLinear Search with a Null Target:")
    test_set = [10, 20, 30, 40, 50, 60, 70]
    print(f"Dataset: {test_set}")
    target = None
    search_index, loop_count = linear_search(test_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    print("\nBinary Search with a Null Target:")
    test_set = [10, 20 , 30, 40, 50, 60, 70]
    print(f"Dataset: {test_set}")
    target = None
    search_index, loop_count = binary_search(test_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    print("\nLinear Search with a single item list:")
    test_set = [10]
    print(f"Dataset: {test_set}")
    target = 10
    search_index, loop_count = linear_search(test_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")

    print("\nBinary Search with a single item list:")
    test_set = [10]
    print(f"Dataset: {test_set}")
    target = 10
    search_index, loop_count = binary_search(test_set, target)
    print(f"Search Target: {target}")
    print(f"Index: {search_index}")
    print(f"Number of loops: {loop_count}")


if __name__ == "__main__":
    main()