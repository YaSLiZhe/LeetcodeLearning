### 时间转换

# 下午5点21分34秒，将时间换算成秒，占一整天秒数的比例

def time2sec(time):
    if time[0] == "上午": time[1] += 0
    else: time[1] += 12
    t = time[1]*60*60+time[2]*60+34
    f = 24*60*60
    print(f"{time[0]}5点{time[2]}分{time[3]}秒换算成秒为{t}秒，占一整天秒数的比例为{t/f}")

time = ["下午", 5, 21, 34]
time2sec(time)