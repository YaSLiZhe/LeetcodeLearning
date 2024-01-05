# 文文读文件
# 文文同学得到一份数据，里面数据通过二进制数据存储。他想要知道文件里的数据是什么，以及对应的十进制数据是什么。
# 请使用with...as 语句配合 open() 函数的方式，读取这个txt文件。
# 在open()函数中打开方式为"r"。
# 文件路径： "/Users/file/二进制数.txt"
# 将从文件中获取的二进制的字符串数据转化为相应的十进制数，并分别输出。
# 输出样例：
# 101
# 5

path = "/Users/file/二进制数.txt"

with open(path, "r") as txtFile:
    data = txtFile.read()
L= len(data)
num = 0
for i in range(L):
    num += int(data[L-i-1])*2**i
    
print(data)
print(num)