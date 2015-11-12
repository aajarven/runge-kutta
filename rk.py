G = 6.67408E-11 #m^3/(kg*s^2)

def rungekutta(f, g, x0, y0, dt):
    ax = f(x0, y0)
    ay = g(x0, y0)
    bx = f(x0 + 0.5*dt*ax, y0 + 0.5*dt*ay)
    by = g(x0 + 0.5*dt*ay, y0 + 0.5*dt*ay)
    cx = f(x0 + 0.5*dt*bx, y0 + 0.5*dt*bx)
    cy = g(x0 + 0.5*dt*by, y0 + 0.5*dt*by)
    dx = f(x0 + dt*cx, y0 + dt*cx)
    dy = f(x0 + dt*cy, y0 + dt*cy)

    x1 = x0 + dt*(ax + 2*bx + 2*cx + dx)/6
    y1 = y0 + dt*(ay + 2*by + 2*cy + dy)/6

    return (x1, y1)

def a(M, R, i):
    a = 0
    for j in range(0, len(M)):
        if (j==i):
            continue
        a = a - G*M[j]*(np.subtract(R[i], R[j]))/np.sqrt(x.dot(x))
    return a

def rdot(x, y):
    return y

def vdot(x, y):

