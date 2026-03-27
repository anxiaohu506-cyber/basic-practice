'''
print("hello world")
message = "你好python"\变量
print(message)
message = "你好世界"
print(message)
name = "xiao hu an"
print(name.title())\首字母大写方法
print(name.upper())\全大写方法
print(name.lower())\全小写方法
first_name = "xiaohu"
last_name = " an"
full_name = f"{first_name}{last_name}"\f字符串（设置格式）
print(full_name.title())
print(f"Hello,{full_name.title()}!")
print("Hello world")
print("\tHello world")
print("Languages:\n\tc\n\tpython\n\tjava")\（\t制表符 \n换行符）
'''

#practice2.3:
'''
name = "Eric"
print(f"Hello {name},would you like to learn some Python today?")
'''
#practice2.4:
'''
name_01 = "xiaohu an"
print(name_01.lower()) #quan xiaoxie
print(name_01.upper()) #quan daxie
print(name_01.title()) #shou daxie
'''
#practice2.5:
'''
famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new."'
print(f"{famous_person} once said,{message}")
'''
#practice2.6:同上
#practice2.7:
'''
name_02 = "           anxiaohu                            "
print(f"\n\t{name_02}")
print(name_02.lstrip())
print(name_02.rstrip())
print(name_02.strip())
'''
#practice2.8:
'''
filename = 'python_notes.txt'
print(filename.removesuffix('.txt')) （去后缀）
print(filename.removeprefix('py')) （去前缀）
print(filename.removesuffix('.txt').removeprefix('pyth'))
'''
#practice2.9:
'''
print(5 + 3)
print(9 - 1)
print(2 * 4)
print(16 // 2) #地板除，向下取整
print(int(16 / 2)) #截断小数
'''
#practice2.10:
'''
num = 9
message = '我最喜欢的数字是：'
print(f"{message}{num}") #f字符串拼接术
'''

#import this （python之禅）
##list章节相关内容如下:

#第三章：
#列表形式如下：
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized',]
print(bicycles)
#访问列表元素例如:
print(bicycles[0])
print(bicycles[1].title())
#使用列表中的各个值:
name = 'an xiaohu'
message = f"{name.title()} have a {bicycles[1]}"
#使用-1可以访问列表最后一个值，-2则是倒数第二个...
print(message)
'''
#practice3.1:
'''
name = ['安小虎', '郭旭', '马会国', '丁生清', '岳振芳']
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
'''
#practice3.2:
'''
message = 'nice to meet you!'
print(f"{name[0]},{message}")
print(f"{name[1]},{message}")
print(f"{name[2]},{message}")
print(f"{name[3]},{message}")
print(f"{name[4]},{message}")
'''
#practice3.3:
'''
commute = ['walk', 'bicycle', 'motorcycle', 'car', 'fly']
w = 'very tired！'
b = 'a little bit tired!'
m = 'a little tired!'
c = 'not tired!'
f = 'unkown!'
print(f"{commute[0]} is {w}")
print(f"{commute[1]} is {b}")
print(f"{commute[2]} is {m}")
print(f"{commute[3]} is {c}")
print(f"{commute[4]} is {f}")
'''
#修改，添加，删除列表元素：
'''
commute = ['walk', 'bicycle', 'motorcycle', 'car']
commute[1] = 'fly' #修改
print(commute)

commute = ['walk', 'bicycle', 'motorcycle', 'car']
commute.append('fly') #末尾添加（append方法）
print(commute)
commute.insert(2, 'fly') #在任意位置插入（insert方法）
print(commute)

#如果知道要删除的元素在列表中的位置，使用del语句【按照索引删除】，不可以继续使用它的值：
commute = ['walk', 'bicycle', 'motorcycle', 'car']
del commute[2]
print(commute)
#使用【pop】方法删除元素，删除末尾元素（本质是从列表弹出）,可以继续使用它的值
commute = ['walk', 'bicycle', 'motorcycle', 'car']
poped_commute = commute.pop() #弹出末尾的值，赋值给新变量
print(commute) #打印原变量，实现删除
print(poped_commute) #打印新变量（弹出的值），此方法删除的值依然能够被访问
#使用pop方法也可以删除列表中任意位置的元素，指定索引即可
commute = ['walk', 'bicycle', 'motorcycle', 'car']
poped1_commute = commute.pop(0)
print(poped1_commute)
#如果只知道要删除元素的值，可使用remove方法，可以继续使用它的值
commute = ['walk', 'bicycle', 'motorcycle', 'car']
commute.remove('bicycle') #删除
print(commute)
commute = ['walk', 'bicycle', 'motorcycle', 'car']
d_commute = 'bicycle' #可以通过新变量来访问
commute.remove('bicycle')
print(d_commute) #可以通过新变量来访问
'''
#practice3.4:
'''
person = ['哥德尔', '希尔伯特', '王浩']
message = '来一起共进晚餐！'
print(f"{person[0]},{person[1]},{person[2]},{message}")
'''
#practice3.5:
'''
person = ['哥德尔', '希尔伯特', '王浩']
message = '来一起共进晚餐'
print(f"{person[0]},{person[1]},{person[2]},{message}")
print(f"{person[1]}无法赴约!")
del person[1] #删除1
person.insert(1, '塔斯基') #在删除的位置添加新的人名
print(f"{person[0]},{person[1]},{person[2]},{message}")
'''
#practice3.6:
'''
person = ['哥德尔', '希尔伯特', '王浩']
message = '来一起共进晚餐！'
print(f"{person[0]},{person[1]},{person[2]},{message}")
print('我找到了一张更大的餐桌!')
person.insert(0, '爱因斯坦')
person.insert(2, '普朗克')
person.append('杨振宁')
print(f"{person[0]},{person[1]},{person[2]},{person[3]},{person[4]},{person[5]}{message}")
'''
#practice3.7:
'''
person = ['哥德尔', '希尔伯特', '王浩']
message = '来一起共进晚餐！'
print(f"{person[0]},{person[1]},{person[2]},{message}")
print('我找到了一张更大的餐桌!')
person.insert(0, '爱因斯坦')
person.insert(2, '普朗克')
person.append('杨振宁')
print(f"{person[0]},{person[1]},{person[2]},{person[3]},{person[4]},{person[5]}{message}")
print('桌子不够，只能请两个人了')
poped1_person = person.pop()
print(f"{poped1_person},sorry")
poped2_person = person.pop()
print(f"{poped2_person},sorry")
poped3_person = person.pop()
print(f"{poped3_person},sorry")
poped4_person = person.pop()
print(f"{poped4_person},sorry")
message = '你可以来'
print(f"{person[0]}{message}")
print(f"{person[1]}{message}")
del person[1] #亦可删除0，再删除0
del person[0] #连续使用del删除需注意索引会变！
print(person)
'''
'''
#使用sort（）【方法】对列表进行【永久排序】（首字母表排序）
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #原序
cars.sort() #字母序
print(cars)
#使用sort（）[方法]也可以按字母表序反方向排序
cars.sort(reverse=True) #反字母序
print(cars)
#使用sorted（）【函数】对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
#反向打印列表reverse()[方法]
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
#使用len（）函数获取列表长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
'''
#practice3.8
'''
location = [')china', 'america', 'france', 'britain', 'norway']
print(location)
print(sorted(location))
print(location)
location_01 = sorted(location, reverse = True)
print(location_01)
print(location)
location.reverse()
print(location)
location.reverse()
print(location)
location.sort()
print(location)
location.sort(reverse = True)
print(location)
'''
#practice3.9
'''
person = ['哥德尔', '希尔伯特', '王浩']
message = '来一起共进晚餐'
print(f"{person[0]},{person[1]},{person[2]},{message}")
num = len(person)
print(f"共邀请了{num}个人来参加晚宴！")
'''
#practice3.10
'''
ultraman = ['tiga', 'taylor', 'jack', 'father of ultra', 'gaia']
ul01 = sorted(ultraman)
print(ul01)
num = len(ultraman)
print(num)
'''
#方法，有点，多半会改动原数据；函数，没点，多半不会改动原数据

#第四章、操作列表：
'''
#遍历。for循环，循环赋值打印：(可对每个元素执行众多不同的操作)
nums = ['alice', 'david', 'carolina']
for num in nums: #for循环
    print(f"{num.title()},that was a great trick!")
    print(f"I cant't wait to see your next trick, {num.title()}.\n")
print('Thank you! everyone. That was a great magic show!')
'''
#practice4.1:
'''
pizzas = ['classic margherita', 'supreme', 'hawaiian']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza！")
print(f" {pizzas[0]} taste good! \n {pizzas[1]} taste no good! \n {pizzas[2]} taste very good！\n I really love pizza!")
'''
#practice4.2:
'''
animals = ['bull', 'sheep', 'chicken']
for animal in animals:
    print(animal)
for animal in animals:
    print(f"{animal} is delicious")
print('these animals are delicious!')
'''
#range()函数：生成数:
'''
for a in range(1, 5) : #range函数从1开始数，到5停止（1，2，3，4）（不含5）
    print(a)
for b in range(5): #从0开始数5个数字
    print(b)
'''
#使用range（）创建数值列表:
'''
numbers = list(range(0, 10, 2)) #第一个参数代表从0开始，第二个参数代表到10停止（不包括10），第三个参数代表步长为2
print(numbers)

#示例：创建一个列表，其中包含前十个整数的平方：
squares = [] #创建一个空列表
for value in range(1, 11): #遍历1~10的值
    square = value ** 2 #在循环中计算乘方【可以不用新变量，用等号后面的计算直接代替下一行（）中的变量】
    squares.append(square) #把得到的平方值加入列表
print(squares)

#几个函数：min（列表变量）；max（列表变量）；sum（列表变量）
#列表推导式：列表推导式将for循环和创建新元素的代码合并成一行，并自动追加新元素。
#使用列表推导式创建前面的平方数列表：
squares = [value ** 2 for value in range(1, 11)]
print(squares)
'''
#practice4.3:
'''
num = range(1, 21)
for num_ in num:
    print(num_)
'''
#practice4.4:
'''
num = list(range(1, 1000001))
for num_ in num:
    print(num_)
'''
#practice4.5:
'''
num = list(range(1, 1000001))
print(f"最小值：{min(num)}")
print(f"最大值：{max(num)}")
print(f"求和：{sum(num)}")
'''
#practice4.6:
'''
num_01 = list(range(1, 20, 2))
for num in num_01:
    print(num)
'''
#practice4.7:
'''
num = list(range(3, 30, 3))
for num_01 in num:
    print(num_01)
'''
#practice4.8:
'''
num0 = []
for num_ in range(1, 11):
    num = num_ ** 3
    num0.append(num)
for num1 in num0:
    print(num1)
'''
#practice4.9:
'''
num = [num0 ** 3 for num0 in range(1, 11)] #列表推导式
print(num)
'''

#切片打印
'''
num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(num[0:3]) #从0开始3为止(不包括3)
print(num[3:]) #从3开始到最后
print(num[2:6]) #从2开始到6为止（不包括6）
print(num[-3:]) #后三个
print(num[6:]) #从6开始
'''
#遍历切片 在for循环中使用切片
'''
num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for num0 in num[2:6]:
    print(num0.title())
'''
#复制列表(使用切片)
'''
num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
num0 = num[:]
num.insert(0, '0')
print(num)
num0.insert(0, '1')
print(num0)
#不用切片复制列表【num0 = num】只是将两个不同的变量指向了同一个列表
'''
#practice4.10:
'''
num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
message1 = 'The first three items in the list are:'
message2 = 'Three items from the middle of the list are:'
message3 = 'The last three items in the last are:'
num0 = num[0:3]
num1 = num[3:6]
num2 = num[6:]
print(f"{message1}{num0}")
print(f"{message2}{num1}")
print(f"{message3}{num2}")
'''
#practice4.11:
'''
pizzas = ['classic margherita', 'supreme', 'hawaiian']
pizzas0 = pizzas[:]
pizzas.append('new')
pizzas0.append('new0')
message = 'My favorite pizzas are:'
for pizza in pizzas:
    print(f"{message}{pizza}")
message0 = "My friend's favorite pizzas are:"
for pizza0 in pizzas0:
    print(f"{message0}{pizza0}")
'''
#practice4.12:与上题类似，略

#元组（不可变的列表（值不能修改））  使用（）括号或者不使用，因为元组是用逗号标识的
#元组的遍历和列表一样（for循环）
'''
dimensions = 200, 50
print(dimensions[0])
print(dimensions[1])
#修改元组变量（不能修改元组的元素，但可以给表示元组的变量赋新值）
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
'''
#practice4.13:
'''
foods = '炸酱面', '新疆炒米粉', '潮汕牛肉', '兰州牛肉面', '牛排'
for food in foods:
    print(food)
#foods[0] = '矿泉水'
#print(foods)
foods = '炸酱面', '新疆炒米粉', '潮汕牛肉', '拉面', '矿泉水'
for food in foods:
    print(food)
'''

#第五章 if语句
#简单示例：
'''
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw': #“==”可以看作“是吗？”
        print(car.upper())
    else:
        print(car.title())
'''
#每条if语句的核心都是一个值为true或者false的表达式，称为条件测试
#在python中检查是否相等是区分大小写的
#如果要检查两个值是否不等，可使用不等运算符（！=）

#使用and与or检查多个条件，例如：
'''
age_0 = 32
age_1 = 18
#检查两个人是否都不小于21岁
if age_0 >= 21 and age_1 >= 21: #and需要都满足才能通过测试
    print('yes')
else:
    print('no')
#检查至少有一个人的年龄不小于21岁
if age_0 >= 21 or age_1  >= 21: #or只需要满足一个条件就能通过测试
    print('yes')
else:
    print('no')
'''
#检查特定的值是否在（或不在）列表中，使用关键字in（或not in）
'''
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 800 not in num:
    print('yes')
else:
    print('no')
'''
#practice5.1:
'''
subaru = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
'''
#practice5.2:
'''
a = 'snegUBOBfugor'
b = 'itjlklpjpuiboIBKsblib'
print(a == b)
print(a != b)

print(a.lower() == b.lower())
print(a.lower() != b.lower())

num0 = 54355
num1 = 268461
num2 = 54
num3 = 54
print(num2 == num3) #相等？true
print(num0 == num1) #相等？false
print(num0 != num1) #不等？true
print(num2 != num3) ##不等？false
print(num1 > num2) #大于？true
print(num3 > num1) #大于？false
print(num3 < num0) #小于？true
print(num2 < num3) #小于？false
print(num1 >= num2) #大于等于？true
print(num0 >= num1) #大于等于？false
print(num3 <= num1) #小于等于？true
print(num0 <= num3) #小于等于？false

num0 = 10
num1 = 10
num2 = 23
print(num0 == num1 and num2 > num1) #输出true
print(num1 < num2 and num0 == num2) #输出false
print(num0 == num1 or num2 > num1) #输出true
print(num1 > num2 or num0 > num2) #输出false

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(12 in nums)
print(1 in nums)
'''

#简单的if语句
'''
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
'''
#if-else
'''
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("go out!")
'''
#if-elif-else
'''
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 25
else:
    price = 40
print(f"Your adminssion cost is ${price}")
'''
#使用多个elif代码块。根据需要使用任意数量的elif代码块
'''
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")
'''
#python并【不】要求if-elif结构后面必须有else代码块。
#测试多个条件（示例如下：）[同时检查，互不影响]
'''
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms!')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print("\nFinished making your pizza!")
'''
#practice5.3:
'''
alien_color = 'green'
if alien_color == 'green':
    print("获得5分")

alien_color = 'green'
if alien_color == 'red':
    print("获得5分")
'''
#practice5.4:
'''
alien_color = 'red'
if alien_color == 'green':
    print("获得5分")
else:
    print("获得10分")

alien_color = 'green'
if alien_color == 'green':
    print("获得5分")
else:
    print("获得10分")
'''
#practice5.5:
'''
alien_color = 'red'
if alien_color == 'green':
    print('获得5分')
elif alien_color == 'yellow':
    print('获得10分')
elif alien_color == 'red':
    print('获得15分')
else:
    print('NO')

alien_color = 'red'
if alien_color == 'red':
    print('YES')
elif alien_color == 'yellow':
    print()
elif alien_color == 'green':
    print()
else:
    print()

alien_color = 'green'
if alien_color == 'green':
    print('YES')
elif alien_color == 'yellow':
    print()
elif alien_color == 'red':
    print()
else:
    print()

alien_color = 'yellow'
if alien_color == 'yellow':
    print('YES')
elif alien_color == 'green':
    print()
elif alien_color == 'red':
    print()
else:
    print()
'''
#practice5.6:
'''
age = int(input("请输入："))
if age < 2:
    print('婴儿')
elif age < 4:
    print('幼儿')
elif age < 13:
    print('儿童')
elif age < 18:
    print('少年')
elif age < 65:
    print('中青年人')
else:
    print('老年人')
'''
#practice5.7:
'''
favorrite_fruits = ['apple', 'orange', 'banana']
if 'apple' in favorrite_fruits:
    print('You really like apple')
if 'orange' in favorrite_fruits:
    print('You really like orange')
if 'banana' in favorrite_fruits:
    print('You really like banana')
if 'a' not in favorrite_fruits:
    print('no')
if 'b' not in favorrite_fruits:
    print('no')
'''
#使用if语句处理列表
#检查特殊元素
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now!')
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")
'''
#在运行for循环前确定列表非空
'''
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
'''
#使用多个列表(示例)
'''
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we are out of {requested_topping}")
print("\nFinished making your pizza!")
'''
#practice5.8:
'''
names = ['a', 'b', 'c', 'd', 'admin']
for name in names: #遍历names中的元素
    if name == 'admin': #如果元素的值等于‘admin’则打印如下消息
        print("Hello admin, would yuo like to see a status report?")
    else: #否则打印如下
        print("禁止访问！")
'''
#practice5.9:
'''
names = ['a', 'b', 'c', 'd', 'admin']
if names: #确认列表是否为空，如果不空则执行下述for循环
    for name in names:
        if name == 'admin':
            print("Hello admin, would yuo like to see a status report?")
        else:
            print("禁止访问！")
else: #如果为空（否则）执行else代码块
    print("We need to find some users")
'''
#practice5.10:
'''
current_users = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'] #列表1
new_users = ['a', 1, 'B', 66, 'e'] #列表2
current_users0 = [] #创建空列表
for current_user in current_users: #遍历列表1的元素
    current_users0.append(current_user.upper()) #把列表1的大写添加进空列表，这样就得到了一个列表1的大写副本

for users in new_users: #遍历列表2的元素
    if users in current_users: #如果其中元素在列表1里
        print("已使用") #打印
    elif users in current_users0: #如果其中元素在列表1的大写副本里，打印
        print("已使用")
    else: #否则，打印
        print("未使用")
'''
#practice5.11:
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
'''

#第六章：字典
#简单示例：
'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) #访问字典中的值
print(alien_0['points']) #访问字典中的值
'''
#在python中，字典是一系列键值对。每个键都与一个值关联，可以使用键来访问与之关联的值。（可以将任意python对象用作字典中的值）
#用{}表示
#访问字典中的值
'''
alien = {'color': 'green', 'points': 5}
new_points = alien['points']
print(alien['color'])
print(new_points)
'''
#添加键值对：
'''
alien = {'color': 'green', 'points': 5}
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)
'''
#创建空字典然后添加：
'''
alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien)
'''
#修改字典中的值：
'''
alien = {'color': 'green', 'points': 5}
print(alien)
alien['color'] = 'red'
print(alien)
'''
#一个例子[外星人]：
'''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} #创建外星人数据
print(f"Originl position: {alien_0['x_position']}") #打印初始x坐标
if alien_0['speed'] == 'slow': #如果速度为slow
    x_increment = 1 #向右移动一个单位
elif alien_0['speed'] == 'medium': #如果速度为medium
    x_increment = 2 #向右移动2个单位
else: #否则
    x_increment = 3 #向右移动3个单位
alien_0['x_position'] = alien_0['x_position'] + x_increment #把字典中的值与移动值相加
print(f"New position: {alien_0['x_position']}")
'''
#删除键值对（del语句[指定字典名和要删除的值]）
'''
alien_0 = {'color':'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
'''
#使用get()来访问
#使用get（）方法在指定的键不存在时返回一个默认值。
#get方法的第一个参数用于指定键（必不可少），第二个参数为当指定的键不存在时要返回的值（可选）（如无则返回none）
'''
alien_0 = {'color':'green', 'points': 5}
value = alien_0.get('c', )
print(value)
'''
#practice6.1:
'''
people = {'name1':'xiaohu', 'name2':'an', 'age':18, 'city':'cq'}
print(people['name1'])
print(people['name2'])
print(people['age'])
print(people['city'])
'''
#practice6.2:
'''
love_num = {'a':5, 'b':9, 'c':5555, 'd':80, 'e':6}
print(f"a喜欢{love_num['a']}")
print(f"b喜欢{love_num['b']}")
print(f"c喜欢{love_num['c']}")
print(f"d喜欢{love_num['d']}")
print(f"e喜欢{love_num['e']}")
'''
#practice6.3:
'''
py = {'列表':'第三章', '元组':'第四章', '字符串':'第二章', '变量':'第一章', '方法':'第二章'}
print(f"列表在{py['列表']}")
print(f"元组在{py['元组']}")
print(f"字符串在{py['字符串']}")
print(f"变量在{py['变量']}")
print(f"方法在{py['方法']}")
'''
#遍历字典（for循环）
#遍历所有键值对：
'''
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items(): #【items()方法返回一个键值对列表】
    print(f"\nkey: {key}")
    print(f"value: {value}")
'''
#遍历字典中的所有键：在不使用字典中的值时，使用keys（）方法.【或者不用，会默认遍历所有的键】
'''
favorite_languages = {
    'a': 'python',
    'b': 'c',
    'c': 'rust',
    'd': 'c++'
}
for name in favorite_languages.keys():
    print(name.title())
'''
'''
favorite_languages = {
    'a': 'python',
    'b': 'c',
    'c': 'rust',
    'd': 'c++'
} #创建一个字典
friends = ['b', 'sarsh'] #创建一个列表
for name in favorite_languages.keys(): #for循环遍历字典中的键（name）（key方法可不用）
    print(f"Hi {name.title()}.") #打印
    if name in friends: #如果字典中的键（name）在列表中
        language = favorite_languages[name].title() #则将其【值】的大写（name）赋值给language
        print(f"\t{name.title()},I see you love {language}") #打印
'''
#按[特定顺序]遍历字典中的所有键。使用sorted函数
'''
favorite_languages = {
    'jen': 'python',
    'sarsh': 'c',
    'edward': 'rust',
    'phil': 'python'
}
for name in sorted(favorite_languages.keys()): 
    #用sorted函数，使得在遍历前获得字典中的所有键，并在遍历前对这个列表进行排序（临时排序（字母表））
    print(f"{name.title()}, thank you for taking the poll.")
'''
#遍历字典中的所有值,使用[values（）方法]，会返回一个值列表
'''
favorite_languages = {
    'jen': 'python',
    'sarsh': 'c',
    'edward': 'rust',
    'phil': 'python'
}
print("")
for language in favorite_languages.values(): #values（）方法
    print(language.title())
'''
#如果字典中有重复值时，可用集合：
'''
favorite_languages = {
    'jen': 'python',
    'sarsh': 'c',
    'edward': 'rust',
    'phil': 'python'
}
print("")
for language in set(favorite_languages.values()): 
    #通过将包含重复元素的列表传入set（），使用这些元素来创建一个集合，用set（）提取。从而去掉重复值
    print(language.title())

#可使用一对花括号直接创建集合（无重复无顺序），例如：
a = {'python', 'c', 'c#', 'java', 'python'} #输出无重复
print(a)
'''
#practice6.4:
'''
py = {'列表':'第三章', '元组':'第四章', '字符串':'第二章', '变量':'第一章', '方法':'第二章'}
py['p0'] = 'a' #添加元素
py['p1'] = 'b'
py['p2'] = 'b'
py['p3'] = 'c'
py['p4'] = 'd'
for name, tip in py.items(): #items方法返回一个键值对列表
        print(f"{name}在{tip}")
'''
#practice6.5:
'''
river_country = {
    'nile':'egypt',
    'huanghe':'china',
    'changjiang':'china'
}
for river,country in river_country.items():
    print(f"The {river.title()} runs through {country.title()}.")
print() #空一行
for river in river_country.keys():
    print(river.title())
print() #空一行
for country in river_country.values():
    print(country.title())
'''
#practice6.6:
'''
favorite_languages = {
    'a': 'python',
    'b': 'c',
    'c': 'rust',
    'd': 'c++'
}
for name0 in favorite_languages.keys():
    print(name0.title())
names = ['a', 'An', 'd', 'He', 'Li']
for name1 in names:
    if name1 in favorite_languages:
        print(f"{name1},感谢你参加调查")
    else:
        print(f"{name1},邀请您参加调查")
'''
#嵌套：有时候，需要将多个字典存储在列表中或将列表作为值存储子啊字典中，称为嵌套。
#可在列表中嵌套字典，在字典中嵌套列表，甚至在字典中嵌套字典
'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
'''
#使用range（）生成更多外星人
'''
aliens = [] #创建空列表存储接下来的将要创建的外星人
for alien_number in range(30): #range（）决定循环的次数，30次即创建30个外星人
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #
    aliens.append(new_alien) #每次创建的外星人都添加到末尾
for alien in aliens[:5]: #使用切片打印前5个外星人
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}") #len（）是列表长度，表示创建了30个外星人
'''
#修改某些外星人的数据：例如将前3个外星人修改为黄色，速度中等且值10分
'''
aliens = [] #创建空列表存储接下来的将要创建的外星人
for alien_number in range(30): #range（）决定循环的次数，30次即创建30个外星人
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #
    aliens.append(new_alien) #每次创建的外星人都添加到末尾
for alien in aliens[:3]: #列表切片
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print("...")
'''
#在字典中存储列表:可以使一个键对应多个值
'''
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
'''
#在字典中存储字典：
#例如每个用户的各种信息：用户名为键，其信息如”’真实姓名‘为键，’安小虎‘为值“
'''
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
} #定义一个字典（内嵌套了一个“信息”字典）
for username, user_info in users.items(): #外层字典的键（username）与值（user_info）
    print(f"\nUsername: {username}") #打印外层字典的键（username）——即用户名
    full_name = f"{user_info['first']} {user_info['last']}" #把内层字典的两个键的值合成一个值赋给full_name
    location = user_info['location'] # 把内层字典的最后一个键的值赋给location
    print(f"\tFull name: {full_name.title()}") #打印full_name——即用户第一信息
    print(f"\tLocation: {location.title()}") #打印location——即用户第二信息
'''
#practice6.7:
'''
people_0 = {'name1':'xiaohu', 'name2':'an', 'age':18, 'city':'cq'}
people_1 = {'name1':'xu', 'name2':'guo', 'age':10, 'city':'nx'}
people_2 = {'name1':'huiguo', 'name2':'ma', 'age':15, 'city':'bj'}
peoples = []
peoples.append(people_0)
peoples.append(people_1)
peoples.append(people_2) #或者也可以用“people = [people_0, people_1, people_2]”
for people in peoples:
    print(people)
'''
#practice6.8:
'''
pet_info0 = {'species': 'cat', 'master name': '郭旭'}
pet_info1 = {'species': 'dog', 'master name': '马会国'}
pet_info2 = {'species': 'dragon', 'master name': '安小虎'}
pets = [pet_info0, pet_info1, pet_info2]
for pet in pets:
    print(f"species: {pet['species']}; master name: {pet['master name']}")
'''
#practice6.9:
'''
favorite_places = {
    'anxiaohu': ['美国'],
    'mahuiguo': ['北京', '上海', '南京'],
    'guoxu': ['宁夏', '日本']
}
for name, places in favorite_places.items():
    print(f"\n{name}喜欢的地方有: ") #字典循环打印名字
    for place in places:
        print(f"-- {place}") #列表循环打印地点
'''
#practice6.10:
'''
love_num = {
    'a':[5, 94516168],
    'b':[9],
    'c':[5555, 56, 456959],
    'd':[80, 498436, 268441654],
    'e':[6, 1]
}
for name, nums in love_num.items():
    print(f"{name.title()} love number is: ")
    for num in nums:
        print(f"----{num}")
'''
#practice6.11:
'''
cities = {
    '北京': {
        '所属国家': '中国',
        '人口约数': 500,
        '相关事实': '首都'
    },
    '上海': {
        '所属国家': '中国',
        '人口约数': 490,
        '相关事实': '直辖市'
    },
    '重庆': {
        '所属国家': '中国',
        '人口约数': 300,
        '相关事实': '直辖市'
    }
}
for city, city_info in cities.items(): #遍历外层字典的键值对
    print(f"\n{city}的信息如下 ") #打印键
    print(f"\n所属国家: {city_info['所属国家']}") #访问内层字典，打印其值
    print(f"人口约数: {city_info['人口约数']}")
    print(f"相关事实: {city_info['相关事实']}")
'''











#######################以下内容是原practice2.py文件中的########################

# 第七章：用户输入和while循环
# 接受用户输入：input函数。设计交互式程序。
# input函数的工作原理：使程序暂停，等待用户输入一些文本，获取输入后，将其赋给一个变量
# 使用int（）函数获取数值输入
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
'''
# 在使用input（）函数时，python会将用户输入解读为字符串。
# 求模运算符（%）：只会指出余数
'''
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
'''
# practice7.1:
'''
message = input("请问要租什么车？")
message_ = 'Let me see if I can find you a Subaru.'
print(message_)
'''
# practice7.2:
'''
message = input("有多少人用餐？")
message = int(message)
if message > 8:
    print("位置不够！")
else:
    print("请坐！")
'''
# practice7.3:
'''
num = input("请输入一个整数：")
num = int(num)
if num % 10 == 0:
    print("yes!")
else:
    print("no!")
'''
# while循环（for循环用于针对集合中的每个元素执行一个代码块，而while循环则不断地运行，直到指定的条件不再满足为止。）
'''
current_number = 1 #从1开始
while current_number <= 5: #如果小于等于5
    print(current_number) #打印
    current_number += 1 #加1，然后继续判断
'''
# 让用户选择何时退出(定义退出值)
'''
prompt = "\nTell me something, and I will repeat it back to you:" #输入一条消息
prompt = "\nEnter 'quit' to end the progrem. " #输入推出值
message = "" #记录用户输入的值，把初始值设置为空字符串
while message != 'quit': #比较message值与quit
    message = input(prompt) #输入
    if message != 'quit': #使用if测试，修复了“程序会将quit也作为一条消息打印出来”的问题
        #如果输入不是quit才打印
        print(message) #打印，直到用户输入quit使循环停止
'''
# 在要求满足很多条件才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。称为标志。
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the progrem. "
active = True #初始处于活动状态
while active: #只要active的值为true，程序一直运行
    message = input(prompt) #用户输入
    if message == 'quit': #判断输入是否为quit
        active = False #如是，则打印quit
    else: #否则打印用户输入的消息
        print(message)
'''
# 使用break退出循环（在所有循环中都可以用）
# 不论条件测试的结果如何，想立即退出while循环，不在运行余下的代码，可使用【break】语句
'''
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"#+=是拼接赋值运算符，把右边字符串拼接到左边变量的后面
while True:
    city = input(prompt)
    if city == 'quit':
         break
    else:
        print(f"I'd love to go to {city.title()}!")
'''
# 在循环中使用continue
# 要返回循环开头，并根据条件测试的结果决定是否继续执行循环
'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #如果上面的条件测试通过，则返回循环开头（while）
    print(current_number) #否则打印
'''
# 避免无限循环
'''
x = 1
while x <= 5:
    print(x)
    x += 1
'''
# practice7.4:
'''
while True:
    message = input("请输入pizza配料：")
    if message == 'quit':
        break
    else:
        print("ok，添加此配料！")
'''
# practice7.5:
'''
#这个程序会无限循环
while True: 
    message = input("输入年龄： ")
    age = int(message)
    if age < 3:
        print("免费！")
    elif age < 12:
        print("票价：10￥！")
    else:
        print("票价：15￥！")      
'''
# practice7.6:
'''
#使用break跳出循环
while True:
    age_input = input("输入年龄(输入‘quit’结束)： ")
    if age_input == 'quit':
        break   
    age = int(age_input)
    if age < 3:
        print("免费！")
    elif age < 12:
        print("票价：10￥！")
    else:
        print("票价：15￥！")

#在while循环中使用条件测试结束循环
age_input = input("请输入你的年龄（输入quit结束）：")
while age_input != 'quit': 
    age = int(age_input)
    if age < 3:
        print("免费！")
    elif age < 12:
        print("票价：10￥！")
    else:
        print("票价：15￥！")
    age_input = input("请输入你的年龄（输入quit结束）：")

#使用变量active控制循环结束的时机
active = True
while active:
    age_input = input("请输入你的年龄（输入quit结束）：")
    if age_input == 'quit':
        active = False
    else:
        age = int(age_input)
        if age < 3:
            print("免费！")
        elif age < 12:
            print("票价：10￥！")
        else:
            print("票价：15￥！")
'''
# practice7.7：编写无限循环，略.

# 使用while循环处理列表和字典
# 在列表之间移动元素
'''
#首先创建一个待验证用户列表
#和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#验证每个用户，直到没有未验证用户为止
#将每个经过验证的用户都移到已验证用户的列表

while unconfirmed_users:
    current_user = unconfirmed_users.pop() #pop方法是弹出列表末尾元素

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#显示所有的已验证用户
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
# 删除为特定值的所有列表元素
'''
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
'''
# 使用用户输入填充字典
'''
responses = {} #定义空字典
#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ") #键
    response = input('Which mountain would you like to climb someday? ') #值

    #将回答储存在字典中
    responses[name] = response

    #看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
'''
# practice7.8:
'''
sandwich_orders = ['sandwich332', 'sandwich333', 'sandwich336']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich!")
    finished_sandwiches.append(sandwich_order)
print()

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)
'''
# practice7.9:
'''
sandwich_orders = ['sandwich332', 'sandwich333', 'sandwich336', 'sandwich336', 'sandwich336', 'sandwich330']
print("No sandwich336!")
while 'sandwich336' in sandwich_orders:
    sandwich_orders.remove('sandwich336')
print(sandwich_orders)
'''
# practice7.10:
'''
place_info = {} #使用字典实现
while True:
    name = input("请输入你的姓名(结束请输入‘quit’)： ")
    if name == 'quit':
        break
    dream_place = input("请输入你最想去度假的地方： ")
    place_info[name] = dream_place
print()
print("调查结果如下：")
for name, dream_place in place_info.items():
    print(f"{name} want to {dream_place}")
'''

##第八章：函数
# 函数是带名字的代码块，用于完成具体的工作
# 定义函数
'''
def greet_user(): #def：函数定义
    """显示简单的问候语""" #文档字符串的注释
    print("Hello")
greet_user() #调用函数
'''
# 向函数传递信息（实参和形参）
'''
def greet_user(username): #username是形参
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")
greet_user('jesse') #调用函数greet_user（）并向它传递实参'jesse'
'''
# practice8.1:
'''
def display_message():
    print("函数")

display_message()
'''
# practice8.2:
'''
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book('酒国')
'''
# 传递实参：函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参
# 在调用函数时，python必须将函数调用中的每个实参关联到函数定义中的一个形参
# 最简单的方式是基于实参的【顺序】进行关联，称为【位置实参】
# 可多次调用
'''
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('狗', '郭旭')
'''
# 关键字实参：传递给函数的名值对。
'''
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='dog', pet_name='guoxu')
describe_pet(pet_name='guoxu', animal_type='dog') #顺序无关紧要。
'''
# 默认值。给每个形参指定默认值。
# 如果在调用函数中给形参提供了实参，python将使用指定的实参值
'''
def describe_pet(pet_name, animal_type='dog'): #pyth依然将这个实参视为位置实参，调用时需要传递的得放置在前面
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(pet_name='guoxu', animal_type='cat') #如不使用默认值
'''
# 等效的函数调用
# 避免实参错误
# practice8.3：
'''
def make_shirt(size, flower):
    print(f"这个T恤的size是：{size}, flower 是：{flower}")
make_shirt(18, 'ysudbvs') #位置实参
make_shirt(size=2651, flower='aligba') #关键字实参
'''
# practice8.4:
'''
def make_shirt(size, flower='I love python'):
    print(f"{size}, {flower}")

make_shirt(size='big')
make_shirt(size='midemun',)
make_shirt(flower='Yes', size='big',)
'''
# practice8.5:
'''
def describe_city(city_name, home_country='China'):
    print(f"{city_name} is in {home_country}")

describe_city(city_name='shanghai')
describe_city(city_name='bejin')
describe_city(city_name='dongjin', home_country='japanese')
'''
# 返回值(return语句将值返回到调用函数的那行代码)
# 返回简单的值
'''
def get_formatted_name(first_name, last_name): #通过形参接受名和姓
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}" #拼接姓名
    return full_name.title() #返回函数调用行
musician = get_formatted_name('jimi', 'hendrix')
#在调用可以返回值的函数时需要提供一个变量，以便将返回的值赋给它
print(musician)
'''
# 让实参变成可选的。（有时需要将实参变成可选的，以便使用函数的人只在必要时才提供额外的信息）
# 并非所有人都有中间名。为让中间名变成可选的，可给形参middle_name指定默认值（空字符串），在用户不提供中间名时不使用这个形参。
'''
def get_formatted_name(first_name, last_name, middle_name=''): #通过形参接受名和姓
    #pyhton将空字符串解读为True
    """返回标准格式的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}" #拼接姓名
    else:
        full_name = f"{first_name} {last_name}"  # 拼接姓名
    return full_name.title() #返回函数调用行

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee',) #确保位置关联
print(musician)
'''
# 返回字典
'''
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', '99')
print(musician)
'''
# 结合使用函数和while循环
'''
def get_formattend_name(first_name, last_name): #定义函数
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}" #拼接
    return full_name.title() #处理好后返回到调用函数处【把函数内部处理好的值传递到函数外部】

while True:
    #这是无限循环（后有改动）
    print("\nPlease tell me your name") #用户输入
    f_name = input("First name: ") #用户输入
    if f_name == 'q':
        break
    l_name = input("Last name: ") #用户输入
    #if l_name == 'q': #这个条件检测实则不需要
       # break #这个条件检测实则不需要

    formatted_name = get_formattend_name(f_name, l_name) #调用函数处理用户输入
    print(f"\nHello, {formatted_name}!") #打印
'''
# practice8.6:
'''
def city_country(city, country):
    print(f"{city},{country}")
    return city_country

city_country(city="shanghai", country="china")
city_country(city="beijin", country="china")
city_country(city="nanjin", country="china")
'''
# practice8.7:
'''
def make_album(singer, zuoping, num=None):
    m_album = {'S' : singer, 'Z' : zuoping, 'N':num}
    print(m_album)
    return make_album

make_album(singer='郭旭', zuoping='shit', num=10)
make_album(singer='马会国', zuoping='shit')
make_album(singer='安小虎', zuoping='最伟大的作品')
'''
# practice8.8:【*】【*】【*】【*】【*】
'''
def make_album(singer, zuoping, num=None): #定义函数（三个形参）
    m_album = {
        '歌手' :singer,
        '专辑' :zuoping,
    } #定义一个字典（其值为形参）
    if num is not None:
        m_album['歌曲数'] = num
    return m_album #返回函数调用处

while True:
    print("请输入信息（按q退出）")
    singer = input("\t姓名： ")
    if singer == 'q':
        break
    zuoping = input("\t作品： ")
    if zuoping == 'q':
        break
    num = input("\t数量（选填）： ")
    if num == 'q':
        break
    if num:
        album_info = make_album(singer, zuoping, int(num))
    else:
        album_info = make_album(singer, zuoping)
    print(album_info)
'''
# 传递列表（将列表传递给函数后，函数可直接访问）（用函数处理列表）
'''
def greet_users(names): #定义函数
    """向列表中的每个用户发出简单的问候"""
    for name in names: #
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot'] #定义列表
greet_users(usernames) #定义函数处理列表
'''
# 在函数中修改列表。
# 情景：一家为用户提交的设计制作3D打印模型的公司。需要打印的设计事先存储在一个列表中，打印后将被移到另一个列表中。
# 不使用函数的操作如下：
'''
unprinted_designs = ['photo case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
'''
# 使用函数的操作：(把具体操作交给函数，让主程序更加简洁)
'''
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models): #
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['photo case', 'robot pendant', 'doedecahedron']
completed_models = []

print_models(unprinted_designs, completed_models) #调用第一个函数
show_completed_models(completed_models) #调用第二个函数
'''
# 禁止函数修改列表。
# 为保留原来未打印的设计列表，需要对其进行存档。（可向函数传递列表副本而不是原始列表）
'''
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models): #
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['photo case', 'robot pendant', 'doedecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models) #调用第一个函数【此处向函数传递了unprinted_designs的副本】
show_completed_models(completed_models) #调用第二个函数

#如无必要，一般应将原始列表传递给函数。因为让函数处理现成的列表可避免花时间和内存创建副本。【在处理大型列表时尤其如此】
'''
# practice8.9:
'''
def show_message(messages):
    for message in messages:
        print(message)

messages = ['I', 'love', 'python']
show_message(messages)
'''
# practice8.10:
'''
def send_messages(messages):
    while messages:
        message = messages.pop()
        sent_messages.append(message)
    print(sent_messages)
    print(messages)
def show_message(messages):
    for message in messages:
        print(message)


messages = ['I', 'love', 'python']
sent_messages = []
show_message(messages)
send_messages(messages)
'''
# practice8.11:
'''
def send_messages(messages):
    while messages:
        message = messages.pop()
        sent_messages.append(message)
    print(sent_messages)
def show_message(messages):
    for message in messages:
        print(message)

messages = ['I', 'love', 'python']
sent_messages = []
show_message(messages)
send_messages(messages[:])
print(messages)
'''
# 传递【任意】数量的实参
'''
def make_pizza(*toppings): #形参前的*号意为创建一个元组
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni') #函数收到的是一个值的元组
make_pizza('mushrooms', 'green peppers', 'extra cheese') #函数收到的是三个值的元组
'''
# 用循环处理（打印制作所需各种配料）
'''
def make_pizza(*toppings):
    """概述要制作的pizza"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"--{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
# 结合使用【位置实参】和任意数量的实参
'''
def make_pizza(size, *toppings): #定义函数
    """概述要制作的pizza"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"--{topping}")

make_pizza(56, 'pepperoni') #基于上述定义，把第一个值给size，其他值都给toppings
make_pizza(99, 'mushrooms', 'green peppers', 'extra cheese') #基于上述定义，把第一个值给size，其他值都给toppings
'''
# 使用任意数量的关键字实参
# 示例：你知道将收到有关用户的信息，但不确定是什么信息
'''
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们直到的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', #提供名和姓
                             location='princeton', #允许提供任意数量的名值对
                             field='physics', #允许提供任意数量的名值对
                             wife='马会国') 
print(user_profile)
'''
# practice8.12:
'''
def make_sandwich(*burden):
    print(f"添加的食材如下: {burden}.")

make_sandwich('a', 'b', 'c', 'd')
make_sandwich(1, 59, 894)
make_sandwich('羊肉串')
'''
# practice8.13:
'''
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们直到的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('小虎', '安', #提供名和姓
                             location='重庆', #允许提供任意数量的名值对
                             field='逻辑学', #允许提供任意数量的名值对
                             wife='C娅')
print(user_profile)
'''
# practice8.14:
'''
def make_car(zhizaoshang, xinghao, **car_info):
    car_info['zhizaosahng'] = zhizaoshang
    car_info['zinghao'] = xinghao
    return car_info

car = make_car('比亚迪', '唐', yanse='黄色', leixing='大型SUV')
print(car)
'''
# 可将函数存储在【模块】中（扩展名为.py的独立文件），再将模块导入主程序（import语句）
# 导入模块的方法
# 1.导入整个模块
# 1.1 创建模块

# 模块代码在pizza.py文件中

# 1.2 接下来在pizza.py所在的目录中创建一个名为making_pizzas.py的文件。
#####这个文件先导入刚创建的模块，再调用make_pizza（）两次。
# making_pizzas.py
'''
import pizza
pizza.make_pizza(16, 'bivbk')
pizza.make_pizza(12, 'naib', 'iuabfa', 'snvbr')
'''
# 要调用被导入模块中的函数，可指定模块和函数名如：pizza.make_pizza（）
# 另一种是直接调用模块中的所有函数：import+模块

# 导入特定的函数：（调用函数时指定其名称即可）
# 【from 模块名 import 函数名】
# 【form 模块名 import 函数名1,函数名2，...】

# 使用【as给函数】指定别名（如果函数名与程序中既有名称重复可用）例如：
'''
from pizza import make_pizza as mp
mp(16, 'eef')
'''

# 使用【as给模块】指定别名
'''
import pizza as p
p.make_pizza(16, 'xidgho')
'''

# 导入模块中的所有函数【使用*】,则可通过名称来调用每个函数，无需点号
'''
from pizza import *
make_pizza(16, 'isgui')
'''
################【最佳的做法是要么只导入需要使用的函数，要么导入整个模块并使用点号】
# practice8.15--8.17略。


# 第九章  类
# 面向对象编程是最有效的软件编写方式之一。在面向对象编程中，编写表示现实世界的事物和情景的类，并基于这些类来创建对象
# 根据类来创建对象称为实例化
# 创建和使用类
'''
class Dog: #定义一个名为Dog的类（约定首字母大写的是类）
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        # __init__()方法。类中的函数称为方法。此处包含三个形参【其中self必不可少且靠前、不需要提供值】
        """初始化属性name和age"""
        self.name = name #以self为前缀的变量可供类中的所有方法使用，可通过类的任意实例来访问。
        self.age = age #以self为前缀的变量可供类中的所有方法使用，可通过类的任意实例来访问。
    def sit(self): #sit方法
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")
    def roll_over(self): #roll_over方法
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")
'''
# 根据类创建实例
# 可以将类视为有关如何创建实例的说明。
# 例如上述Dog类就是一系列说明，让py知道如何创建表示特定小狗的实例。
'''
class Dog:
 """一次模拟小狗的简单尝试"""

 def __init__(self, name, age):
    # __init__()方法。类中的函数称为方法。此处包含三个形参【其中self必不可少且靠前、不需要提供值】
    """初始化属性name和age"""
    self.name = name  # 以self为前缀的变量可供类中的所有方法使用，可通过类的任意实例来访问。
    self.age = age  # 以self为前缀的变量可供类中的所有方法使用，可通过类的任意实例来访问。

def sit(self):  # sit方法
  """模拟小狗收到命令时坐下"""
  print(f"{self.name} is now sitting.")

def roll_over(self):  # roll_over方法
  """模拟小狗收到命令时打滚"""
  print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6) 
#调用Dog类中的__init__方法并传入实参'willie'和6。类返回实例并赋值给my_dog变量。（根据类创建的实例用全小写（my_dog））
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
'''
# 01 创建多个实例
'''
class Dog:
    def __init__(self, name, age):
        # __init__()方法。类中的函数称为方法。此处包含三个形参【其中self必不可少且靠前、不需要提供值】,称为属性
        """初始化属性name和age"""
        self.name = name  # 以self为前缀的变量可供类中的所有方法使用，可通过类的任意实例来访问。
        self.age = age  # 以self为前缀的变量可供类中的所有方法使用，可通过类的任意实例来访问。

    def sit(self):  # sit方法
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):  # roll_over方法
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
'''
# practice9.1:
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restauarant(self):
        print(f"这个餐厅叫{self.restaurant_name},主营{self.cuisine_type}.")
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业！")

restaurant = Restaurant('新疆羊肉串', '烧烤')
restaurant.describe_restauarant()
restaurant.open_restaurant()
'''
# practice9.2:
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restauarant(self):
        print(f"这个餐厅叫{self.restaurant_name},主营{self.cuisine_type}.")
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业！")

restaurant = Restaurant('新疆羊肉串', '烧烤')
restaurant.describe_restauarant()

restaurant = Restaurant('KFC', 'UFO')
restaurant.describe_restauarant()

restaurant = Restaurant('凯里酸汤鱼', '贵州酸汤鱼')
restaurant.describe_restauarant()
'''
# practice9.3:
'''
class User:
    def __init__(self, first_name, last_name, xinbie, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.xinbie = xinbie
    def describe_user(self):
        print(f"用户基本信息如下\n\t姓名：{self.first_name}{self.last_name} \n\t性别：{self.xinbie} \n\t年龄：{self.age}")
        #print(f"{self}")
    def greet_user(self):
        print(f"Hello {self.first_name}{self.last_name}！")

user = User('安', '小虎', '男', 99)
user.describe_user()
user.greet_user()
print()
user = User('图', '灵', '男', 29)
user.describe_user()
user.greet_user()
'''
# 使用类和实例（可以使用类来模拟现实世界的很多情形）
# 9.2.1Car类
'''
class Car:
    """一次模拟汽车的的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
'''
# 给属性指定默认值（有些属性无需通过形参来定义，可以在__init__方法中为其指定默认值）
'''
class Car:
    """一次模拟汽车的的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #添加属性，其初始值为0
    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''
# 修改属性的值（三种方法）
# 01直接通过实例修改
'''
class Car:
    """一次模拟汽车的的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #添加属性，其初始值为0
    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 #【直接访问属性并修改其值】
my_new_car.read_odometer()
'''
# 通过方法修改属性的值
'''
class Car:
    """一次模拟汽车的的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #添加属性，其初始值为0
    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage): #【添加一个方法，这个方法接受一个里程值】
        self.odometer_reading = mileage #并将其赋给self.odometer_reading

        if mileage >= self.odometer_reading: #可以做一些额外的工作【比如这个if循环】
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23) #调用update_odometer方法，并传递一个实参，该实参对应形参mileage
my_new_car.read_odometer()
'''
# 通过方法让属性的值递增
'''
class Car:
    """一次模拟汽车的的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        # 添加属性，其初始值为0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):  # 添加一个方法，这个方法接受一个里程值
        self.odometer_reading = mileage  # 并将其赋给self.odometer_reading
        print(f"This car has {mileage} miles on it.")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23_500)  # 调用update_odometer方法，并传递一个实参，该实参对应形参mileage

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
'''
# practice9.4:
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restauarant(self):
        print(f"这个餐厅叫{self.restaurant_name},主营{self.cuisine_type}.")
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业！")
    def number(self):
            print(f"有{self.number_served}人曾在这里就餐.")
    def set_number(self, num):
        self.number_served = num
        #print(f"有{self.number_served}人曾在这里就餐.")
    def increment_number_served(self, num_):
        self.number_served += num_
        print(f"每天可能接待{self.number_served}人.")

restaurant = Restaurant('新疆羊肉串', '烧烤')
restaurant.describe_restauarant()
#restaurant.number_served = 99 ####【实例直接修改，在此处修改，修改后调用】
#
restaurant.set_number(23)
restaurant.number()
restaurant.increment_number_served(200)
restaurant.open_restaurant()
'''
# practice9.5:
'''
class User:
    def __init__(self, first_name, last_name, xinbie, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.xinbie = xinbie
        self.login_attempts = 0
    def describe_user(self):
        print(f"用户基本信息如下\n\t姓名：{self.first_name}{self.last_name} \n\t性别：{self.xinbie} \n\t年龄：{self.age}")
        #print(f"{self}")
    def greet_user(self):
        print(f"Hello {self.first_name}{self.last_name}！")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('安', '小虎', '男', 99)
user.describe_user()
user.greet_user()
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
'''
# 继承
# 如果要编写的类是一个既有的类的特殊版本，可使用继承。
# 当一个类继承另一个类时，将自动获得后者的所有属性和方法。
# 原有的类称为父类，而新类称为子类。【除此之外子类还可以定义自己的属性和方法】

# 子类的__init__()方法
# 在既有的类的基础上编写新类，通常要调用父类的__init__()方法。
# 这将初始化在父类的__init__()方法中定义的所有属性，从而让子类也可以使用这些属性。
'''
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一个句子，指出汽车的行驶里程"""
        pritn(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles
#在创建子类时，父类必须包含在当前文件中，且位于子类前面。
class ElectricCar(Car): #定义子类时，必须在括号内指定父类的名称。【子类应该只存在特有的属性】
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): #__init__()方法接受并创建Car实例所需要的信息
        """初始化父类的属性"""
        super().__init__(make, model, year) #super()方法能调用父类的方法【这里是__init__()方法】
        self.battery_size = 40 #添加了一个电动车特有的属性，并设置初始值
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.") #打印特有属性
    def fill_gas_tank(self): #假设Car类中有一个名为fill_gas_tank（）的方法，它对电动汽车来说毫无意义，这里进行了重写
        """电动车没有油箱"""
        print("This car does't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery() 
'''
# 属性和方法越来越多，文件越来越长。
# 在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。
'''
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一个句子，指出汽车的行驶里程"""
        pritn(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles

class Battery: #定义新类，它没有继承任何类
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")

class ElectricCar(Car): #定义子类时，必须在括号内指定父类的名称。【子类应该只存在特有的属性】
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): #__init__()方法接受并创建Car实例所需要的信息
        """初始化父类的属性"""
        super().__init__(make, model, year) #super()方法能调用父类的方法【这里是__init__()方法】
        self.battery = Battery() 

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery() 
'''











##################练习测试时所用的被测试文件
'''
def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
'''
##################练习测试时所用的被测试文件
'''
def get_city_country(city, country, population=None):
    if population:
        ci_co = f"{city.title()}, {country.title()} - population {population}"
    else:
        ci_co = f"{city.title()}, {country.title()}"
    return ci_co
'''
##################练习测试时所用的被测试文件
#一个要测试的类【在practice.py中】
'''
class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results")
        for response in self.responses:
            print(f"- {response}")
'''
##################练习测试时所用的被测试文件
'''
class Employee:
    def __init__(self, first_name, last_name, n_x):
        self.first_name = first_name
        self.last_name = last_name
        self.n_x = n_x
    def give_raise(self, amount=50000): #实现年薪增量(give_raise方法)
        self.n_x += amount
        return self.n_x
'''
##################练习测试时所用的被测试文件







'''#practice2[导入函数的时候]的一个程序用到的函数
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-- {topping}")
'''



#practice9.6:
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restauarant(self):
        print(f"这个餐厅叫{self.restaurant_name},主营{self.cuisine_type}.")
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业！")
    def number(self):
            print(f"有{self.number_served}人曾在这里就餐.")
    def set_number(self, num):
        self.number_served = num
        #print(f"有{self.number_served}人曾在这里就餐.")
    def increment_number_served(self, num_):
        self.number_served += num_
        print(f"每天可能接待{self.number_served}人.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def couwei(self):
        print(f"口味如下：")
        for flavor in self.flavors:
            print(f"\t--{flavor}")

Ice = IceCreamStand('冰激淋店',
                    '冷饮',
                    ['a', 'b', 'c']
                    )
Ice.describe_restauarant()
Ice.set_number(10)
Ice.number()
Ice.couwei()
'''
#practice9.7:
'''
class User:
    def __init__(self, first_name, last_name, xinbie, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.xinbie = xinbie
        self.login_attempts = 0
    def describe_user(self):
        print(f"用户基本信息如下\n\t姓名：{self.first_name}{self.last_name} \n\t性别：{self.xinbie} \n\t年龄：{self.age}")
        #print(f"{self}")
    def greet_user(self):
        print(f"Hello {self.first_name}{self.last_name}！")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, xinbie, age, privileges):
        super().__init__(first_name, last_name, xinbie, age)
        self.privileges = privileges

    def show_privileges(self):
        print(f"管理员权限入下：")
        for privilege in self.privileges:
            print(f"\t--{privilege}")

Ad = Admin('an',
                   'xiaohu',
                   'nan',
                   99,
                   ['can add post', 'can delete post', 'can ban user']
                   )
Ad.show_privileges()
'''
#practice9.9:
'''
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一个句子，指出汽车的行驶里程"""
        pritn(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles

class Battery: #定义新类，它没有继承任何类
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        """打印一条消息报告续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car): #定义子类时，必须在括号内指定父类的名称。【子类应该只存在特有的属性】
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): #__init__()方法接受并创建Car实例所需要的信息
        """初始化父类的属性"""
        super().__init__(make, model, year) #super()方法能调用父类的方法【这里是__init__()方法】
        self.battery = Battery()

Car = Battery()
Car.get_range() #升级前
Car.upgrade_battery() #强行升级
Car.get_range() #升级后
'''
#导入类
#from car import Car【从car文件（模块）中导入Car类】
#可在一个模块中存储多个类
#from car import Car, ElectricCar【从一个模块中导入多个类】
#import car【导入整个模块】
#from module_name import *【导入模块中的所有类（该方法不推荐）】
#习题略

#python标准库【是一组模块】
#习题略


#第十章 文件和异常
#读取文件
#读取文件的全部内容
#要读取文件，需要一个包含若干行文本的文件。
##创建一个文件，它包含精确到小数点后30位的圆周率值，且在小数点后每10位处换行。
'''
from pathlib import Path
#从pethlib模块导入Path类.提供特定功能的模块通常称为库
path = Path('axh.txt')
#axh.txt与.py在同一目录下，因此只需文件名即可访问
contents = path.read_text().rstrip()
#read_text()方法读取文件的全部内容，作为一个字符串返回。
#要在读取文件时删除末尾的换行符，可在read_text（）后直接调用rstrip（）。【方法链式调用】
contents = contents.rstrip()
#相比于原始文件，该输出多了一行，要删除这个空行，可对contents调用rstrip（）。
print(contents)
'''
#相对文件路径和绝对文件路径
#当将类似于axh.txt文件名传递给Path时，python将在当前执行的文件（.py）所在的目录中查找。
#指定路劲的两种方式：
#相对文件路径：让python到相对于当前运行的程序所在目录的指定位置去查找【path=Path('文件所在文件夹/文件)】
# 【此时文件所在文件夹和程序在同一文件夹】
#绝对文件路径：以系统根文件夹为起点
'''
from pathlib import Path
path = Path('C:/Users/lenovo/Desktop/axh.txt')
contents = path.read_text()
print(contents)
'''
#访问文件中的各行
#使用splitlines()方法将冗长的字符串转换为一系列行，再使用for循环以每次一行的方式检查文件中的各行。
'''
from pathlib import Path
path = Path('C:/Users/lenovo/Desktop/axh.txt')
contents = path.read_text()
lines = contents.splitlines() #splitlines()方法返回一个列表，其中包含文件所有的行
for line in lines:
    print(line)
'''
#使用文件的内容
#将文件的内容读取到内存中后，就能以任意方式使用这些数据了。
'''
from pathlib import Path
path = Path('C:/Users/lenovo/Desktop/axh.txt')
contents = path.read_text()
lines = contents.splitlines()
txt_string = '' ##splitlines()方法返回一个列表，其中包含文件所有的行
for line in lines:
    txt_string += line.lstrip() #使用循环将各行加入txt_string
print(txt_string)
print(len(txt_string))
#变量txt_string存储的字符串包含原来位于每行左端的空格，调用lstrip()方法可以删除空格
'''
#包含100万位的大型文件【方法同上】
#例：圆周率值中包含你的生日吗？
'''
from pathlib import Path
path = Path('C:/Users/lenovo/Desktop/axh.txt')
contents = path.read_text()
lines = contents.splitlines()
txt_string = '' ##splitlines()方法返回一个列表，其中包含文件所有的行
for line in lines:
    txt_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in txt_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
'''
#practice10.1:
'''
from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text(encoding='utf-8') #encoding(指定编码方式)
print(contents)
ls = contents.splitlines() #splitlines方法返回一个列表
for l in ls:
    print(l)
'''
#practice10.2:
'''
from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text(encoding='utf-8') #encoding(指定编码方式)
message = contents.replace('python', 'c') #replace方法可将字符串中的指定单词替换为其他单词
print(message)
'''
#practice10.3:
'''
from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text(encoding='utf-8').replace('python', 'c') #使用方法链式调用
print(contents)
'''
#写入文件
#保存数据的最简单的方式之一是将其写入文件。
#通过将输入写入文件，即便关闭包含程序输出的终端窗口，这些输出也依然存在。
#写入一行
'''
from pathlib import Path
path = Path('learning_python.txt')
path.write_text("In python you can fuck any one!")
#write_text（）方法接受单个实参，即要写入文件的字符串
#运行上述代码，即可在文本中写入一行
#注意：python只能将字符串写入文本文件。如果要写入数值数据，必须先使用函数str（）将其转换为字符串格式
'''
#写入多行
#write_text()方法会完成以下工作：
#首先，如果path变量对应的路径指向的文件不存在，就创建它
#其次，将字符串写入文件后，它会确保文件得以妥善地关闭。
'''
from pathlib import Path
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path = Path('Axh.txt') #若对已存在的文件作此操作，则write_text会删除其内容，然后将指定内容写入
path.write_text(contents)
'''
#practice10.4
'''
from pathlib import Path
name = input("请输入姓名： ")
path = Path('guest.txt')
path.write_text(name)
'''
#practice10.5【*****】
'''
from pathlib import Path
path = Path('guest_book.txt')
content = '' #初始化存储内容的字符串
print("请输入姓名（按q退出）：")
while True:
    name = input()
    if name.lower() == 'q':
        break
    content += name + '\n' #每次添加名字后加上换行符
path.write_text(content.strip()) #用strip去掉最后多余的换行符
print("所有姓名已保存到guest_book.txt文件")
'''

#异常
#python使用称为异常的特殊对象来管理程序执行期间发生的错误。
#每当发生让python不知所措的错误时，它都会创建一个异常对象。
#如果编写了处理该异常的代码，程序继续运行；如果未对异常进行处理，程序将停止，并显示一个traceback。
#【异常是用try-except代码块处理的】

#处理ZeroDivisionError异常

#print(5/0) #运行这行代码会出现ZeroDivisionError错误
'''
try: 
    print(5/0) #如果此代码引发异常则进入except代码块，无异常则正常打印
except ZeroDivisionError:
    print("You can't divide by zero!")
'''
#使用异常避免崩溃
#如果在错误发生时程序工作还没有完成，妥善地处理错误就显得尤为重要。
'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number) #尝试计算【只有可能引发错误的代码才需要放在try语句中】
    except ZeroDivisionError: #如果报错ZeroDivisionError
        print("You can't divide by 0!") #打印
    else: #否则打印计算结果
        print(answer)
'''
#处理FileNotFoundError异常
'''
from pathlib import Path
path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry,the file {path} does not exist.")
'''
#分析文本【以下程序可得出文本单词数】
'''
from pathlib import Path
path = Path('guest_book.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry,the file {path} does not exist.")
else:
    #计算文件大致包含多少个单词
    words = contents.split() #该方法生成一个列表，其中包含文档中的所有单词。
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
'''
#使用多个文件【*****】#静默失败
'''
from pathlib import Path
def count_words(path): #把上面的代码移到此函数中
    """计算一个文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        path #pass语句让python在执行到此时什么都不做
        #print(f"Sorry,the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()  # 该方法生成一个列表，其中包含文档中的所有单词。
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
filenames = ['aaa.txt',
             'bbb.txt',
             'ccc.txt',
             'ddd.txt',
             'eee.txt',
             'fff.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
'''
#practice10.6:
'''
try:
    num1 = int(input("请输入第一个数："))
except ValueError:
    print("第一个数输入不合法！！！")
else:
    try:
        num2 = int(input("请输入第二个数："))
    except ValueError:
        print("第二个数输入不合法！！！")
    else:
        print(num1 + num2)
'''
#practice10.7:
'''以下是两个while循环，保证用户在输入不合法之后可以继续输入
while True:
    try:
        num1 = int(input("请输入第一个数："))
    except ValueError:
        print("第一个数输入不合法！！！")
    else:
        break
while True:
    try:
        num2 = int(input("请输入第二个数："))
    except ValueError:
        print("第二个数输入不合法！！！")
    else:
        print(num1 + num2)
        break
'''

#以下是一个while循环
'''
print("欢迎使用加法计算器（输入‘q’退出）！")
while True:
    try:
        num1 = input("请输入第一个数：")
        if num1 == 'q':
            break
        num1 = int(num1)
        num2 = input("请输入第二个数：")
        if num2 == 'q':
            break
        num2 = int(num2)
        print(num1 + num2)
        break
    except ValueError:
        print("输入不合法！！！")
'''
#practice10.8:
'''
from pathlib import Path
def lgwj(path):
    try:
        contents = path.read_text(encoding='utf-8') #读取文件
        print(contents) #打印读取到的内容
    except FileNotFoundError:
        print(f"{filename}文件不存在!")
filenames = ['cats.txt', 'xxx.txt', 'dogs.txt'] #1.实例，两个文件组成的列表
for filename in filenames: #2.遍历这个列表，对每个文件做以下操作
    path = Path(filename) #3.访问文件
    lgwj(path) #4.调用lgwj函数
'''
#practice10.9:
'''
from pathlib import Path
def lgwj(path):
    try:
        contents = path.read_text(encoding='utf-8') #读取文件
        print(contents) #打印读取到的内容
    except FileNotFoundError:
        path #静默失败
        #print(f"{filename}文件不存在!")
filenames = ['cats.txt', 'xxx.txt', 'dogs.txt'] #1.实例，文件组成的列表
for filename in filenames: #2.遍历这个列表，对每个文件做以下操作
    path = Path(filename) #3.访问文件
    lgwj(path) #4.调用lgwj函数
'''
#practice10.10:
'''
from pathlib import Path
def caozuo(path, char='道'):
    try:
        contents = path.read_text(encoding='gbk', errors='ignore')
        count = contents.count('道') #count计数                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        print(f"'{char}'在文章{path.name}中出现了{count}次")
    except FileNotFoundError:
        print(f"{path.name}文件不存在，跳过统计！")

filenames = ['东坡易传-宋-苏东坡.txt',
             '读易详说-宋-李光.txt',
             '横渠易说-宋-张载.txt'
             ]
for filename in filenames:
    path = Path(filename)
    caozuo(path)
'''
#存储数据
#程序会把以用户提供的信息存储在列表和字典等数据结构中。
#使用【模块json】来存储数据。
##json能将简单的python数据结构转换为JSON格式的字符串，并在程序运行时从文件中加载数据。
#JSON格式最初是为javaScript开发的，但随后成了一种通用的格式，被众多语言采用。
#使用json.dumps()和json.loads()
#json.dumps()函数接受一个实参，即要转换为JSON格式的数据，这个函数返回一个字符串
'''
from pathlib import Path
import json #导入模块json

numbers = [2, 3, 5, 7, 11, 13] #创建一个数值列表

path = Path('numbers.json') #选择一个文件名，指定要将该数值列表存储到哪个文件中
contents = json.dumps(numbers) #使用json.dumps()函数生成一个字符串
path.write_text(contents) #写入文件
'''
#使用json.loads()将这个列表读取到内存中
'''
from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
'''
#保存和读取用户生成的数据
'''
from pathlib import Path
import json
username = input("What is your name? ") #用户输入

path = Path('username.json') #创建文件
contents = json.dumps(username) #转字符串
path.write_text(contents) #写入

print(f"We'll remeber you when you come back, {username}!")
'''
'''
from pathlib import Path
import json
path = Path('username.json')
contents = path.read_text() #读取文件
username = json.loads(contents) #将恢复的文件赋值给username
print(f"Welcome back, {username}")
'''
'''
from pathlib import Path
import json
path = Path('username.json')
if path.exists(): #如果指定文件存在则True
    contents = path.read_text() #读取
    username = json.loads(contents) #恢复
    print(f"Welcome back, {username}!")
else:
    username =input(f"What's your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remeber you when you come back, {username}")
'''
#重构
#虽然代码能够正确地运行，但还可以将其划分为一系列完成具体工作的函数来进行改进。此过程称为重构
'''
from pathlib import Path
import json

def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    if path.exists():  # 如果指定文件存在则True
        contents = path.read_text()  # 读取
        username = json.loads(contents)  # 恢复
        print(f"Welcome back, {username}!")
    else:
        username = input(f"What's your name?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remeber you when you come back, {username}")
greet_user()
'''
#重构greet_user()
'''
from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():  # 如果指定文件存在则True
        contents = path.read_text()  # 读取
        username = json.loads(contents)  # 恢复
        return username
    else:
        return None
def get_new_username(path):
    """提示用户输入用户名"""
    username = input(f"What's your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remeber you when you come back, {username}")
greet_user()
'''
#practice10.11:
#输入，存储，读取
'''
from pathlib import Path
import json

num = input("请输入:")
path = Path('number.txt')
contents = json.dumps(num) #转字符串
path.write_text(contents) #写入
print("存储完成！")

num_ = path.read_text()
number = json.loads(num_)
print(f"I kown your favorite number! It's {number}")
'''
#practice10.12:
'''
from pathlib import Path
import json

path = Path('number.txt')
def file():
    num = input("请输入:")
    contents = json.dumps(num)  # 转字符串
    path.write_text(contents)  # 写入
    print(f"存储{num}完成！")

try:
    num_ = path.read_text()
    if not num_.strip():
        print("文件为空，请先储存！")
        file()
    else:
        number = json.loads(num_)
        print(f"I kown your favorite number! It's {number}")
except FileNotFoundError:
    print("文件不存在！")
    file()
'''
#practice10.13:
'''
from pathlib import Path
import json

username = input("What is your name? ")
xinbie = input("girl or boy? ")
age = input("How old are you? ")

user_info = {'姓名':username, '性别':xinbie, '年龄':age}
path = Path('username.json')
contents = json.dumps(user_info)
path.write_text(contents)

username_ = path.read_text()
user = json.loads(username_)
#print(user)
for us1,us2 in user.items():
    print(f"{us1}：{us2}")
'''
#practice10.14:
'''
from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():  # 如果指定文件存在则True
        contents = path.read_text()  # 读取
        username = json.loads(contents)  # 恢复
        return username
    else:
        return None
def get_new_username(path):
    """提示用户输入用户名"""
    username = input(f"What's your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    username = get_stored_username(path)
    print(f"请问您是{username}先生/女士吗?")
    num = input("你可以输入'yes'或者其他: ")
    if num == 'yes':
        print(f"Welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remeber you when you come back, {username}")
greet_user()
'''

#第11章 测试代码【pytest】【证明函数，类能正确地工作】
#1.测试函数
'''
from practice2 import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
'''
#单元测试和测试用例
#单元测试用于核实函数的某个方面没有问题。
#测试用例是一组单元测试
#全覆盖测试用例
#测试文件的名称很重要，必须以test打头，当python运行测试时，它将查找以test打头的文件，并运行其中的所有测试。
'''
from practice2 import get_formatted_name

def test_first_last_name(): #【测试函数】名必须以test打头，并且更具描述性
    """能够正确处理像Janis Joplin这样的姓名吗"""
    formatted_name = get_formatted_name('janis', 'joplin') #调用要测试的函数
    #【断言（assertion）】就是声称满足特定的条件：这里声称formatted_name的值为'Janis Joplin'
    assert formatted_name == 'Janis Joplin'
#让pytest运行这个测试文件【文件名必须以test开头或结尾(带下划线)】
#若测试未通过,如果检查的条件没错，不要修改测试，应该修复导致测试不能通过的代码。
'''
'''
from practice2 import get_formatted_name
def test_first_last_name():
    """能够正确处理像Janis Joplin这样的姓名吗"""
    formatted_name = get_formatted_name('janis', 'joplin')  # 调用要测试的函数
    # 【断言（assertion）】就是声称满足特定的条件：这里声称formatted_name的值为'Janis Joplin'
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗"""
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus'
    )
    assert formatted_name == 'Wolfgang Amadeus Mozart'
'''
#practice11.1:
'''
from practice1 import get_city_country
def test_cities():
    info = get_city_country(
        'santiago', 'chile'
    )
    assert info == 'Santiago, Chile'
'''
#practice11.2:
'''
from practice1 import get_city_country
def test_cities():
    info = get_city_country(
        'santiago', 'chile'
    )
    assert info == 'Santiago, Chile'
'''
'''
from practice1 import get_city_country
def test_ci_co_po():
    info = get_city_country(
        'santiago', 'chile', population=50000000
    )
    assert info == 'Santiago, Chile - population 50000000'
'''

#测试类
#各种断言
#常用断言
'''
assert a == b [断言两个值相等]
assert a != b [断言两个值不等]
assert a [断言a的布尔值为True]
assert not a [断言a的布尔值为False]
assert element in list [断言元素在列表中]
assert element not in list [断言元素不在列表中]
'''
#一个要测试的类【在practice.py中】
#一个使用AnonymousSurvey类的程序
'''
from practice1 import AnonymousSurvey
#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak? "
language_survey = AnonymousSurvey(question) #创建问题实例
#显示问题并存储答案
language_survey.show_question() #调用打印问题函数
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("language: ") #获取用户答案
    if response == 'q':
        break
    language_survey.store_response(response)  #存储答案的函数
#显示调查结果
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
'''
#测试AnonymousSurvey类
'''
from practice1 import AnonymousSurvey
def test_store_single_response():
    """验证用户在面对调查问题时只提供一个答案，这个答案也能被妥善地存储"""
    question = "What language did you first learn to speak? " #【要测试类的行为，需创建其实例】
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses #断言元素在列表中

def test_store_single_responses():
    """验证用户在面对调查问题时只提供三个答案，这个答案也能被妥善地存储"""
    question = "What language did you first learn to speak? " #【要测试类的行为，需创建其实例】
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses #断言元素在列表中
'''
#使用【夹具：应用了装饰器的函数】【可减少测试代码的重复】
# 【在测试中，夹具可帮助搭建测试环境。这意味着创建供多个测试使用的资源】
#【在pytest中，要创建夹具，可编写一个使用装饰器@pytest.fixture装饰的函数】
#【装饰器是放在函数定义前面的指令，在运行函数前python将该指令应用于函数，以修改函数代码的行为】
'''
import pytest #导入pytest，因为定义了一个装饰器
from practice1 import AnonymousSurvey
@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的AnonymousSurvey实例"""
    question = "What language did you first learn to speak? "
    language_survey = AnonymousSurvey(question)
    return language_survey
def test_store_single_reaponse(language_survey):
    """测试单个答案会被妥善地处理"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
def test_store_three_responses(language_survey):
    """测试三个答案会被妥善处理"""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
'''
#practice11.3:
'''
import pytest
from practice1 import Employee
@pytest.fixture
def employee():
    employee = Employee('an', 'xiaohu', 500000)
    return employee
def test_give_default_raise(employee):
    assert employee.give_raise() == 550000
def test_give_custom_raise(employee):
    assert employee.give_raise(100000) == 600000
'''

#####################################！！！第一部分结束！！！##########################################