import math as m
import numpy as np

# Opsti Podaci:
# d - rastojanje od y ose do centra kosa
# g - gravitaciona konstanta
# H - visina kosa u odnosu na koor. pocetak
# r - polupr. lopte
# obruc - poluprecnik obruca


def main():

    r = 0.1213
    obruc = 0.23
    g = 9.81
    h = 2.01
    #h = int(input("Unesite visinu igraca: "))
    H = 3.05 - 5.0/4 * h
    #print(f"Kos je za {H:.4} m visi od izbacaja kosarkasa")
    d = 4.15
    d_1 = d - obruc + r
    d_2 = d + obruc - r

    min_teta = max(m.atan(H/d), 0)
    max_teta = to_radian(90)
    #for teta in np.arange(min_teta, max_teta, to_radian(1)):
    #    print(to_degree(teta))
    teta = to_radian(60)

    v = nadji_brzinu(d, teta, H, g)

    #print(f"Brzina neophodna da bi lopta prosla kroz centar obruca pri uglu od "
    #      f"{to_degree(teta):.4} stepeni je {v:.4} m/s^2")

    #T = d / (v*m.cos(teta))
    #print(f"vreme leta lopte je {T:.4} sekundi")

    teta1 = nadji_ugao(d_1, v, H, g, teta)
    print(to_degree(teta1))


def to_degree(alfa):
    return alfa * 180 / m.pi


def to_radian(alfa):
    return alfa * m.pi / 180


def nadji_brzinu(d, teta, y, g):
    return m.sqrt((g * (d**2)) / (2 * (m.cos(teta) ** 2) * (d * m.tan(teta) - y)))


def nadji_ugao(d, v, y, g, teta):
    ugao1 = m.atan((v**2 + m.sqrt(v**4 - g*(g*(d**2) + 2*y*(v**2)))) / (g*d))
    #ugao2 = m.atan()
    return ugao1


if __name__ == "__main__":
    main()
