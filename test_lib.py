from cmath import exp
from lib import *


def test_moyenne():


    data = [10, 11, 12]

    result = moyenne(data)
    expected_result = 11

    if result != expected_result:
        print("test a échoué")
        exit(1)

    

test_moyenne()
exit(0)