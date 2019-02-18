

from collections import Counter
import random
# 1-5随机取数，后面的意思就是循环100次，成了一个集合datas
datas = [random.randint(1,5) for i in range(100)]
print(type(datas))
print(datas)

counter = Counter()
for data in datas:
    # 用中括号
    counter[data] += 1
print(counter)