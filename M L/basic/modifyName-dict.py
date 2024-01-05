### 成绩修改 - 字典获取所有键值对

# lily和tony的成绩登反了，输出修改后的成绩。

score = {"lily":97, "qiqi":93, "tony":78, "fenfen":88}
item = score['lily']
score['lily'] = score["tony"]
score["tony"] = item

print("---学生成绩---")
for key in score:
    print(key, score[key])
# for key, value in score.items():   print(key, value)