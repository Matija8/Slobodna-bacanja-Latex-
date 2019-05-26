from math import *
import numpy as np
import matplotlib.pyplot as plt


def teta1_teta2(d_c, r_l, r_o, g, H):
    d_1 = d_c - r_o + r_l
    d_2 = d_c + r_o - r_l
    teta1, teta2 = (0, 1)
    return teta1, teta2


def to_degree(alfa):
    return alfa * 180 / pi


def to_radian(alfa):
    return alfa * pi / 180


if __name__ == "__main__":
    d_c = 4.15      # daljina do centra obruča
    r_l = 0.1213    # poluprečnik lopte
    r_o = 0.23      # poluprečnik obruča
    g = 9.81        # gravitaciona konstanta

    hk = 3.05       # visina koša
    h = 2.01        # visina košarkaša
    H = hk-5.0/4*h  # popravljena visina koša
    (teta_1, teta_2) = teta1_teta2(d_c, r_l, r_o, g, H)
    print(teta_1, teta_2)
