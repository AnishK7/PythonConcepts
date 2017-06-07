"""
Named Tuples
"""
from collections import namedtuple

employee = namedtuple('Employee', ['id', 'title', 'salary'])


arjun = employee(1,'Developer', 12345)
print(arjun)

aj = employee(id=2, title='Lazy Developer', salary=123)

print(aj)
