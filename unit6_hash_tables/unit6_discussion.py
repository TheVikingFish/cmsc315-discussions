"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""

# I created this class to quickly display all contents of a dictionary for this assignment
def display_dict(dictionary):
    # this loop prints every key-value pair in the dictionary in an easy-to-read format
    for item, qty in dictionary.items():
        print(f"{item}: {qty}")



def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # 1. Create an empty dictionary.
    home_inventory = {}

    # 2. Add at least 5 key-value pairs.
    # the dictionary is like a hash table because it uses unique keys that are hashed and
    # are also paired with values. Collisions and resizing are in the background in Python
    home_inventory["air_filters"] = 2
    home_inventory["dish_pods"] = 20
    home_inventory["milk"] = 1
    home_inventory["apples"] = 8
    home_inventory["shampoo"] = 3

    # 4. Display the contents of the dictionary.
    # this custom class uses a loop to print every key-value pair in a dictionary
    display_dict(home_inventory)



    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # two existing keys are retrieved and clearly displayed here
    # in this example with home_inventory[key], the key is hashed, the hash is masked to a slot,
    # Python checks the stored hash and then compares the hashes, and then probes for a collision
    print(f"apples: {home_inventory['apples']}")
    print(f"air_filters: {home_inventory['air_filters']}")



    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("\nDictionary before updating:")
    display_dict(home_inventory)

    #updating the value of an existing key
    # updating hashes the key, follows the same probe sequence as lookup, and overwrites the value
    # when it finds a matching key. No new slot is used and the order is unchanged
    home_inventory["dish_pods"] = 0

    print("\nDictionary after updating:")
    display_dict(home_inventory)



    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("\nDictionary before deleting a key-value pair:")
    display_dict(home_inventory)

    # using the del keyword to delete a key-value pair from the dictionary
    # Deleting find the key via the same hash probe, then marks the slot as a tombstone instead of
    # emptying it, so the lookups for keys that collide past it can still find them
    del home_inventory["air_filters"]

    print("\nDictionary after deleting a key-value pair:")
    display_dict(home_inventory)



    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    print("\nThe results of trying to delete a key that doesn't exist using home_inventory.pop():")
    # delete a missing key safely by using the .pop() method with a default value that will return
    # if the key is not found
    print(home_inventory.pop("nonexistant_key", None))

    print("\nThe results of trying to lookup a key that doesn't exist using home_inventory.get():")
    # the .get() method allows us to give a default value if the key is not found, otherwise there
    # would be an error
    print(home_inventory.get('nonexistant_key', None))
    

if __name__ == "__main__":
    main()