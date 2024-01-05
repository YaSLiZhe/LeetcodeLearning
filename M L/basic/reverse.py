# 文本翻转
# 编写一个名为 rev() 的函数，传入参数s，实现对字符串x反转。
# 函数内首先通过判断字符串s是否为空（""），或者s的长度是否为1，若满足则反转后的字符串为本身；
# 否则，通过字符串切片和递归实现字符串反转。
# 最后，传入参数s为"yequbiancheng"，调用函数rev() 并输出结果。

def rev(s):
    if s == "" or len(s) == 1: return s
    # 反转后字符串为最后一个元素➕反转前的len(s)-1个元素
    revStr = s[-1] + rev(s[0:len(s)-1])
    return revStr

s = "yequ"
print(rev(s))

