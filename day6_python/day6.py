import string

from day6_python.input import input_prod
from day6_python.test_input import input_test

listof_int = []
votes = 0
for str in input_prod:
    number_of_participant = len(str.split(','))
    for char in string.ascii_lowercase:
        if str.count(char) == number_of_participant:
            votes += 1

print(votes)