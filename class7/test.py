import numpy as np
import imageio
import matplotlib.pyplot as plt


image = imageio.imread('img/example.jpg')

#展示一下原图
plt.imshow(image)
plt.show()


def mosaic_effect(image, block_size):
    '''
    

    Parameters
    ----------
    image : 输入图片
    block_size : 马赛克的大小，越大越模糊

    Returns
    -------
    mosaic_image : TYPE
        DESCRIPTION.

    '''
    rows, cols, _ = image.shape
    mosaic_image = np.zeros_like(image) #定义了一个559x621x3全0数组

    #打马赛克
    for i in range(0, rows, block_size):  #从0到整行 以block_size为步长
        for j in range(0, cols, block_size): #从0到整列 以block_size步长
            
            block = image[i:i+block_size, j:j+block_size] #圈定出要做马赛克的区域
           
            avg_color = block.mean(axis=(0, 1))  #找到平均值
            mosaic_image[i:i+block_size, j:j+block_size] = avg_color  #把圈出来的这块区域用平均值替代

    return mosaic_image

block_size = 5 # 马赛克大小为10


#调用我们刚刚写的函数，做马赛克操作
mosaic_image = mosaic_effect(image, block_size)

#展示一下打了马赛克的照片
plt.imshow(mosaic_image)
plt.show()







