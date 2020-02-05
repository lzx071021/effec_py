"""Playground for Effective Python: 55 Specific Ways to Write Better Python"""

# Chpater 1  用 Pythonic 方式来思考
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
# * Tip 36: 用 subprocess 模块来管理子进程

# * Tip 37: 可以用线程来执行阻塞式 I/O，但不要用它做平行计算

# * Tip 38: 在线程中使用 Lock 来防止数据竞争

# * Tip 39: 用 Queue 来协调各协程之间的工作

# * Tip 40: 考虑用协程来并发地运行多个函数

# * Tip 41: 考虑用 concurrent.futures 来实现真正的平行计算


# Chapter 6  内置模块

# * Tip 42: 用 functools.wraps 定义函数修饰器
# from functools import wraps


# def trace(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print('%s(%r, %r) -> %r' %
#               (func.__name__, args, kwargs, result))
#         return result
#     return wrapper


# @trace  # Equivalent to fibonacci = trace(fibonacci)
# def fibonacci(n):
#     if n in (0, 1):
#         return n
#     return fibonacci(n - 2) + fibonacci(n - 1)


# fibonacci(3)
# help(fibonacci)

# * Tip 43: 考虑用 contextlib 和 with 语句来改写可复用的 try / finally 代码
# import logging
# from contextlib import contextmanager


# @contextmanager
# def debug_logging(level):
#     logger = logging.getLogger()
#     logger.setLevel(level)
#     old_level = logger.getEffectiveLevel()
#     try:
#         yield logger
#     finally:
#         logger.setLevel(old_level)


# def my_func():
#     # logger = logging.getLogger()
#     # logger.setLevel(logging.DEBUG)
#     # logger.debug('debug data')
#     # logger.error('error data')
#     # logger.debug('more debug data')
#     # logger.warning('warning data')

#     logging.debug('debug data')
#     logging.error('error data')
#     logging.debug('more debug data')
#     logging.warning('warning data')


# with debug_logging(logging.DEBUG):
#     print('Inside: ')
#     my_func()

# print('After: ')
# my_func()

# with debug_logging(logging.DEBUG) as logger:
#     logger.debug('debug data')
#     logging.debug('logging module debug data')  # This msg will not print

# * Tip 44: 用 copyreg 实现可靠的 pickle 操作

# * Tip 45: 应该用 datatime 模块来处理本地时间，而不是用 time 模块

# * Tip 46: 使用内置算法与数据结构

# * Tip 47: 在重视精确度的场合，应该使用 decimal

# * Tip 48: 学会安装由 Python 开发者社区所构建的模块


# Chapter 7  协作开发
# * Tip 49: 为每个函数、类和模块编写文档字符串

# * Tip 50: 用包来安排模块，并提供稳固的 API

# * Tip 51: 为自编的模块定义根异常，以便将调用者与 API 相隔离

# * Tip 52: 用适当的方式打破循环依赖关系

# * Tip 53: 用虚拟环境隔离项目，并重建其依赖关系


# Chapter 8  部署
# * Tip 54: 考虑用模块级别的代码来配置不同的部署环境

# * Tip 55: 通过 repr 字符串来输出调试信息

# * Tip 56: 用 unittest 来测试全部代码

# * Tip 57: 考虑用 pdb 实现交互调试

# * Tip 58: 先分析性能，然后再优化

# * Tip 59: 用 tracemalloc 来掌握内存的使用及泄漏情况
