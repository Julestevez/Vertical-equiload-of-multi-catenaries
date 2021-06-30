# Vertical-equiload-of-multi-catenaries
This programme permits to obtain the vertical equiload configuration of chains of catenaries, included in the calculus of my PhD dissertation


Explanation of how to obtain a parabola
Note that the arc length (line integral) of the quadratic a*x0^2 + b*x0 is given by the integral of sqrt(1 + (2ax + b)^2) from x = 0 to x = x0. On solving the integral, the value of the integral is obtained as 0.5 * (I(u) - I(l)) / a, where u = 2ax0 + b; l = b; and I(t) = 0.5 * (t * sqrt(1 + t^2) + log(t + sqrt(1 + t^2)), the integral of sqrt(1 + t^2).

Since y0 = a * x0^2 + b * x0, b = y0/x0 - a*x0. Substituting the value of b in u and l, u = y0/x0 + a*x0, l = y0/x0 - a*x0. Substituting u and l in the solution of the line integral (arc length), we get the arc length as a function of a:

s(a) = 0.5 * (I(y0/x0 + a*x0) - I(y0/x0 - a*x0)) / a

Now that we have the arc length as a function of a, we simply need to find the value of a for which s(a) = S. This is where my favorite root-finding algorithm, the Newton-Raphson method, comes into play yet again.

The working algorithm for the Newton-Raphson method of finding roots is as follows:

For a function f(x) whose root is to be obtained, if x(i) is the ith guess for the root,

x(i+1) = x(i) - f(x(i)) / f'(x(i))

Where f'(x) is the derivative of f(x). This process is continued till the difference between two consecutive guesses is very small.

In our case, f(a) = s(a) - S and f'(a) = s'(a). By simple application of the chain rule and the quotient rule,

s'(a) = 0.5 * (a*x0 * (I'(u) + I'(l)) + I(l) - I(u)) / (a^2)

Where I'(t) = sqrt(1 + t^2).

The only problem that remains is calculating a good initial guess. Due to the nature of the graph of s(a), the function is an excellent candidate for the Newton-Raphson method, and an initial guess of y0 / x0 converges to the solution in about 5-6 iterations for a tolerance/epsilon of 1e-10.

Once the value of a is found, b is simply y0/x0 - a*x0.
