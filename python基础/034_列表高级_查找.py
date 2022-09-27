# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 14:00
# @Author : fx
# @File : 034_列表高级_查找
# @Project : pythonProject

food_list = ['红烧肉', '绿烧肉', '白烧肉']

food_need = input('输入你想吃的食物')

if food_need in food_list:
    print('嘉然今天吃%s' % food_need)
else:
    print('嘉然今天没得吃')
