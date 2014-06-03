"""

>>> l = MonoList()
>>> l.append(3)
>>> len(l)
1
>>> l.append('x')
Traceback (most recent call last):
  ...
TypeError: 'x' is not the same type as 3 (int)
>>> l.extend(range(4))
>>> len(l)
5
>>> l.extend([10, [11]])
Traceback (most recent call last):
  ...
TypeError: '[11]' is not the same type as 3 (int)


"""
