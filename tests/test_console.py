import unittest

from unittest.mock import patch

from io import StringIO

from console import HBNBCommand

class Test_console(unittest.TestCase):
    def test_calculate_total(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            tmp1 = int(f.read())
            HBNBCommand().onecmd("create BaseModel name=\"bakka\"")
            HBNBCommand().onecmd("BaseModel.count()")
            f.seek(0)
            tmp2 = int(f.read())
            self.assertEqual(tmp2, tmp1 + 1)
