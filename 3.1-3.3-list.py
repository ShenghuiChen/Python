
names = ["xiaoyu", 'xiaochen','xiaozeng']
invite = "一块吃个饭吧？ "
invite = "一块吃个饭吧 "
invite = "一块吃个饭吧 "
# print(names[2] + " 不能赴约")
# names[2] = "xiaoli"




# print("找到了个更大的餐桌")

names.insert(0,"xiaolin")
names.insert(2,"xiaozhang")
names.append("xiaodeng")

# print(invite + names[0])
# print(invite + names[1])
# print(invite + names[2])
# print(invite + names[3])
# print(invite + names[4])




pizza_list = ["香肠披萨","榴莲披萨","芝士披萨"]
for i in pizza_list:
    print("我喜欢" + i)

print("I really love pizza!")

total = 0
for  i in range(1,101):
    total = total + i
# print(total)


# numbers = []
# for num in range(1,101):
#      numbers.append(num)
#
# for num in numbers:
#     print(num)


# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))



alien_color = "yellow"
if alien_color == "green":
    print("You got 5 points!")
elif alien_color == "yellow":
    print("You got 10 points!")
else:
    print("You got 15 points!")



friend = {"first_name": "xiaole", "last_name": "chen", "age": 25, "city": "xiamen"}
# print("姓名： " + friend["last_name"] + friend["first_name"])
# print("年龄：" + str(friend["age"]))
# print("城市： " + friend["city"])

rivers = {"Nile": "Egypt", "Yangtze River": "China", "Amazon River": "Brazil"}

# for river, country in rivers.items():
#     print("The " + river + "run through " + country + ".")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)




# number= int(input("请输入一个数字： "))
# if number % 10 == 0:
#     print("您输入的数字是10的倍数")



# user_input = input("请输入您想要添加的披萨配料： ")
# while user_input != "quit":
#     print("好的， 披萨里会为您添加" + user_input)
#     user_input = input("请输入您想要添加的披萨配料： ")



# def calculate_sector(central_angle, radius):
#     sector_area = central_angle / 360 * 3.14 * radius ** 2
#     print(f"此扇形面积为： {sector_area}")
#
#
# calculate_sector(160, 30)

# def favorite_book(title):
#     print(f"One of my favorite books is {title}. ")
#
# favorite_book("三体")
#
# print(favorite_book("ss"))


# def city_country(city, country):
#      return f"{city},  {country}"
#
# print(city_country("shenzhen", "zhonguo"))




# class CuteCat:
#     def __init__(self):
#         self.name = "Lambton"
#
# cat1 = CuteCat()
# print(cat1.name)


class CuteCat:
    def __init__(self,cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
    def speak(self):
        print("喵" * self.age)
    def think(self, content):
        print(f"小猫{self.name}在思考{content}。。")


cat1 = CuteCat("Jojo", '2', "yellow")
# print(f"小猫{cat1.name}的年龄是{cat1.age}岁， 花色是{cat1.color}")
#
# cat1.think("现在去抓沙发还是去撕纸箱")



class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"餐厅名： {self.restaurant_name}")
        print(f"菜系： {self.cuisine_type}")

    def open_restaurant(self):
        print("餐厅正在营业")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_bumber_served(self, increment_number):
        # self.number_served = self.number_served + increment_number 或者使用下面写法 +=
        self.number_served  += increment_number



taotaoju = Restaurant("陶陶居", "粤菜")
print(taotaoju.restaurant_name)
print(taotaoju.number_served)

print(taotaoju.cuisine_type)
taotaoju.describe_restaurant()
taotaoju.open_restaurant()

taotaoju.set_number_served(500)
taotaoju.increment_bumber_served(20)
print(taotaoju.number_served)

class IceCreamStand(Restaurant):  #Restaurant继承父类
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, "甜品") #super()调用父类方法
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)

so_sweet = IceCreamStand("So Sweet", ["香蕉", "草莓", "哈密瓜", "开心果"])
so_sweet.describe_restaurant()
so_sweet.show_flavors()

























