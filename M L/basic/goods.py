# 购物小票
# 聪聪去超市购物，她的购物信息如列表goods所示。

# 请定义一个函数showGoods()，传入参数x，帮他遍历列表x，计算总价。

# 列表嵌套字典

goods = [
    {"name": "面包", "mount": 7, "price": 5},
    {"name": "牛奶", "mount": 3, "price": 10},
    {"name": "香蕉", "mount": 1, "price": 12},
    {"name": "大米", "mount": 2, "price": 98}
    ]

def showGoods(x):
    totalPrice = 0
    print("--- 商品信息 ---")
    for i in range(0,len(x)):
        totalPrice += x[i]["price"] * x[i]["mount"]
        print(i+1, x[i]["name"], x[i]["mount"], x[i]["price"])
    print(f"本次购物总价为{totalPrice}元")

showGoods(goods)


# 创建一个列表嵌套字典
list_of_dicts = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]

# 访问列表中的第一个字典，并打印名字
print(list_of_dicts[0]['name'])  # 输出: Alice

# 修改列表中的第二个字典的年龄
list_of_dicts[1]['age'] = 31

# 向列表中添加一个新的字典
list_of_dicts.append({'name': 'David', 'age': 40})

# 输出整个列表
print(list_of_dicts)
# 输出: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 31}, {'name': 'Charlie', 'age': 35}, {'name': 'David', 'age': 40}]
