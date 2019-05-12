import matplotlib.pyplot as plt
import numpy as np
import cv2
# data = np.array([mpimg.imread(name) for name in os.listdir('images/sample_images/')], dtype=np.float64)
image = cv2.imread('fluid.jpeg', cv2.IMREAD_COLOR)
#X = np.random.random((100, 100)) # sample 2D array
X=np.asarray(image)
print(X[:][:])
plt.imshow(X[:][:])
X=X[:][:]
plt.show()



#du/dt = -(u.d)u- 1/rho*(dp) + vd^2u + F

# Gradeient: dp=(dp/dx,dp/dy)=== (p(i+1,j)-p(i-1,j))/2dx,(p(i,j+1)-p(i,j-1))/2dy
#Divergence; d.u=du/dx+dv/dy==== (u(i+1,j)-u(i-1,j))/2dx+(v(i,j+1)-v(i,j-1))/2dy)
#Laplacian: d^2p= d^2p/dx^2+d^2p/dy^2===== (p(i+1,j)-4*p(i,j)+p(i-1,j)+p(i,j+1)+p(i,j-1))/(dx)^2
dx=1
dy=1
P=np.random.random((100, 100))  #pressure
U=np.random.random((100, 100))  #initial velocity
def Gradient_Divergence(A):#Gradeient: dp=(dp/dx,dp/dy)=== (p(i+1,j)-p(i-1,j))/2dx,(p(i,j+1)-p(i,j-1))/2dy
    px=A[:]                    #Divergence; d.u=du/dx+dv/dy==== (u(i+1,j)-u(i-1,j))/2dx+(v(i,j+1)-v(i,j-1))/2dy)
    py=A[:]
    for j in range(len(px[0])):
        for i in range(1,len(px)-1):
            px[i][j]=px[i+1][j]-px[i-1][j]
    for i in range(len(px)):
        for j in range(1,len(px[0])-1):
            px[i][j]=px[i][j+1]-px[i][j-1]
    px=np.asarray(px)
    py=np.asarray(py)
    return ((px/(2*dx)).tolist(),(py/(2*dy)).tolist())

grad=(Gradient_Divergence(P))
divergence=(Gradient_Divergence(U))
# plt.imshow(P)
# plt.show()
plt.imshow(np.asarray(grad[0]))
plt.imshow(np.asarray(grad[1]))
plt.show()

plt.imshow(divergence[0])
plt.imshow(divergence[1])
plt.show()

def Laplacian(P):#Laplacian: d^2p= d^2p/dx^2+d^2p/dy^2===== (p(i+1,j)-4*p(i,j)+p(i-1,j)+p(i,j+1)+p(i,j-1))/(dx)^2
    p=P[:]
    for j in range(1,len(p[0])-1):
        for i in range(1,len(p)-1):
          p[i][j]= p[i+1][j]-4*p[i][j]+p[i-1][j]+p[i][j+1]+p[i][j-1]
    p=np.asarray(p)/(dx**2)
    return p
p=Laplacian(P)
plt.imshow(p)
plt.show()




        
        


