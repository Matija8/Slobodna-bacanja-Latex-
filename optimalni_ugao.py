from teta1_2 import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time

#TODO sredi module (izbaci main, sredi brojke)

def optimalni_ugao(d_c, r_l, r_o, g, H):
    min_teta = max(atan(H/d_c) + prebaci_u_radijan(5), prebaci_u_radijan(45))
    max_teta = prebaci_u_radijan(60)
    opt_teta = min_teta
    opt_razlika = 0
    start = time.time()
    for ugao in np.arange(min_teta, max_teta, 0.0001):
        teta1, teta2 = nadji_teta1_teta2(ugao, d_c, r_l, r_o, g, H)
        if teta2 - teta1 > opt_razlika:
            opt_teta = ugao
            opt_razlika = teta2 - teta1
    end = time.time()
    #print(end - start)
    return opt_teta



if __name__ == "__main__":
    d_c = 4.15      # daljina do centra obruca
    r_l = 0.1213    # poluprecnik lopte
    r_o = 0.23      # poluprecnik obruca
    g = 9.81        # gravitaciona konstanta
    hk = 3.05       # visina kosa
    h = 1.95        # visina kosarkasa
    H = hk-5.0/4*h  # popravljena visina kosa

    teta = optimalni_ugao(d_c, r_l, r_o, g, H)
    print(prebaci_u_stepen(teta))
