import turtle

# Xác định kích thước bút và màu bút
turtle.pensize(6)
turtle.pencolor("blue")

# Vẽ hình tròn cho khuôn mặt
face_size = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(face_size)

# Vẽ mắt
eye_size = 20
turtle.fillcolor ("red")

# Vẽ mắt phải
turtle.begin_fill()
turtle.penup()
turtle.goto(100,50)
turtle.pendown()
turtle.circle(eye_size)
turtle.end_fill()

# Vẽ mắt trái
turtle.begin_fill()
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.circle(eye_size)
turtle.end_fill()

# Vẽ mũi
turtle.fillcolor ("yellow")
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(-70, steps=3)
turtle.end_fill()

# Vẽ miệng
turtle.penup()
turtle.goto(-100,-70)
turtle.pendown()
turtle.right(90)
turtle.circle(100,180)



turtle.done()