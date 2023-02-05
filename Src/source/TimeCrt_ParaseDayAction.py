'''
Author: ayzp yu_zhi_peng@126.com
Date: 2023-01-03 21:45:39
LastEditors: ayzp yu_zhi_peng@126.com
LastEditTime: 2023-02-05 11:04:51
FilePath: \timer-cry\5-TR4A\Codes\src\ParaseDayAction.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

##########################################################################################################
#BEGIN===>libaray
# 从剪贴板复制，粘贴数据
import pyperclip as pyperclip

import datetime

#END===>libaray
##########################################################################################################


##########################################################################################################
#BEGIN===>data struct

firstClassMemberList = [
    "第I类工作",
    "第II类工作",
    "第III类工作",
    "第IV类工作",
]

secondClassMemberList = [
    "中心事务",
    "组织工作",
    "可能自我",
    "",
    "英语能力",
    "编程能力",
    "阅读能力",
    "技能",
    "日常",
    "",
    "娱乐",
    "社交",
    "杂事",
    "",
    "吃饭",
    "睡觉",
    "交通",
    "家务",
    "",
    "时间管理",
]

thirdClassMemberList = [
    "中心工作",
    "中心事务文档",
    "例会",
    "工作沟通",
    "个人品牌",
    "自我思考",
    "可能自我文档",
    "听力",
    "单词&阅读",
    "口语",
    "编程工具",
    "编程参考书",
    "编程文档",
    "阅读",
    "阅读文档",
    "摄影",
    "煮饭",
    "健康",
    "技能文档",
    "练字",
    "学习强国",
    "手机",
    "电影",
    "音乐会/展览会/话剧/旅游",
    "家人聊天",
    "朋友聊天",
    "同事聊天",
    "干活",
    "早中晚夜宵",
    "聚餐",
    "去上班、回家",
    "洗漱洗澡",
    "整理打扫",
    "总结计划",
    "时间管理方法更新",
]

fourthClassMemberList = [
    "工作",
    "bilibili更新",
    "CSDN&个人博客",
    "简书",
    "微信公众号",
    "刷题",
    "算法基础视频",
    "linux视频",
    "项目",
    "Python",
    "linux内核",
    "锻炼",
]


class FirstClass:
    # 描述
    description = "用来存储第一级类事情所使用的时间"
    memberList = []

    # 时间
    totalTime = 0
    # 内容


    # method
    def __init__(self) -> None:
        pass

class SecondClass:
    # attribute fields
    

    # method
    def __init__(self) -> None:
        pass

class ThirdClass:
    # attribute fields
    

    # method
    def __init__(self) -> None:
        pass

class FourthClass:
    # attribute fields
    

    # method
    def __init__(self) -> None:
        pass

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

    sleepTime = "NULL"
    getupTime = "NULL"

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


#END===>data struct
##########################################################################################################


##########################################################################################################
#BEGIN===>API
# 将字符串的时间转换为数字的时间分钟
def strTime2NumTime(strTime):
    strTimeList = strTime.split(":")
    NumTime = int(strTimeList[0]) * 60 + int(strTimeList[1])
    return NumTime

# 将分钟数转换为字符串的时间
def numTime2StrTime(NumTime):
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

    # print(dataDay)




#END===>API
##########################################################################################################


print("HELLO")

readDataFromClipboard()
