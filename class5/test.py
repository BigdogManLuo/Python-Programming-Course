import random
import math
import tkinter as tk

# 创建画布
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

# 绘制正方形和内接圆
square_size = 300
square_center = (canvas_width/2, canvas_height/2)
square_coords = (square_center[0]-square_size/2, square_center[1]-square_size/2,
                 square_center[0]+square_size/2, square_center[1]+square_size/2)
canvas.create_rectangle(square_coords, outline='black')
canvas.create_oval(square_coords, outline='black')

# 计算正方形和内接圆的面积和半径
square_area = square_size**2
circle_radius = square_size/2

# 生成随机点并绘制
num_points = 2000
num_points_in_circle = 0
for i in range(num_points):
    x = random.uniform(square_coords[0], square_coords[2])
    y = random.uniform(square_coords[1], square_coords[3])
    distance = math.sqrt((x-square_center[0])**2 + (y-square_center[1])**2)
    if distance <= circle_radius:
        canvas.create_oval(x, y, x+1, y+1, fill='red')
        num_points_in_circle += 1
    else:
        canvas.create_oval(x, y, x+1, y+1, fill='blue')
    canvas.update()
    canvas.after(3)
    
    if i%50==1:
        # 估算圆周率
        pi_estimate = 4 * num_points_in_circle / i
        print('估算的圆周率为：', pi_estimate)

# 进入主循环
tk.mainloop()
