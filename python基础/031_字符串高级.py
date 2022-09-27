# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 13:23
# @Author : fx
# @File : 031_字符串高级
# @Project : pythonProject

# 获取长度len()
a = 'hel#lo'
print(len(a))

# 输出第一次出现的下表，1
print(a.find('e'))

# start with ,end with,返回布尔值
print(a.startswith('h'))
print(a.endswith('o'))

# count, 返回查询次数
print(a.count('l'))

# replace 替换。要接受
b = a.replace('l', 'I')
print(b)

# 切割
print(a.split('#'))

b = 'china'
print(b.upper())

c = 'CHINA'
print(c.lower())

# 只能去前后空格
d = '  aafae'
print(len(d))
print(len(d.strip()))

# join,spilt的逆操作
e = 'a'
print(e.join('jerry'))