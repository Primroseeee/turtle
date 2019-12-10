#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle as t
def draw_branch(length):
    if length >= 10:
        #画右侧树枝
        t.forward(length)
        t.right(30)
        draw_branch(length - 10)
        
        #画左侧树枝
        t.left(60)  
        draw_branch(length - 10)

        #返回之前节点
        t.right(30)
        if length <=10:
            t.pencolor("yellow") #画笔颜色为黄色
            star()               #画五角星
        else:
            t.pencolor("red")  #画笔颜色为红色
            t.circle(5)        #画圆
        t.backward(length)

def star():               #画五角星
    t.fillcolor("yellow") #填充黄色
    t.begin_fill()
    j = 1
    while j <= 5:   
        t.forward(20)   #向前20
        t.left(144)     #逆时针转144度
        j = j + 1
    t.end_fill()

def main():
    t.penup()        #抬起画笔
    t.backward(100)  #后退100
    t.pendown()      #落下画笔
    t.pensize(2)     #画笔宽度2
    t.left(90)       #逆时针转90度，画笔朝上
    draw_branch(80)  #长度为80
    t.exitonclick()  #d点击后退出turtle
    

    
if __name__ == "__main__" :
    main()
