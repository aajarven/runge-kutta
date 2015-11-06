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


