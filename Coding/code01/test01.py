"""
用于熟悉python语法基础
"""
# !/usr/bin/python
import re
from osgeo import gdal
from osgeo import ogr
from selenium import webdriver
from selenium.webdriver import Chrome

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

driver = Chrome()
driver.get('')

'''查找元素的所有方法'''
# 前端代码如下：
# <span class="bg s_ipt_wr quickdelete-wrap">
#     <span class="soutu-btn"></span>
#     <input id="kw" class="s_ipt" autocomplete="off" maxlength="255" value="" name="wd">
#     <a id="quickdelete" class="quickdelete" href="javascript:;" title="清空" style="top: 0px; right: 0px; display: none;"></a>
# </span>
# <span class="bg s_btn_wr">
#     <input id="su" class="bg s_btn" type="submit" value="百度一下">
# </span>

driver.find_element_by_xpath()
driver.find_element()
driver.find_element_by_id("kw")  # 使用id查找
driver.find_element_by_name('wd')
driver.find_element_by_class_name("s_btn")
# 利用元素属性来进行xpath定位
driver.find_element_by_xpath("//input[@id='kw']")
#  标签名input也可以用*来代替,只要是在该标签内，任意属性都可以
driver.find_element_by_xpath("//*[@name='wd']")
#  CSS属性定位可以比较灵活地选择控件的任意属性，定位方式也会比xpath快
#  一般class是用.标记，id是用#标记，标签名直接写具体标签名
driver.find_element_by_css_selector('.s_ipt')
driver.find_element_by_css_selector("#su")
# css定位里面也可以通过属性或者组合方式定位：
driver.find_element_by_css_selector("input[autocomplete='off']")
# 这样写的定位顺序是这样的，先定位到一个class名为bg s_btn_wr的span标签，
# 在这个标签下面有一个id为su的input标签，这样就定位到了
driver.find_element_by_css_selector("span.bg.s_btn_wr>input#su")
# 在CSS里面下级标签用>链接，如果class中有空格，空格用.表示
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()

# By定位
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "kw")
driver.find_element(By.NAME, "wd")
driver.find_element(By.CLASS_NAME, "s_ipt")
driver.find_element(By.TAG_NAME, "input")
driver.find_element(By.LINK_TEXT, u"新闻")
driver.find_element(By.PARTIAL_LINK_TEXT, u"新")
driver.find_element(By.XPATH, "//*[@class='bg s_btn']")
driver.find_element(By.CSS_SELECTOR, "span.bg s_btn_wr>input#su")












