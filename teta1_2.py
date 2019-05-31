from math import *
import numpy as np
import matplotlib.pyplot as plt


def nadji_teta1_teta2(teta, d_c, r_l, r_o, g, H):
    # uslov (8)
    if not atan(H/d_c) + prebaci_u_radijan(1) < teta < prebaci_u_radijan(90):
        return teta, teta

    v = nadji_brzinu(d_c, teta, H, g)
    # uslov (5)
    min_teta = max(asin(sqrt(2*g*H/v**2)), atan(H/d_c)) + prebaci_u_radijan(1)
    max_teta = prebaci_u_radijan(90)

    ugao_korak = prebaci_u_radijan(1)  # prvo nam je 1 stepen korak
    teta1 = uslovi_11_i_12(teta, min_teta, -ugao_korak, d_c, r_l, r_o, g, H, v)

    ugao_korak = prebaci_u_radijan(0.01)  # zatim 0.01 stepen, ali sad idemo od teta1
    teta1 = uslovi_11_i_12(teta1, min_teta, -ugao_korak, d_c, r_l, r_o, g, H, v)

    ugao_korak = prebaci_u_radijan(1)  # prvo nam je 1 stepen korak
    teta2 = uslovi_11_i_12(teta, max_teta, ugao_korak, d_c, r_l, r_o, g, H, v)

    ugao_korak = prebaci_u_radijan(0.01)  # zatim trazimo preciznije od teta2 do max_teta, k = 0.01
    teta2 = uslovi_11_i_12(teta2, max_teta, ugao_korak, d_c, r_l, r_o, g, H, v)

    return teta1, teta2


def uslovi_11_i_12(od, do, korak, d_c, r_l, r_o, g, H, v):
    teta1_2 = od

    stani = False

    # uslov (11)
    for ugao in np.arange(od, do, korak):
        if not d_c - r_o + r_l < nadji_distancu(v, ugao+korak, H, g) < d_c + r_o - r_l:
            teta1_2 = ugao
            break

        # uslov (12)
        t1 = (d_c - r_o - r_l) / (v * cos(ugao+korak))
        t2 = (d_c - r_o + r_l) / (v * cos(ugao+korak))
        for t in np.linspace(t1, t2, 10):
            if not (((x_koord(t, v, ugao+korak) - (d_c - r_o))**2
                    + (y_koord(t, v, ugao+korak, g) - H)**2) > (r_l**2)):
                teta1_2 = ugao
                stani = True
                break

        if stani is True:
            break

    return teta1_2


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
    return v*cos(teta)/g*(v*sin(teta)+sqrt(v**2*sin(teta)**2 - 2*g*H))


if __name__ == "__main__":
    d_c = 4.19            # daljina do centra obruca
    r_l = 0.1213          # poluprecnik lopte
    r_o = 0.23            # poluprecnik obruca
    g = 9.81              # gravitaciona konstanta
    hk = 3.05             # visina kosa

    h = float(input("Unesite visinu kosarksa (u metrima): "))
    if not 0 < h < 3:
        print("Visina kosarkasa nije u korektnom rasponu (do 3 metra)!")
        exit()
    H = hk-5.0/4*h        # popravljena visina kosa

    teta = float(input("Unesite ugao teta (u stepenima): "))
    if not 0 < teta < 90:
        print("Ugao mora biti izmedju 0 i 90!")
        exit()
    (teta_1, teta_2) = nadji_teta1_teta2(prebaci_u_radijan(teta), d_c, r_l, r_o, g, H)
    print(f"teta1 = {prebaci_u_stepen(teta_1):.2f}, teta2 = {prebaci_u_stepen(teta_2):.2f}")
    # kraj programa
