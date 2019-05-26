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
    d_c = 4.15      # daljina do centra obruca
    r_l = 0.1213    # poluprecnik lopte
    r_o = 0.23      # poluprecnik obruca
    g = 9.81        # gravitaciona konstanta

    hk = 3.05       # visina kosa
    h = 2.01        # visina kosarkasa
    H = hk-5.0/4*h  # popravljena visina kosa
    (teta_1, teta_2) = teta1_teta2(d_c, r_l, r_o, g, H)
    print(teta_1, teta_2)
