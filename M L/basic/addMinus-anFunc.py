### 加or减 - 匿名函数的用法（定义和调用）
# 定义匿名函数，若参数x大于y，则计算参数x与y的和；否则计算参数x与y的差。

func = lambda x, y: x + y if x > y else x - y
print(func(3, 5))