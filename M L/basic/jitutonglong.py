# 鸡兔同笼问题
# input:
# 35
# 94
# output:
# chicken=23.0, rabbit=12.0

heads = int (input())
feet = int (input())
rabbit = (feet - heads * 2) / 2
chicken = heads - rabbit
if rabbit.is_integer() and chicken.is_integer() and rabbit>=0 and chicken>=0:
	print(f"chicken={chicken}, rabbit={rabbit}")
else: print ("no result")