# 读取文件

from pathlib import Path
path = Path("./learning_python.txt")
content = path.read_text()
print(content)

lines = content.splitlines()
print(lines)

for line in lines:
    print(line)

# with open("./成绩.txt", 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         pass # 计算平均成绩





# 写入文件

# from pathlib import Path
# path = Path("./data.txt")
# path.write_text("Hello\nYoooo")
# print(path)


from pathlib import Path

names = ""
user_input= input("请输入访客的名字（完成所有名字输入后，请输入q终止程序）：")
while user_input != "q":
    names += user_input + "\n"
    user_input = input("请输入访客的名字（完成所有名字输入后，请输入q终止程序）：")

path = Path("./guest_book.txt")
path.write_text(names)


# user_input1 = input("请输入第一个数字： ")
# user_input2 = input("请输入第二个数字： ")
# try:
#     result = int(user_input1) + int(user_input2)
# except ValueError:
#     print("请输入合理的数字。")
# else:
#     print(result)


