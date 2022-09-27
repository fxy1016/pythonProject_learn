# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 13:51
# @Author : fx
# @File : 032_列表高级
# @Project : pythonProject

# append,加到后面

food_list = ['红烧肉', '绿烧肉', '白烧肉']
print(food_list)
food_list.append('紫烧肉')
print(food_list)

# insert
char_list = ['a','c','d']
char_list.insert(1,'b')
print(char_list)

# extend
food_list = ['红烧肉', '绿烧肉', '白烧肉']
char_list = ['a','c','d']
food_list.extend(char_list)
print(food_list)