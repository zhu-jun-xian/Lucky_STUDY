#全部读取
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

#逐行读取
file_name = "pi_digits.txt"
with open(file_name) as file_object2:
    for line in file_object2:
        print(line.rstrip())

#存进列表
file_name = "pi_digits.txt"
with open(file_name) as file_object2:
    lines = file_object2.readlines()
for line in lines:
    print(line.rstrip())

#读进字符串
pstring = ''
file_name = "pi_digits.txt"
with open(file_name) as file_object2:
    lines = file_object2.readlines()
for line in lines:
    print(line.rstrip())
    pstring += line.strip()
print(pstring)
print(len(pstring))

#写入文件
file_path = 'test.txt'
with open(file_path,'w') as file_project:
    file_project.write("sdgyugyudsguiudscgudcsguiusdguisdugidsgui\n")
    file_project.write("guudhvdhugghduighudshguddhguhdsughudhguidshguihdug\n")
with open(file_path,'a') as file_project:
    file_project.write("456565615211245654545545645646456456456\n")
    file_project.write("guudhvdhugghduighudshguddhguhdsughudhguidshguihdug\n")

#异常
try:
    print(5/0)
except ZeroDivisionError:
    print("you can not divide by zero")

#使用json保存数据
import json
number = [2,5,5,45,5,8]
with open('number.json','w') as f:
    json.dump(number,f)

numbers = []
with open('number.json') as f1 :
    numbers = json.load(f1)
print(numbers)