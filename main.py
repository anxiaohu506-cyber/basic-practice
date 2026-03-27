'''
import random #导入随机数模块

print("已进入猜数字游戏") #给玩家提示
print("想象一个整数") #给玩家提示

secret_number = random.randint(1, 100) #生成的数字，是正确答案
guess_count = 0 #记录猜测次数，起始为0

while True: #一直循环，直到玩家猜对用break跳出循环
    try: #从try到except是防止输入非法字符，如果输入非法字符则提示"NO,请输入一个有效数字"，而不是报错
        guess = int(input("请输入：")) #input让玩家输入，int则把输入转成数字
        guess_count += 1 #记录次数

        if guess < secret_number: #判断
            print("小了")
        elif guess > secret_number: #判断
            print("大了")
        else:
            print(f"YES,是{secret_number}") #判断
            print(f"共{guess_count}次")
            break #正确则跳出
    except ValueError:
        print("NO,请输入一个有效数字")
'''


import turtle
import math

screen = turtle.Screen()
screen.title("heart")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)

heart = turtle.Turtle()
heart.speed(0)
heart.hideturtle()
heart.color("pink")
heart.pensize(2)


def heart_x(t, scale=1):
    return scale * 16 * math.sin(t) ** 3


def heart_y(t, scale=1):
    return scale * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))


def draw_heart(scale):
    heart.penup()
    t = 0
    step = 0.05
    heart.goto(heart_x(t, scale), heart_y(t, scale))
    heart.pendown()
    heart.begin_fill()
    while t <= 2 * math.pi:
        x = heart_x(t, scale)
        y = heart_y(t, scale)
        heart.goto(x, y)
        t += step
    heart.end_fill()


angle = 0
base_scale = 15


def animate():
    global angle
    heart.clear()
    scale = base_scale + 1.5 * math.sin(angle)
    draw_heart(scale)
    screen.update()
    angle += 0.1
    screen.ontimer(animate, 40)


animate()
turtle.done()
