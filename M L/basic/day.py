d = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
def calDay(year, month, day):
    count = 0
    if year > 9999 or year < 1000: print("输入的年份格式错误！")
    if month > 12 or month <= 0: print("输入的月份格式错误！")
    # 代码中的闰年判断逻辑是错误的。应该是这样判断一个年份是否为闰年：如果年份能被4整除但不能被100整除，或者能被400整除，那么这一年就是闰年。
    if (year%4==0 and year%100!=0) or year%400==0:
        d[2] = 29
    # 日格式的检查应该在循环外进行，而且应该只针对指定的月份进行检查。
    if day < 1 or day > d[month]: print("输入的日格式错误！")
    for key in d:
        if key < month: count += d[key]
    count += day
    print(f"{year}年{month}月{day}日是这一年的第{count}天！")
calDay(2021, 5, 20)
    