import time
from pynput import mouse
from pynput import keyboard

M=mouse.Controller() #创建一个鼠标对象
K=keyboard.Controller() #创建一个键盘对象

print(M.position)

#找到QQ下拉框（1621，5）
M.position=(1400,0)


#找到对话联系人（1680，277）
time.sleep(0.5)
M.position=(1400,277)


#双击聊天框
M.click(mouse.Button.left, 2)

#定位到聊天栏（1059，625）
M.position=(800,625)
time.sleep(0.5)


#点击聊天栏
time.sleep(0.5)
M.click(mouse.Button.left, 1)
#输入对话
time.sleep(0.5)
K.type("hello,world!")
time.sleep(0.5)

#发送（ctrl+enter）
K.press(keyboard.Key.ctrl_l)
K.press(keyboard.Key.enter)
K.release(keyboard.Key.enter)
K.release(keyboard.Key.ctrl_l)