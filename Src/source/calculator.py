'''
Author: ayzp yu_zhi_peng@126.com
Date: 2023-01-18 15:11:48
LastEditors: ayzp yu_zhi_peng@126.com
LastEditTime: 2023-01-18 16:18:06
FilePath: \timercry\Src\source\calculator.py
Description: 用于测试UT，作为例子存在,
'''

class Calculator:
    def add(self, *args):
        result = 0

        for n in args:
            result += n
        
        return result