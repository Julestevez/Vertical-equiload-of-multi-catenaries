#this is a pseudocode to obtain the parabola between two points, knowing the arc length of it
def find_coeff(x0, y0, s0):
    def dI(t):
        return sqrt(1 + t*t)

    def I(t):
        rt = sqrt(1 + t*t)
        return 0.5 * (t * rt + log(t + rt))

    def s(a):
        u = y0/x0 + a*x0
        l = y0/x0 - a*x0
        return 0.5 * (I(u) - I(l)) / a

    def ds(a):
        u = y0/x0 + a*x0
        l = y0/x0 - a*x0
        return 0.5 * (a*x0 * (dI(u) + dI(l)) + I(l) - I(u)) / (a*a)

    N = 1000
    EPSILON = 1e-10
    guess = y0 / x0

    for i in range(N):
        dguess = (s(guess) - s0) / ds(guess)
        guess -= dguess
        if abs(dguess) <= EPSILON:
            print("Break:", abs((s(guess) - s0)))
            break
        print(i+1, ":", guess)

    a = guess
    b = y0/x0 - a*x0

    print(a, b, s(a))