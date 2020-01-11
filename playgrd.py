# Playground for Effective Python: 55 Specific Ways to Write Better Python

# # * Tip 1: system info
# import sys

# sys.version_info
# sys.version

# # * Tip 2: PEP 8

# # * Tip 3: Difference between bytes and str
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

# # * Tip4: Use utility funcs to replace complicated exprs
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

# * Tip 5: Slicing seqs
