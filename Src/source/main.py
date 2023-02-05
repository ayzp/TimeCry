# main.py
# =============================================
from fileinput import filename
import json
import datetime
from pathlib import Path
import PySimpleGUI

# 从剪贴板复制，粘贴数据
import pyperclip as pyperclip

# 系统相关
# import os

##########################################################################################################
#BEGIN===>DataType Definition
homeFolder = Path.cwd()
srcFolder = homeFolder / 'src'
incFolder = homeFolder / 'inc'
dataFolder = homeFolder / 'data'



class Events_T:
    # attribute fields
    name = "NULL"
    eventDuringTime = 0

    # method
    def __init__(self) -> None:
        pass

class DayEvents:
    # attribute fields
    weather = "NULL"
    place = "NULL"
    dateRecord = "NULL"
    dreamRecord = "NULL"

    QuadrantI = {
        "alias": "TypeI",
        "CenterThing": {
            "CenterWork": 100,
            "Doc": 100
        },
        "OrganizationThing": {
            "OrganizationWork": 100
        },
        "PossibleSelf": {
            "PersonalBrand": 100,
            "ThoughtSelf": 100,
            "Doc": 100
        }
    }

    # method
    def __init__(self) -> None:
        pass


oneDay = DayEvents() # 创建一个类实例

#END===>DataType Definition
##########################################################################################################


##########################################################################################################
#BEGIN===>API

# 将字符串的时间转换为数字的时间分钟
def strTime2NumTime(strTime):
    strTimeList = strTime.split(":")
    NumTime = int(strTimeList[0]) * 60 + int(strTimeList[1])
    return NumTime

# 将分钟数转换为字符串的时间
def strTime2NumTime(NumTime):
    strTime = str(int(NumTime / 60)) + ":" + str(NumTime % 60)
    return strTime

# 从剪贴板读取时间
# 输入：先复制OneNote中的数据
# 输出：将数据复制到oneDay类中
# 当前，oneDay类的数据还没有规划怎么存储
def readDataFromClipboard():
    dataDay = pyperclip.paste()
    dataDayLines = dataDay.split("\r\n")

    # print(dataDay[0])
    oneDay.weather = dataDayLines[0]
    oneDay.place = dataDayLines[1]
    oneDay.dateRecord = dataDayLines[2]
    oneDay.dreamRecord = dataDayLines[3]

    for i in range(4, len(dataDayLines)-4, 2):
        startTime = dataDayLines[i]
        events = dataDayLines[i+1]
        endTime = dataDayLines[i+2]

        # 计算一件事情持续时间：以分钟计算，后面需要将其还原为字符串进行写入EXCEL
        eventDuringTime = strTime2NumTime(endTime) - strTime2NumTime(startTime)

        print(startTime, events, endTime, eventDuringTime)

    print(dataDay)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def addData():
    print("add Data")



def writeData():
    print(writeData)

#END===>API
##########################################################################################################

# TODO : 准备数据中间存储结构体：
# TODO : 写入excel数据，从中间存储结构体对应拿，然后写入特定的位置上去


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    readDataFromClipboard()
    print("Success")















