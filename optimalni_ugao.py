from teta1_2 import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time


def optimalni_ugao(d_c, r_l, r_o, g, H):
    min_teta = max(atan(H/d_c) + prebaci_u_radijan(1), prebaci_u_radijan(20))
    max_teta = prebaci_u_radijan(70)  # moze i do 90 ali nema potrebe
    opt_teta = min_teta
    opt_razlika = 0
    korak_teta = prebaci_u_radijan(0.01)  # 0.01 stepen nam je korak
    start = time.time()

    for ugao in np.arange(min_teta, max_teta, korak_teta):
        teta1, teta2 = nadji_teta1_teta2(ugao, d_c, r_l, r_o, g, H)
        # ako sklonimo komentar ispod mozemo da vidimo teta2-teta1 za svaki ugao
        print(f"teta = {prebaci_u_stepen(ugao):.2f}, raz = {prebaci_u_stepen(teta2 - teta1):.3f}")
        if teta2 - teta1 > opt_razlika:
            opt_teta = ugao
            opt_razlika = teta2 - teta1

    end = time.time()
    print(f"Vreme trajanja programa: {(end - start):.4} s")  # ispisuje vreme trajanja programa u sekundama
    return opt_teta


if __name__ == "__main__":
    d_c = 4.19            # daljina do centra obruca
    r_l = 0.75/(2*pi)     # poluprecnik lopte
    r_o = 0.23            # poluprecnik obruca
    g = 9.81              # gravitaciona konstanta
    hk = 3.05             # visina kosa

    h = float(input("Unesite visinu kosarksa (u metrima): "))
    if not 0 < h < 3:
        print("\nVisina kosarkasa nije u korektnom rasponu (do 3 metra)")
        exit()
    H = hk-5.0/4*h        # popravljena visina kosa

    teta = optimalni_ugao(d_c, r_l, r_o, g, H)
    print(f"\nOptimalni ugao teta = {prebaci_u_stepen(teta):.4f}")
    # kraj programa
