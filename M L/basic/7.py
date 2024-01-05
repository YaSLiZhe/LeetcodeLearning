### 逢7说“过”

i = 0
x = 1
while(x <= 100):
    if x % 7 == 0 or "7" in str(x): i+=1
    x += 1
print(f"一共说了{i}次过")