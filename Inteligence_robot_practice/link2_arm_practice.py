import numpy as np
import math
import matplotlib.pyplot as plt
import pdb
L1=1.0
L2=1.0
Epsilon = 1.0e-12
def link_one_X(theta1):
  return L1*math.cos(theta1)
def link_one_Y(theta1):
  return L1*math.sin(theta1)
def X(theta1, theta2):
    return L1*math.cos(theta1)+L2*math.cos(theta1+theta2)
def Y(theta1, theta2):
    return L1*math.sin(theta1)+L2*math.sin(theta1+theta2)
def Jacobian(q):
    theta1 = q[0]
    theta2 = q[1]
    dxdtheta1 = -L1*math.sin(theta1)-L2*math.sin(theta1+theta2)/Epsilon
    dxdtheta2 = -L2*math.sin(theta1+theta2)/Epsilon
    dydtheta1 = L1*math.cos(theta1)+L2*math.cos(theta1+theta2)/Epsilon
    dydtheta2 = L2*math.cos(theta1+theta2)/Epsilon
    return np.array([[dxdtheta1, dxdtheta2],[dydtheta1, dydtheta2]])
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
  plt.xlim(-2.0,2.0)
  plt.ylim(-2.0,2.0)
  plt.grid()
  plt.legend(fontsize=20) # 凡例
  plt.show()

def distance(u,v):
    return np.linalg.norm(u-v)
def Tstar(q):
  return np.array([[X(q[0],q[1])], [Y(q[0],q[1])]])
def main():
    T = np.array([[1.0], [1.0]])
    
    q= np.array([[np.pi/3.0], [-np.pi/3.0]])
    x=(0,link_one_X(q[0]),X(q[0],q[1]))
    y=(0,link_one_Y(q[1]),Y(q[0],q[1]))
    plot(x,y)
    while distance(T, Tstar(q)) > Epsilon:
        th1 = q[0]
        th2 = q[1]
        deltaT = T-Tstar(q)
        J = Jacobian(q)
        Jinv = np.linalg.inv(J)
        
        q += np.matmul(Jinv,deltaT)
        print(q)
        print(X(q[0],q[1]))
        print(Y(q[0],q[1]))
        x=(0,link_one_X(q[0]),X(q[0],q[1]))
        y=(0,link_one_Y(q[0]),Y(q[0],q[1]))
        plot(x,y)
if __name__ == "__main__":
  main()
