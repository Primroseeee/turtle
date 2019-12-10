#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle as t
def draw_branch(length):
    if length >= 10:
        t.forward(length)
        t.right(30)
        draw_branch(length - 10)

        t.left(60)
        draw_branch(length - 10)

        t.right(30)
        if length <=10:
            t.pencolor("yellow")
            star()
        else:
            t.pencolor("red")
            t.circle(5)
        t.backward(length)

def star():
    t.fillcolor("yellow")
    t.begin_fill()
    j = 1
    while j <= 5:   
        t.forward(20)   
        t.left(144)    
        j = j + 1
    t.end_fill()

def main():
    t.penup()
    t.backward(100)
    t.pendown()
    t.pensize(2)
    t.left(90)
    draw_branch(80)
    t.exitonclick()
    

    
if __name__ == "__main__" :
    main()


# In[ ]:




