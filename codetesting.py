import unittest
from io import StringIO
from unittest.mock import patch
from collections import deque

def process_input():
    d = deque()
    for i in range(int(input())):
        inp = input().split()
        getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
    return d

def process_output(d):
    print(*[item for item in d])

class TestCode(unittest.TestCase):
    # d = process_input()
    # process_input()
    def test_program(self):
        input_values = ["4", "append 1", "append 2", "pop", "pop"]
        expected_output = ""

        with patch("builtins.input", side_effect=input_values), patch("sys.stdout", new=StringIO()) as fake_output:
            d = process_input()
            process_output(d)
            actual_output = fake_output.getvalue().strip()

            self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
    

