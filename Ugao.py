import math as m
import numpy as np
import matplotlib.pyplot as plt

# Opsti Podaci:
# d - rastojanje od y ose do centra kosa
# g - gravitaciona konstanta
# H - visina kosa u odnosu na koor. pocetak
# r - polupr. lopte
# obruc - poluprecnik obruca


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
    print(f"x = {d:.4}")
    print(f"y = {H:.4}")
    d_1 = d - obruc + r
    d_2 = d + obruc - r

    min_teta = max(m.atan(H/d), 0)
    max_teta = to_radian(90)
    #for teta in np.arange(min_teta, max_teta, to_radian(1)):
    #    print(to_degree(teta))
    teta = to_radian(60)

    v = nadji_brzinu(d, teta, H, g)
    #Brzina neophodna da bi lopta prosla kroz centar obruca pri uglu teta
    print(f"Vo = {v:.4}")

    #plot idealne putanje
    plot_putanje(d, v, teta, g, d_1, d_2, H)

    teta1 = nadji_ugao(d_1, v, H, g, teta)
    print(to_degree(teta1))


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
    plt.plot(vektor_x, vektor_y)
    #ivice obruca
    plt.plot([d_1, d_2], [H, H], 'r.')
    plt.show()


def nadji_brzinu(d, teta, y, g):
    return m.sqrt((g * (d**2)) / (2 * (m.cos(teta) ** 2) * (d * m.tan(teta) - y)))


def nadji_ugao(d, v, y, g, teta):
    ugao1 = m.atan((v**2 + m.sqrt(v**4 - g*(g*(d**2) + 2*y*(v**2)))) / (g*d))
    ugao2 = m.atan((v**2 + m.sqrt(v**4 - g*(g*(d**2) + 2*y*(v**2)))) / (g*d))
    return ugao1


if __name__ == "__main__":
    main()
