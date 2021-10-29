
#大小写
# name = "zhujnXIAN"
# print(name.upper())
# print(name.lower())

#f字符串花括号内对象替换
#python版本 >3.6
# firstName = "朱"
# lastName = "均贤"
# print(f"{firstName}{lastName}""是傻逼") 
# #python版本 <3.6
# print("{}{}""是傻逼".format(firstName,lastName)) 

#删除空白
# name = "      pyhton     "
# print(name)
# #删除末尾空白
# print(name.rstrip())
# #删除开头空白
# print(name.lstrip())
# print((name.rstrip()).lstrip())
# #删除两边空白
# print(name.strip())

#除法永远都是浮点数
# i = 6 / 2  # = 3.0
# print(i)

# #python的数组叫列表 按照特定顺序排列
# bicycles = ["trek","cannomndale",'redline']
# print(bicycles[0])#trek
# #使用
# message = f"{bicycles[0].title()}"
# print(message)
# #修改
# bicycles[0] = '火车'
# message = f"{bicycles[0].title()}"
# print(message)
# #添加
# bicycles.append('nicai')
# print(bicycles)
# #插入
# bicycles.insert(0,"huizij")
# print(bicycles)
# #删除 del需要知道下标位置
# del bicycles[0]
# print(bicycles)
# #pop 不仅可以删除，还可以继续使用
# print(bicycles)
# last = bicycles.pop()
# print(last)
# print(bicycles)
# bicycles.remove("redline")
# print(bicycles)
# #添加
# bicycles.append('aaa')
# bicycles.append('gaa')
# bicycles.append('Haa')
# bicycles.append('自己')
# #sort 排序，按字母 先大写，再小写，再拼音 永久排序
# bicycles.sort()
# print(bicycles)
# #sort 逆序
# bicycles.sort(reverse=True)
# print(bicycles)
# #临时排序 sorted()
# print(bicycles)
# print(sorted(bicycles))
# print(bicycles)
# #reverse 逆序
# bicycles.reverse()
# print(bicycles)
# #长度
# print(len(bicycles))
# #循环打印
# for i in bicycles:
#     print(i)

#创建数值列表 range
#顺序生成1到99
# for i in range(1,100):
#     print(i)
# #list可将range的结果转为列表
# num = list(range(1,5))
# print(num)
# #python中**表示乘方
# num1 = []
# for i in range(0,25):
#     num1.append(i**2)
# print(num1)
# #统计
# print(min(num1))
# print(max(num1))
# print(sum(num1))
# #切割列表
# print(num1[5:9])
# #开头->
# print(num1[:9])
# #结束->
# print(num1[9:])
# #后三->
# print(num1[-3:])
# #复制列表
# num2 = num1[:]
# print(num2)
# #列表是随时可以改的
# #而元组不可以，是不可变的列表
# tuples1 = (1,2,3,4,5)
# for i in tuples1:
#     print(i)
# #tuples1是元组变量 (1,2,3,4,5)是元组  元组不可变 但元组变量可变
# tuples1 = ("hhhHHH",8,"绘画",6,"gghh")
# for i in tuples1:
#     print(i)
# #每次缩进四个空格

#if条件
# cars = ["audi",'bmw','subaru']
# for car in cars:
#     if car == "bmw": 
#         print(car.upper())
#     else:
#         print(car.title().lower())

# #if 处理列表
# request_toppings = ["mushroom",'green peppers','extra cheese']
# for request_topping in request_toppings:
#     print(request_topping)

# #字典
# alien_0 = {'color':'green','point':5}
# print(alien_0['color'])
# print(alien_0['point'])
# #字典是一种动态结构，可随意添加键值对
# alien_0["x"] = 252
# alien_0["y"] = 123
# print(alien_0)
# #三种结构 list[]列表 turpes()元组  {}字典
# #删除字典对 del
# del alien_0['x']
# print(alien_0)
# #print(alien_0['x']) 会出现键值对的错误
# #get()第一参数用来指定键 第二个参数用来指定参数没有时返回的数 如果没有第二个参数，将返回None,None并非错误
# print(alien_0.get('x','no point'))
# #遍历字典
# for key,value in alien_0.items():
#     print(f"\nkey:{key}")
#     print(f"value:{value}")
# #遍历所有键
# for key in alien_0.keys():
#     print(key.title())
# #按顺序遍历所有键
# for key in sorted(alien_0.keys()):
#     print(f"{key.title()}")
# #遍历所有值
# for value in alien_0.values():
#     print(f"{value}")
#  #   print(value.title()) 不可以，奇怪？
#  #集合set可以剔除重复值 对有重复值的列表调用set方法，会剔除重复后创建一个集合
# for v in set(alien_0.values()):
#     print(v)

#创建一个存储外星人的列表
# aliens = []
# #创建30个绿色的外星人
# for alien in range(30):
#     new_alien = {'color':'green','point':5,'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)

#函数input
# message = input("tell me something")
# print(message)

# name = input("\nplease input your name\n")
# print(name)

#多行字符串
# name = "军衔"
# name += "zhu"
# print(name)
# #使用函数input 会将用户输入解读为字符串 函数int()会将输入解读为数字
# age = input("how old are you")
# age = int(age)
# if age > 16:
#     print("大树")
# else:
#     print("号年轻")
#while 循环
# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1
# #检查用户输入退出标志
# message = ""
# while message != 'quit' :
#     message = input()
#     print(message)

#使用标志
# active = True
# while(active):
#     message = input()
#     if(message == 'quit'):
#         active = False
#     else:
#         print(message)

# #break退出循环
# while True:
#     message = input()
#     if(message == 'quit'):
#         break
#     else:
#         print(message)

#循环中continue continue会重头开始执行代码 break会退出
# current = 0
# while current <= 10:
#     current += 1
#     if(current % 2 == 0):
#         continue
#     print(current)


# unconfirmed_used = ['alien','brien','canda']
# confirmed_used   = []
# while unconfirmed_used:
#     current_user = unconfirmed_used.pop()
#     print(f"verifying{current_user.title()}")
#     confirmed_used.append(current_user)
# for confirm in confirmed_used:
#     print(confirm.title())

# #remove删除列表元素 只能删除在列表中出现一次的元素
# pets = ['cat','dog','mouse','cat']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# #使用用户输入来填充字典
# responses = {}
# active = True
# while active:
#     name = input('name:')
#     response = input('response:')
#     responses[name] = response
#     repeat = input('y/n')
#     if(repeat == 'n' or repeat == 'N'):
#         active = False
# for n,r in responses.items():
#     print(f"{n}：{r}")

#函数
# def greet_user(username):
#     print(f"hello,{username.title()}")

# greet_user("诸郡县")

# #位置实参
# def describe_pet(animal_type,pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"\nMy {animal_type} is a {pet_name}")

# describe_pet('hamster','harry')

# #关键字实参
# def describe_pet(animal_type,pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"\nMy {animal_type} is a {pet_name}")

# describe_pet(animal_type = 'hamster',pet_name = 'harry')

# #默认值
# def describe_pet(pet_name,animal_type = 'dog'):
#     print(f"\nI have a {animal_type}")
#     print(f"\nMy {animal_type} is a {pet_name}")

# describe_pet(pet_name = 'harry')

# #返回值
# def get_formatted_name(first_name,last_name):
#     full_name = f"{first_name}{last_name}"
#     return full_name.title()

# print(get_formatted_name('zhu',' junxian'))

# #让实参变为可选的
# def get_formatted_name(first_name,last_name,middle_name = ''):
#     if middle_name:
#         full_name = f"{first_name}{middle_name}{last_name}"
#     else:
#         full_name = f'{first_name}{last_name}'
#     return full_name.title()
# print(get_formatted_name('zhu',' junxian'))

# #返回字典
# def build_person(first_name,last_name):
#     person = {'first':first_name,'last':last_name}
#     return person

# print(build_person('zhu','lkj'))

#返回字典
# def build_person(first_name,last_name,age = None):
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# print(build_person('zhu','lkj',age = 45)) 
# print(build_person('zhu','lkj'))

# def greet_user(names):
#     for name in names:
#         msg = f"hello,{name.title()}"
#         print(msg)
# usernames = ['hannah','ty','margot']
# greet_user(usernames)
# #函数中修改列表
# unprintf = ['phone case','rebot','robot']
# compile = []
# while unprintf:
#     current = unprintf.pop()
#     print(current)
#     compile.append(current)
# print(compile)
# #利用传递副本方式 禁止函数修改列表
# #切片表示法[:]可以创建列表

# #形参名*topping,将所有值放进空元组
# def make_Pizza(*topping):
#     print('\nmaking a pizza')
#     for top in topping:
#         print(f'-{top}')

# make_Pizza('zxc','xcv','cvb','xcvbn')

# #结合位置实参和任意数量实参
# def make_Pizza(size,*topping):
#     print(f'\nmaking {size} pizza')
#     for top in topping:
#         print(f'-{top}')

# make_Pizza(16,'zxc','xcv','cvb','xcvbn')

#fail#user_info 创建一个名为user_info的空字典，并将收到的所有键值对都放进字典
# def build_profile(first,last,**user_info):
#     user_info['fiest_name'] = first
#     user_info['last_name']  = last
#     return user_info

# user = build_profile['zhu','junxian',localsad = 'dgg']
# print(user)

#导入整个文件
# import pizza
# pizza.make_Pizza(16,'as')

# #导入模块
# from pizza import make_Pizza
# make_Pizza(16,'zchi','sfds')

# #首字母大写的就是类 _init_() 默认的方法格式 创建类的调用它
# class Dog:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(f"{self.name} is sitting now")

#     def roll(self):
#         print(f"{self.name} rolled over !")

# #创建实例
# my_dog = Dog("PETER",6)
# my_dog.sit()
# my_dog.roll()

# #编写Car 类
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odmeter = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year}{self.make}{self.model}"
#         return long_name.title()
#     def read_odmeter(self):
#         print(f"this car has {self.odmeter} miles on it")
#     def update_odmeter(self,mileage):
#         self.odmeter = mileage
#     def increment_odmeter(self,miles):
#         self.odmeter += miles
# #创建实例
# my_car = Car('奔驰','a4',2014)
# print(my_car.get_descriptive_name())
# #直接修改属性值
# my_car.odmeter = 456
# my_car.read_odmeter()
# #通过方法修改值
# my_car.update_odmeter(5556)
# my_car.read_odmeter()
# #通过方法
# my_car.increment_odmeter(456)
# my_car.read_odmeter()

# #继承
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = 75
#     def get_battery_info(self):
#         print(f"battery:{self.battery}")
#     def update_odmeter(self, mileage):
#         self.odmeter = mileage
#         print(f"overload fun is {self.odmeter}")

# my_tesla = ElectricCar('tesla','model s',2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.get_battery_info()
# my_tesla.update_odmeter(123)

#实例用作属性
class Battery:
    def __init__(self,battery = 75):
        self.battery = battery
    def print_info(self):
        print(f"battery:{self.battery}")

class ElectricCar:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        self.battery = Battery()

car = ElectricCar('cvb','zxc')
car.battery.print_info()