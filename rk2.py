def rungekutta(f, g, R0, V0, M):
    koko = R.shape
    R1 = np.zeros(koko)
    V1 = np.zeros(koko)
    for i in range(koko[0]):
        for j in range(koko[1]):
            if (i != j):
                x0 = R0[i, j]
                y0 = V0[i, j]
                m = M[i, j]

                ax = f(x0, y0, m) 
                ay = g(x0, y0, m) 
                bx = f(x0 + 0.5*dt*ax, y0 + 0.5*dt*ay, m)
                by = g(x0 + 0.5*dt*ay, y0 + 0.5*dt*ay, m)
                cx = f(x0 + 0.5*dt*bx, y0 + 0.5*dt*bx, m)
                cy = g(x0 + 0.5*dt*by, y0 + 0.5*dt*by, m)
                dx = f(x0 + dt*cx, y0 + dt*cx, m)
                dy = g(x0 + dt*cy, y0 + dt*cy, m)

                R1[i, j] = x0 + dt*(ax + 2*bx + 2*cx + dx)/6
                V1[i, j] = y0 + dt*(ay + 2*by + 2*cy + dy)/6

    return (R1, V1)

def a(
