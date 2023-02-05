'''
Author: ayzp yu_zhi_peng@126.com
Date: 2023-02-05 11:10:09
LastEditors: ayzp yu_zhi_peng@126.com
LastEditTime: 2023-02-05 11:10:23
FilePath: \timercry\UT\UT_T1_Classic_Design_Data_001.py
Description: 测试数据结构，测试输出给EXCEL整理模块的数据；
'''
import unittest
import sys
import logging
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# TODO 添加测试
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