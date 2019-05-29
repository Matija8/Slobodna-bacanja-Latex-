from math import *
import numpy as np
import matplotlib.pyplot as plt


def nadji_teta1_teta2(teta, d_c, r_l, r_o, g, H):
    # uslov (8)
    if not atan(H/d_c) < teta < pi/2:
        return teta, teta
    v = nadji_brzinu(d_c, teta, H, g)

    min_teta = max(asin(sqrt(2*g*H/v**2)), atan(H/d_c))
    max_teta = prebaci_u_radijan(85)    # TODO
    ugao_korak = 0.001
    t1 = (d_c - r_o - r_l) / (v * cos(teta))
    t2 = (d_c - r_o + r_l) / (v * cos(teta))
    t_korak = 0.1
    teta1 = teta2 = teta
    stani = False
    #print( nadji_distancu(v, teta, H, g)) TODO

    for ugao in np.arange(teta, min_teta, -ugao_korak):
        if not d_c - r_o + r_l < nadji_distancu(v, ugao, H, g) < d_c + r_o - r_l:
            teta1 = ugao
            break
        for t in np.arange(t1, t2, t_korak):  # TODO
            if not ((x_koord(t, v, ugao) - (d_c - r_o))**2 + (y_koord(t, v, ugao, g))**2 > r_l**2):
                teta1 = ugao
                stani = True
                break
        if stani is True:
            break

    stani = False

    for ugao in np.arange(teta, max_teta, ugao_korak):
        if not d_c - r_o + r_l < nadji_distancu(v, ugao, H, g) < d_c + r_o - r_l:
            teta2 = ugao
            break
        for t in np.arange(t1, t2, t_korak):  # TODO
            if not ((x_koord(t, v, ugao) - (d_c - r_o)) ** 2 + (y_koord(t, v, ugao, g)) ** 2 > r_l ** 2):
                teta2 = ugao
                stani = True
                break
            if stani is True:
                break

    return teta1, teta2


def prebaci_u_stepen(alfa):
    return alfa * 180 / pi


def prebaci_u_radijan(alfa):
    return alfa * pi / 180


def x_koord(t, v, teta):
    return v * cos(teta) * t


def y_koord(t, v, teta, g):
    return v * sin(teta) * t - g * t**2 / 2


def nadji_brzinu(d, teta, y, g):
    return sqrt(g * (d**2) / (2 * cos(teta) ** 2 * (d * tan(teta) - y)))


def nadji_distancu(v, teta, H, g):
    #proveru (5) vrsimo pre poziva
    return v*cos(teta)/g*(v*sin(teta)+sqrt(v**2*sin(teta)**2 - 2*g*H))


if __name__ == "__main__":
    d_c = 4.15      # daljina do centra obruca
    r_l = 0.1213    # poluprecnik lopte
    r_o = 0.23      # poluprecnik obruca
    g = 9.81        # gravitaciona konstanta
    hk = 3.05       # visina kosa
    h = 1.95        # visina kosarkasa
    H = hk-5.0/4*h  # popravljena visina kosa

    teta = prebaci_u_radijan(30)
    (teta_1, teta_2) = nadji_teta1_teta2(teta, d_c, r_l, r_o, g, H)
    print(prebaci_u_stepen(teta_1), prebaci_u_stepen(teta_2))
