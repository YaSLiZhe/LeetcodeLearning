def func(d):
    count = 0
    for i in range(1, d+1):
        if i%2==0: i = -i
        count += i 
    print(count)

func(99)