# Playground for Effective Python: 55 Specific Ways to Write Better Python

# Pythonic
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

# Chapter 2  Function
# * Tip 14: Prefer Exceptions to Returning None

# * Tip 15: Know How Closures Interact with Variable Scope

# * Tip 16: Consider Generators Instead of Returning Lists
# def index_file(handle):
#     offset = 0
#     for line in handle:
#         if line:
#             yield offset
#         for letter in line:
#             offset += 1
#             if letter == ' ':
#                 yield offset


# text = 'Four score and seven years ago'
# with open('tmp.txt', 'w') as f:
#     f.write(text)

# with open('tmp.txt', 'r') as f:
#     it = index_file(f)
#     print(list(it))


# * Tip 17: Be Defensive When Iterating Over Arguments
# def normalize(numbers):
#     total = sum(numbers)
#     result = []
#     for value in numbers:
#         percent = 100 * value / total
#         result.append(percent)
#     return result


# def normalize_defensive(numbers):
#     if iter(numbers) is iter(numbers):
#         raise TypeError('Must supply a container !')
#     total = sum(numbers)
#     result = []
#     for value in numbers:
#         percent = 100 * value / total
#         result.append(percent)
#     return result


# class ReadVisit:
#     def __init__(self, datapath):
#         self.datapath = datapath

#     def __iter__(self):
#         with open(self.datapath) as f:
#             for line in f:
#                 yield int(line)


# def lines(numbers):
#     result = [str(value) + '\n' for value in numbers]
#     return result


# visits = [15, 35, 80]


# with open('visit_data.txt', 'w') as f:
#     f.writelines(lines(visits))

# print(normalize_defensive(visits))
# new_visits = ReadVisit('visit_data.txt')
# print(normalize_defensive(new_visits))

# * Tip 18: Reduce Visual Noise with Variable Positional Arguments

# * Tip 19: Provide Optional Behavior with Keyword Arguments

# * Tip 20: Use None and Docstrings to Specify Dynamic Default Arguments

# * Tip 21: 用只能以关键字形式指定的参数来确保代码明晰

# * Tip 22: 尽量用辅助类来维护程序的状态，而不要用字典和元组
# from collections import namedtuple

# Grade = namedtuple('Grade', ('score', 'weight'))


# class Subject:
#     def __init__(self):
#         self._grades = []

#     def report_grade(self, score, weight):
#         self._grades.append(Grade(score, weight))

#     def average_grade(self):
#         total, total_weight = 0, .0
#         for grade in self._grades:
#             total += grade.score * grade.weight
#             total_weight += grade.weight
#         return total / total_weight


# class Student:
#     def __init__(self):
#         self._subjects = {}

#     def subject(self, name):
#         if name not in self._subjects:
#             self._subjects[name] = Subject()
#         return self._subjects[name]

#     def average_grade(self):
#         total, count = 0, 0
#         for subject in self._subjects.values():
#             total += subject.average_grade()
#             count += 1
#         return total / count


# class GradeBook:
#     def __init__(self):
#         self._students = {}

#     def student(self, name):
#         if name not in self._students:
#             self._students[name] = Student()
#         return self._students[name]


# book = GradeBook()
# albert = book.student('Albert Einstein')
# math = albert.subject('Math')
# math.report_grade(70, 0.3)
# math.report_grade(80, 0.7)
# print(albert.average_grade())

# * Tip 23: 简单的接口应该接受函数，而不是类的实例

# from collections import defaultdict


# class BetterCounterMissing:
#     def __init__(self):
#         self.added = 0

#     def __call__(self):
#         self.added += 1
#         print('New Key Added')
#         return 0


# current = {'green': 12, 'blue': 3}
# increments = [
#     ('red', 5),
#     ('blue', 17),
#     ('orange', 9),
# ]

# counter = BetterCounterMissing()
# result = defaultdict(counter, current)
# for key, amount in increments:
#     result[key] += amount
# print(result)
# print(result['pink'])

# * Tip 24: 以 @classmethod 形式的多态去通用地构建对象

# * Tip 25: 用super初始化父类

# * Tip 26: 只在使用 Mix-in 组件制作工具类时进行多重继承

# * Tip 27: 多用 public 属性，少用 private 属性

# * Tip 28: 继承 collections.abc 以实现自定义的容器类型

# Chapter 4  元类及属性

# * Tip 29: 用纯属性取代get和set方法

# * Tip 30: 考虑用 @property 来代替属性重构

# * Tip 31: 用描述符来改写需要复用的 @property 方法

# * Tip 32: 用 __getattr__、__getattribute__ 和 __setattr__ 实现按需生成的属性

# * Tip 33: 用元类来验证子类

# * Tip 34: 用元类来注册子类

# * Tip 35: 用元类来注解类的属性

# Chapter 5  并发及并行

# Chapter 6  内置模块

# * Tip 42:
