
names = ["xiaoyu", 'xiaochen','xiaozeng']
invite = "一块吃个饭吧？ "
invite = "一块吃个饭吧 "
invite = "一块吃个饭吧 "
print(names[2] + " 不能赴约")
names[2] = "xiaoli"




print("找到了个更大的餐桌")

names.insert(0,"xiaolin")
names.insert(2,"xiaozhang")
names.append("xiaodeng")

print(invite + names[0])
print(invite + names[1])
print(invite + names[2])
print(invite + names[3])
print(invite + names[4])




pizza_list = ["香肠披萨","榴莲披萨","芝士披萨"]
for i in pizza_list:
    print("我喜欢" + i)

print("I really love pizza!")

total = 0
for  i in range(1,101):
    total = total + i
print(total)


numbers = []
for num in range(1,101):
     numbers.append(num)

for num in numbers:
    print(num)


print(min(numbers))
print(max(numbers))
print(sum(numbers))



alien_color = "yellow"
if alien_color == "green":
    print("You got 5 points!")
elif alien_color == "yellow":
    print("You got 10 points!")
else:
    print("You got 15 points!")



friend = {"first_name": "xiaole", "last_name": "chen", "age": 25, "city": "xiamen"}
print("姓名： " + friend["last_name"] + friend["first_name"])
print("年龄：" + str(friend["age"]))
print("城市： " + friend["city"])

rivers = {"Nile": "Egypt", "Yangtze River": "China", "Amazon River": "Brazil"}

# for river, country in rivers.items():
#     print("The " + river + "run through " + country + ".")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

观看到P22结束


