import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import cos
from math import pi

# pour crée l'animation:
# convert -delay 100 -loop 0 M5P5*.png M5P5_animation.gif

def draw_result(lst_x, lst_y, title):
    plt.plot(lst_x, lst_y, '-b')

    plt.xlabel("x")
    plt.legend(loc='center')
    plt.title(title)
    plt.grid()
    plt.savefig(title+".png")  # should before plt.show method

    plt.show(block=False)
    #plt.show()
    plt.close()

PROFONDEUR = 1000 
LIMITE = 1e-5 # pour limiter les calculs
def R(x, a, b):
  Rx = 0
  
  for n in range(0, PROFONDEUR):
    an = pow(a, n) * cos(pow(b,n) * pi * x) 
    Rx += an
    if abs(an) < LIMITE:
      break 

  return Rx


def Plot(xmin, xmax, title, a, b):
  if (a*b <= 2*pi + 1) or (b < 0) or (b%4 != 0) or (a<0) or (a>1):
    print("Invalide ! a=" + str(a) + " b=" + str(b))
    exit(666)


  NBPTS = 1000
  #xincr = 0.000001
  xincr = (xmax-xmin) / (NBPTS-1)
  x = xmin

  xs = []
  ys = []
  pts = 0
  while x <= xmax:
    y = R(x, a, b)
    xs.append(x)
    ys.append(y)
    x += xincr
    pts += 1

  draw_result(xs, ys, title)

if __name__ == "__main__":
  # a: joue sur l'amplitude
  # b: joue sur la fréquence 

  #for _b in range(16, 41, 4):
    #Plot(-50, 50, "Weierstrass_a_0.5_b_" + str(_b), 0.5, _b)

  #for _b in range(16, 41, 4):
    #Plot(-5, 5, "Weierstrass_a_0.5_b_" + str(_b), 0.5, _b)

  #for _b in range(16, 41, 4):
      #Plot(-1, 1, "Weierstrass_a_0.5_b_" + str(_b), 0.5, _b)
    Plot(-1, 1, "Weierstrass_a_0.9_b_24", 0.9, 24)
    #Plot(-0.1, 0.1, "Weierstrass_a_0.7_b_24", 0.7, 24)
    #Plot(-0.01, 0.01, "Weierstrass_a_0.7_b_24", 0.7, 24)
