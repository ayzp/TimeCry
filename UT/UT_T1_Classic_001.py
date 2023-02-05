import unittest
import sys
import logging
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Src.source.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Setup
        cal = Calculator()
        except_result = 10
        
        # Action 
        actual_result = cal.add(2, 3, 5)
        
        # Assert
        self.assertEqual(except_result, actual_result)