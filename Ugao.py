import math as m
import numpy as np
import matplotlib.pyplot as plt

# Opsti Podaci:
# d - rastojanje od y ose do centra kosa
# r - polupr. lopte
# obruc - poluprecnik obruca
# g - gravitaciona konstanta
# h - visina kosarkasa
# hk - visina kosa
# H - visina kosa u odnosu na koor. pocetak


def main():

    d = 4.15
    r = 0.1213
    obruc = 0.23
    g = 9.81
    h = 2.01
    #h = int(input("Unesite visinu igraca: "))
    hk = 3.05

    H = hk - 5.0/4 * h
    #print(f"Kos je za {H:.4} m visi od izbacaja kosarkasa")
    #print(f"x = {d:.4}")
    #print(f"y = {H:.4}")
    # Ivice obruca. d_1 bliza, d_2 dalja ivica
    d_1 = d - obruc + r
    d_2 = d + obruc - r
    print(d_1, d_2)

    # TODO Pokazujemo da ugao mora biti veci od atan(H/d) da bi dobacili
    #plot_putanje(d, 100, m.atan(H/d), g, d_1, d_2, H)
    #plt.show()
    #return

    # TODO Pokazujemo da ugao mora biti veci od asin(H/d)
    #v = 100
    #plot_putanje(d, v, m.asin(m.sqrt(2*g*H/(v**2))), g, d_1, d_2, H)
    #plt.show()
    #return

    # Trazimo za svako moguce teta razliku teta2-teta1
    # teta su u rasponu od atan(H/d) do 90
    min_teta = max(m.atan(H/d) + to_radian(1), to_radian(1))
    #min_teta = to_radian(45)
    max_teta = to_radian(80)
    optimalno_teta = min_teta
    optimalna_razlika = 0
    for teta in np.arange(min_teta, max_teta, to_radian(1)):
    #for teta in [to_radian(60)]:

        # Brzina neophodna da bi lopta prosla kroz centar obruca pri uglu teta
        print(to_degree(teta))
        v = nadji_brzinu(d, teta, H, g)
        print(f"Vo = {v:.4}")
        #plot_putanje(d, v, teta, g, d_1, d_2, H)
        #plt.show()
        #return

        (teta1, teta2) = nadji_uglove_iterativno(d_1, d_2, v, H, g, teta)
        print(f"Uglovi su {to_degree(teta1):.4}, {to_degree(teta2):.4}")

        if abs(teta2 - teta1) > optimalna_razlika:
            optimalna_razlika = abs(teta2 - teta1)
            optimalno_teta = teta

        print(f"Optimalno teta je {to_degree(optimalno_teta):.4}")
        print(f"Optimalna razlika teta2 - teta1 = {to_degree(optimalna_razlika):.8}")

        #prikaz svih grafika
        #plot_putanje(d, v, teta, g, d_1, d_2, H)
        #plot_putanje(d_2, v, teta1, g, d_1, d_2, H)
        #plot_putanje(d_2, v, teta2, g, d_1, d_2, H)
        #plt.show()

    # plot uglova
    plot_putanje(d, v, teta, g, d_1, d_2, H)
    plot_putanje(d_2, v, teta1, g, d_1, d_2, H)
    plot_putanje(d_2, v, teta2, g, d_1, d_2, H)
    plt.show()


def to_degree(alfa):
    return alfa * 180 / m.pi


def to_radian(alfa):
    return alfa * m.pi / 180


def x_koord(v, teta, t):
    return v * m.cos(teta) * t


def y_koord(v, teta, t, g):
    return v * m.sin(teta) * t - g * t**2 / 2


def plot_putanje(d, v, teta, g, d_1, d_2, H):
    T = d / (v*m.cos(teta))
    print(f"vreme leta lopte je {T:.4} sekundi")
    vektor_t = np.arange(0, T, 0.01)
    vektor_x = [x_koord(v, teta, t) for t in vektor_t]
    vektor_y = [y_koord(v, teta, t, g) for t in vektor_t]
    #axes = plt.gca()
    #axes.set_xlim([-0.1, 5])
    #axes.set_ylim([-0.1, 1.5])
    plt.plot(vektor_x, vektor_y)
    # ivice obruca
    plt.plot([d_1, d_2], [H, H], 'r.')


def nadji_brzinu(d, teta, y, g):
    return m.sqrt((g * (d**2)) / (2 * (m.cos(teta) ** 2) * (d * m.tan(teta) - y)))


def nadji_distancu(v, teta, H, g):
    #ako vazi ovaj uslov onda lopta nece dostici visinu kosa
    if (v*m.sin(teta))**2 <= 2*g*H:
        return float('nan')
    # izrazili smo T preko y (y(T) = H)
    # uzimamo + u resenju kvadratne jne jer trazimo t kada je lopta u padu
    T = (v*m.sin(teta) + m.sqrt((v*m.sin(teta))**2 - 2*g*H)) / g
    return x_koord(v, teta, T)


def nadji_uglove_iterativno(d_1, d_2, v, H, g, teta):
    # trazimo iterativno teta za koje je (x, y) = (d_1, H) i (x, y) = (d_2, H)
    # x == d u daljem kodu
    teta_1 = teta
    teta_2 = teta
    # korak za teta = 0.01 stepen
    dt = to_radian(0.01)
    # inicijalno d
    d_init = nadji_distancu(v, teta, H, g)
    if not d_1 < d_init < d_2:
        #raise Exception("Pri ovom uglu i brzini lopta ne upada u kos uopste!")
        teta_1 = teta
    d = d_init

    while d_1 < d < d_2:
        teta_1 -= dt
        d = nadji_distancu(v, teta_1, H, g)

    d = d_init

    while d_1 < d < d_2:
        teta_2 += dt
        d = nadji_distancu(v, teta_2, H, g)

    return teta_1, teta_2


def nadji_ugao_nacin2(d, v, y, g, teta):
    #ugao1 = m.atan((v**2 + m.sqrt(v**4 - g*(g*(d**2) + 2*y*(v**2)))) / (g*d))
    #ugao2 = m.atan((v**2 + m.sqrt(v**4 - g*(g*(d**2) + 2*y*(v**2)))) / (g*d))
    return


if __name__ == "__main__":
    main()
