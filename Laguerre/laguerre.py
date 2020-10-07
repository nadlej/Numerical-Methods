import cmath


def horner(z, factor):
    if isinstance(factor, list):
        p = factor[len(factor) - 1]
        k = len(factor) - 1
    else:
        p = factor
        k = 0

    while k > 0:
        k = k - 1
        p = p * z + factor[k]
    return p


def derivative(pol):
    if (len(pol) - 1) == 0:
        return complex(0, 0)
    der = [0] * (len(pol) - 1)

    for i in range((len(pol) - 2), -1, -1):
        der[i] = pol[i + 1] * (i + 1)

    return der


def newpol(root, old_pol):
    new_pol = [0] * (len(old_pol)-1)
    new_pol[len(old_pol)-2] = old_pol[len(old_pol)-1]

    for i in range((len(old_pol)-3), -1, -1):
        new_pol[i] = old_pol[i+1] + (new_pol[i+1] * root)

    return new_pol


def laguerre(start, comlex):
    z = start
    tmp = complex(100, 0)

    while abs(horner(z, comlex) - horner(tmp, comlex)) > 1e-13:
        tmp = z
        fun = horner(z, comlex) * (len(comlex) - 1)
        der = horner(z, derivative(comlex))

        sec_der = horner(z, derivative(derivative(comlex)))

        denominator = cmath.sqrt((der * der * ((len(comlex) - 1) - 1) - (fun * sec_der)) * ((len(comlex) - 1) - 1))

        if (abs(der - denominator)) > (abs(der + denominator)):
            denominator = der - denominator
        else:
            denominator = der + denominator
        z = z - (fun/denominator)

    return z


def pierw(poly):
    start = complex(0, 0)
    z = [0] * (len(poly)-1)

    z[0] = laguerre(start, poly)
    tmp = poly

    for i in range(1, len(poly)-1, 1):
        pol_less = newpol(z[i-1], tmp)
        z[i] = laguerre(start, pol_less)
        z[i] = laguerre(z[i], poly)
        tmp = pol_less

    for i in range(0, len(z), 1):
        print(z[i])





complex_number = [complex(16,0), complex(-72,0), complex(-28,0), complex(558,0),
                    complex(-990,0), complex(783,0), complex(-486,0), complex(243,0)]
print("Podpunkt a")
pierw(complex_number)

complex_number = [complex(-4,0), complex(-4,0), complex(-12,0), complex(-8,0), complex(-11,0),
                    complex(-3,0), complex(-1,0), complex(2,0), complex(3,0), complex(1,0), complex(1,0)]
print("\nPodpunkt b")
pierw(complex_number)


complex_number = [complex(1, 0), complex(0, -1), complex(-1, 0), complex(0, 1), complex(1, 0)]
print("\nPodpunkt c")
pierw(complex_number)








