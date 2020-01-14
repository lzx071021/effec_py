# Playground for Effective Python: 55 Specific Ways to Write Better Python

# # * Tip 1: Know Which Version of Python You're Using 
# import sys

# sys.version_info
# sys.version

# # * Tip 2: Follow the PEP8 Style Guide

# # * Tip 3: Know the Differences Between bytes, str, and unicode
# import os

# def to_bytes(bytes_or_str):
#     if isinstance(bytes_or_str, str):
#         value = bytes_or_str.encode('utf-8')
#     else:
#         value = bytes_or_str
#     return value  # type: bytes


# def to_str(bytes_or_str):
#     if isinstance(bytes_or_str, bytes):
#         value = bytes_or_str.decode('utf-8', errors='ignore')  # ! UnicodeError without errors='ignore'
#     else:
#         value = bytes_or_str
#     return value  # type: str


# with open('tmp.txt', 'w+') as f:
#     f.write(to_str(os.urandom(10)))

# # * Tip4: Write Helper Functions Instead of Complex Expressions
# from urllib.parse import parse_qs

# my_values = parse_qs('red=5&blue=0&green=',
#                      keep_blank_values=True)
# print(repr(my_values))

# # No
# red = my_values.get('red', [''])[0] or 0
# print('Red: %r' % red)

# # No
# red = my_values.get('red', [''])
# red = int(red[0]) if red[0] else 0

# # Yes
# def get_first_int(values, key, default=0):
#     found = values.get(key, [''])
#     if found[0]:
#         found = int(found[0])
#     else:
#         found = default
#     return found

# * Tip 5: Know How to Slice Sequences

# * Tip 6: Avoid Using start, end and stride in a Single Slice

# * Tip 7: Use List Comprehensions Instead of map and filter

# * Tip 8: Avoid More Than Two Expreesions in List Comprehensions

# * Tip 9: Consider Generator Expressions for Large Comprehensions

# * Tip 10: Prefer enumerate Over range

# * Tip 11: Use zip to Process Iterators in Parallel 

# * Tip 12: Avoid else Blocks After for and while Loops 

# * Tip 13: Take advantage of Each Block in try, except, else, finally 

# * Tip 14: Prefer Exceptions to Returning None

# * Tip 15: Know How Closures Interact with Variable Scope