### 本月工资条 - 字典
# 输出均值
# 11.4

my_dict ={"cc": 8, "yoyo" :11, "kiki": 14, "bobo" :9, "lily": 15}
total = 0
i = 0
for value in my_dict.values():
	total += value
	i += 1
average = total / i
print(average)