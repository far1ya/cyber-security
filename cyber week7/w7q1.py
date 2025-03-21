def hash_function(key, table_size):
    """
    A simple hash function using the division method.
    :param key: The key to be hashed (e.g., a string or integer).
    :param table_size: The size of the hash table (an integer).
    :return: The index in the hash table.
    """
    return key % table_size

# Example usage
key = 12345
table_size = 10
hashed_value = hash_function(key, table_size)
print(f"Hash of {key} with table size {table_size} is {hashed_value}")
