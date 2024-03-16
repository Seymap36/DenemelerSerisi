import turtle
import random
renkler=["red","blue","magenta","pink","black"]
for a in range(5):
    #print(renkler[a])
    turtle.color(random.choice(renkler))
    turtle.forward(100)
    turtle.right(90)

input()