from teta1_2 import *
from math import *
import numpy as np
import matplotlib.pyplot as plt


def optimalni_ugao(d_c, r_l, r_o, g, H):
    return


if __name__ == "__main__":
    d_c = 4.15      # daljina do centra obruča
    r_l = 0.1213    # poluprečnik lopte
    r_o = 0.23      # poluprečnik obruča
    g = 9.81        # gravitaciona konstanta

    hk = 3.05       # visina koša
    h = 2.01        # visina košarkaša
    H = hk-5.0/4*h  # popravljena visina koša
    teta = optimalni_ugao(d_c, r_l, r_o, g, H)
    print(teta)
