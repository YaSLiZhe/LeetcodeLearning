### 相同放一起
# 列表list1和list2列表中的相同数字放进list3
# output: [12, 56]

list1 = [12,34,56, 78,9]
list2 = [12,4,56,15,43,89]
list3 = []
for l1 in list1:
	for l2 in list2:
		if l1 == l2: list3.append(l1)
print (list3)