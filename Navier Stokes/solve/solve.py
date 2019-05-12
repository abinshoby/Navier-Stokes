import matplotlib.pyplot as plt
import numpy as np
import cv2




#du/dt = -(u.d)u- 1/rho*(dp) + vd^2u + F

# Gradeient: dp=(dp/dx,dp/dy)=== (p(i+1,j)-p(i-1,j))/2dx,(p(i,j+1)-p(i,j-1))/2dy
#Divergence; d.u=du/dx+dv/dy==== (u(i+1,j)-u(i-1,j))/2dx+(v(i,j+1)-v(i,j-1))/2dy)
#Laplacian: d^2p= d^2p/dx^2+d^2p/dy^2===== (p(i+1,j)-4*p(i,j)+p(i-1,j)+p(i,j+1)+p(i,j-1))/(dx)^2
rho=1.0
dx=0.1
dy=0.1
dt=0.1
F=1.0

rr=[100 for i in range(50)]
for i in range(50):
    rr.append(0)


P=np.asarray([rr for i in range(100)])#np.random.random((100, 100))  #pressure
U=np.random.random((100, 100))  #initial velocity

V=np.random.random((100, 100))

def Laplacian(P):#Laplacian: d^2p= d^2p/dx^2+d^2p/dy^2===== (p(i+1,j)-4*p(i,j)+p(i-1,j)+p(i,j+1)+p(i,j-1))/(dx)^2
    p=P[:]
    for j in range(1,len(p[0])-1):
        for i in range(1,len(p)-1):
          p[i][j]= p[i+1][j]-4*p[i][j]+p[i-1][j]+p[i][j+1]+p[i][j-1]
    p=np.asarray(p)/(dx**2)
    return p
# p=Laplacian(P)
# plt.imshow(p)
# plt.show()

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
    return np.asarray([px/(2*dx),py/(2*dy)])

plt.imshow(P)
plt.show()

dun=U.copy()
diffn=1
diff=0
du=None
while(diffn-diff!=0):
    diff=diffn
    grad=(Gradient_Divergence(P))
    divergence=(Gradient_Divergence(U))
    plt.imshow(P)
    plt.show()


    # plt.imshow(np.asarray(grad[0]))
    # plt.imshow(np.asarray(grad[1]))
    # plt.show()

    # plt.imshow(divergence[0])
    # plt.imshow(divergence[1])
    # plt.show()




    #du/dt = -(u.d)u- 1/rho*(dp) + vd^2u + F

    #print("dp:",grad)

    dux=dt*((-1/rho)*grad[0]+V[0]*divergence[0]**2+F-divergence[0])*dx
    duy=dt*((-1/rho)*grad[1]+V[1]*divergence[1]**2+F-divergence[1])*dy
    # plt.imshow(dux)
    # plt.show()
    du=dux+duy
    # plt.imshow()
    # plt.show()
    # print(du)
    # print(divergence)
    # U=U+divergence
    # print(U)
    # P=P+grad
    diffn=(np.sum(du)-np.sum(dun))/np.sum(du)
    print(diffn)
    
    plt.imshow(du)
    plt.show()