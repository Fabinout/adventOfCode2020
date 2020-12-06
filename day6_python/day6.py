from day6_python.input import input_prod
from day6_python.test_input import input_test


listof_int = []

for str in input_prod:
    s = set(str)
    if ',' in s: s.remove(',')
    listof_int.append(len(s))

print(sum(listof_int))