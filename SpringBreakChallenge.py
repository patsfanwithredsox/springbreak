#Remove spaces

>>> s = " \t foo \n bar "
>>> "".join(s.split())
'foobar'