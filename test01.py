"""
用于熟悉python语法基础
"""
# !/usr/bin/python
import re

# 类之间的调用


# ---------字符串的使用--------------------------------------
var1 = "hello world!"
print(var1[1:3])
print("ar1[1:7]", var1[1:7])
print(var1[1:8])
print(var1[2:5])  # 输出为'llo', 2是起始下标

# 字符串格式化
print("My name is %s ，age is %d !" % ('Mary', 21))

# python的字符串 string内置函数
str1 = var1.capitalize()  # 字符串第一个字符大写
str2 = var1.center(15)  # 返回一个原字符串居中,并使用空格填充至长度为15的新字符串
str3 = var1.count('o')  # 返回 'o' 在 字符串var1 里面出现的次数
str4 = var1.replace('hello', 'hi')  # 将var1中的'hello'，替换成'hi',得到一个新字符串
bool_value = var1.startswith('h')  # 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False

# 将字符串中的数字解析出来转换成int类型
string01 = "共15条,每页显示"
string_a = string01.replace('共', '')
string_b = string_a.replace('条,每页显示', '')
num = int(string_b)
num += 2
print(num)

# ------------列表的使用-----------------------------------------
list01 = ['c', 'c++01', 'c++', 'Java', 'python']
del list01[1]  # 删除列表中第二个元素
list_1 = list01[-1]  # 读取倒数第1个
list_2 = list01[-2]  # 读取倒数第2个

# 插入列表 insert(index, obj)
list01.insert(0, 'smile')  # index=0时，从头部插入obj
# ['smile', 'c', 'c++', 'Java', 'python']
list01.insert(2, 'hello')  # index > 0 且 index < len(list)时，在index的位置插入obj,其他依次向后移
# ['smile', 'c', 'hello', 'c++', 'Java', 'python']
list01.insert(10, 'last')  # index大于列表长度时，直接在尾部插入
list01.insert(-13, '-13')  # index<0,且绝对值比len大时，直接从头部插

print('\n打印输出-----------：')
# print(list01)

# ------------正则表达式-----------------------------------------
print(re.match('www', 'www.runoob.com'))
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
