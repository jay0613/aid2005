list01 = [1, 9, 2, 1, 1, 3, 9, 2, 1, "张", 1111, 1]
list02 = [7, 8, 9, 5, 4, 2, 1, 8]

list01.insert(1, "你好")  # 在指定索引处添加元素
list01.append("app")  # 在列表后面添加项目(可以是单个元素或者容器)

# extend和append差不多 但是如果给新列表添加一个旧列表则会把旧列表拆了,把元
# 素一个一个的添加进去新列表,而append则是直接把整个列表添加进去
list01.extend(list02)   # 把list02列表拆了把元素一个一个添加进去list01里面
list01.remove("张")  # 内部会从头到尾进行查找,删除第一个匹配项
a = list01.pop(6)  # 删除索引处的元素,并返回该元素，不写参数，默认删除最后一个
b = list01.copy()  # 复制列表
# list01.clear()  # 清除列表内所有元素
c = list01.count(1)  # 返回数字1在列表中的数量
d = list01.index(9)  # 查找列表返回该元素的索引(只会返回查找到的第一个)
list02.sort()  # 把列表从小到大排序,改变原容器
list02.reverse()  # 把原来列表反转,头变尾,尾变头(并不是从大到小或者从小到大)

# 整理完毕

# 方案2
