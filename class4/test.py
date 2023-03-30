import random
import matplotlib.pyplot as plt

#创建一个 100x100的列表

n=150

A=[[0]*(n) for i in range(n)]  #这个语句暂时不用理解


#初始化世界
for i in range(n):
    for j in range(n):
        A[i][j]=random.choice([0,1])



#展示最初的形态
fig=plt.figure()
plt.axis('off')
im=plt.imshow(A,cmap="Greens")
        

#遍历整个列表
for k in range(1000):
    newA=[[0]*(n) for i in range(n)]
    #世界更新规则
    for i in range(1,n-1):
        for j in range(1,n-1):
            #繁殖规则：
            if A[i-1][j]+A[i][j-1]+A[i][j+1]+A[i+1][j]+A[i-1][j-1]+A[i-1][j+1]+A[i+1][j-1]+A[i+1][j+1]==3:
                newA[i][j]=1
            elif A[i-1][j]+A[i][j-1]+A[i][j+1]+A[i+1][j]+A[i-1][j-1]+A[i-1][j+1]+A[i+1][j-1]+A[i+1][j+1]<2:
                newA[i][j]=0
            elif A[i-1][j]+A[i][j-1]+A[i][j+1]+A[i+1][j]+A[i-1][j-1]+A[i-1][j+1]+A[i+1][j-1]+A[i+1][j+1]==2:
                newA[i][j]=A[i][j]
            elif A[i-1][j]+A[i][j-1]+A[i][j+1]+A[i+1][j]+A[i-1][j-1]+A[i-1][j+1]+A[i+1][j-1]+A[i+1][j+1]>3:
                newA[i][j]=0
    
    A=newA
    
    
    #可视化
    im.set_data(A)
    plt.pause(0.2)
    
plt.show()