import numpy as np
import math
import matplotlib.pyplot as plt
import pdb

L1=1.0
L2=1.0
L3=1.0
Epsilon = 1.0e-12
def link_one_X(theta1):
  return L1*math.cos(theta1)
def link_one_Y(theta1):
  return L1*math.sin(theta1)

def link_two_X(theta1,theta2):
  return L1*math.cos(theta1)+L2*math.cos(theta1+theta2)
def link_two_Y(theta1,theta2):
  return L1*math.sin(theta1)+L2*math.sin(theta1+theta2)

def link_three_X(theta1,theta2,theta3):
  return L1*math.cos(theta1)+L2*math.cos(theta1+theta2)+L3*math.cos(theta1+theta2+theta3)
def link_three_Y(theta1,theta2,theta3):
  return L1*math.sin(theta1)+L2*math.sin(theta1+theta2)+L3*math.sin(theta1+theta2+theta3)

def X(theta1, theta2, theta3):
    return L1*math.cos(theta1)+L2*math.cos(theta1+theta2)+L3*math.cos(theta1+theta2+theta3)

def Y(theta1, theta2, theta3):
    return L1*math.sin(theta1)+L2*math.sin(theta1+theta2)+L3*math.sin(theta1+theta2+theta3)

def Jacobian(q):
    theta1 = q[0]
    theta2 = q[1]
    theta3 = q[2]
    dxdtheta1 = -L1*math.sin(theta1)-L2*math.sin(theta1+theta2)-L3*math.sin(theta1+theta2+theta3)
    dxdtheta2 = -L2*math.sin(theta1+theta2)-L3*math.sin(theta1+theta2+theta3)
    dxdtheta3 = -L3*math.sin(theta1+theta2+theta3)

    dydtheta1 = L1*math.cos(theta1)+L2*math.cos(theta1+theta2)+L3*math.cos(theta1+theta2+theta3)
    dydtheta2 = L2*math.cos(theta1+theta2)+L3*math.cos(theta1+theta2+theta3)
    dydtheta3 = L3*math.cos(theta1+theta2+theta3)
    return np.array([[dxdtheta1, dxdtheta2, dxdtheta3],[dydtheta1, dydtheta2, dydtheta3]])

# グラフの描画
def plot(x, y):
  fn = "Times New Roman"
  # グラフ表示の設定
  fig = plt.figure()
  
  ax = fig.add_subplot(111,facecolor="w")
  ax.tick_params(labelsize=13) # 軸のフォントサイズ
  plt.xlabel("$x [m]$", fontsize=20, fontname=fn)
  plt.ylabel("$y [m]$", fontsize=20, fontname=fn)
  plt.plot(x, y,"-g",lw=5,label="link") # リンクの描画
  plt.plot(x, y,"or",lw=5, ms=10,label="joint") # 関節の描画
  plt.xlim(-3.0,3.0)
  plt.ylim(-3.0,3.0)
  plt.grid()
  plt.legend(fontsize=20) # 凡例
  plt.show()
def plot_o(x, y, obstacle):
  fn = "Times New Roman"
  # グラフ表示の設定
  fig = plt.figure()
  
  ax = fig.add_subplot(111,facecolor="w")
  ax.tick_params(labelsize=13) # 軸のフォントサイズ
  plt.xlabel("$x [m]$", fontsize=20, fontname=fn)
  plt.ylabel("$y [m]$", fontsize=20, fontname=fn)
  plt.plot(x, y,"-g",lw=5,label="link") # リンクの描画
  plt.plot(x, y,"or",lw=5, ms=10,label="joint") # 関節の描画
  
  plt.scatter(obstacle[0,0],obstacle[0,1],color="r")
  plt.xlim(-3.0,3.0)
  plt.ylim(-3.0,3.0)
  plt.grid()
  plt.legend(fontsize=20) # 凡例
  
  plt.show()
def distance(u,v):
    return np.linalg.norm(u-v)
def Tstar(q):
  return np.array([[X(q[0],q[1],q[2])], [Y(q[0],q[1],q[2])]])
def main():
    T = np.array([[2.0], [1.0]])
    
    
    q= np.array([[np.pi/3.0], [-np.pi/3.0], [1/3.0]])
    x=(0,link_one_X(q[0]),link_two_X(q[0],q[1]),link_three_X(q[0],q[1],q[2]))
    y=(0,link_one_Y(q[0]),link_two_Y(q[0],q[1]), link_three_Y(q[0],q[1],q[2]))
    
    nabla_x=[x,y]
    
    while distance(T, Tstar(q)) > Epsilon:
        th1 = q[0]
        th2 = q[1]
        th3 = q[2]
        
        xd=T-Tstar(q)
        J=Jacobian(q)
        Js = np.linalg.pinv(J)
        qd0 = q+np.sqrt(np.linalg.det(np.matmul(J,J.T)))
        
        q += np.matmul(Js,xd)+np.matmul((np.identity(J.shape[1])-np.matmul(Js,J)),qd0)

    x=(0,link_one_X(q[0]),link_two_X(q[0],q[1]),link_three_X(q[0],q[1],q[2]))
    y=(0,link_one_Y(q[0]),link_two_Y(q[0],q[1]), link_three_Y(q[0],q[1],q[2]))
    plot(x,y)
    
    #障害物回避
    obstacle=np.array([[1.5,0.0]])
    for i in range(2):#障害物よける行動
      x1=np.array([[link_one_X(q[0]),link_one_Y(q[0])]])
      x2=np.array([[link_two_X(q[0],q[1]),link_two_Y(q[0],q[1])]])
      nx1=x1-obstacle
      nx2=x2-obstacle
      J=Jacobian(q)#[2,3]
      Js = np.linalg.pinv(J)
      xd=T-Tstar(q)
      qd0=q+np.matmul(J[:,1].T,nx2.T)[0]
      
      q += np.matmul(Js,xd)+np.matmul((np.identity(J.shape[1])-np.matmul(Js,J)),qd0)
      x=(0,link_one_X(q[0]),link_two_X(q[0],q[1]),link_three_X(q[0],q[1],q[2]))
      y=(0,link_one_Y(q[0]),link_two_Y(q[0],q[1]), link_three_Y(q[0],q[1],q[2]))
      
    plot_o(x,y,obstacle)
    print()
if __name__ == "__main__":
  main()
