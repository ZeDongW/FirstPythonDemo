# 使用turtle画出奥运五环
# 导入turtle
import turtle
# 获取turtlr画笔对象
t = turtle.Pen()
#将画笔调粗
t.width("10")
#抬笔
t.penup()
#设置第一个五环的颜色，蓝色
t.color("blue")
#去第一个五环的坐标
t.goto(-260,-45)
#下笔
t.pendown()
#开始画半径为100的圆
t.circle(100)
#抬笔
t.penup()
#设置第二个五环的颜色，黄色
t.color("yellow")
#去第二个五环的坐标
t.goto(-130,-155)
#下笔
t.pendown()
#开始画半径为100的圆
t.circle(100)
#抬笔
t.penup()
#设置第三个五环的颜色，黑色
t.color("black")
#去第三个五环的坐标
t.goto(0,-45)
#下笔
t.pendown()
#开始画半径为100的圆
t.circle(100)
#抬笔
t.penup()
#设置第四个五环的颜色，绿色
t.color("green")
#去第四个五环的坐标
t.goto(130,-155)
#下笔
t.pendown()
#开始画半径为100的圆
t.circle(100)
#抬笔
t.penup()
#设置第五个五环的颜色，红色
t.color("red")
#去第一个五环的坐标
t.goto(260,-45)
#下笔
t.pendown()
#开始画半径为100的圆
t.circle(100)

#保留图像
turtle.done()