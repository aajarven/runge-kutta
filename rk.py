G = 1 #TODO muuta

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


def kertoimet(f, g, x0, y0, dt):
    ax = f(x0, y0)
    ay = g(x0, y0)
    bx = f(x0 + 0.5*dt*ax, y0 + 0.5*dt*ay)
    by = g(x0 + 0.5*dt*ay, y0 + 0.5*dt*ay)
    cx = f(x0 + 0.5*dt*bx, y0 + 0.5*dt*bx)
    cy = g(x0 + 0.5*dt*by, y0 + 0.5*dt*by)
    dx = f(x0 + dt*cx, y0 + dt*cx)
    dy = f(x0 + dt*cy, y0 + dt*cy)

    return ([ax, bx, cx, dx], [ay, by, cy, dy])

def a(M, R, i):
    a = 0
    for j in range(0, len(M)):
        if (j==i):
            continue
        a = a - G*M[j]*(np.subtract(R[i], R[j]))/np.sqrt(x.dot(x))
    return a

# huom ei sis m
def a(x1, x2):
    return -G*(x1-x2)/(np.dot(x1, x2)**(3/2))



lkm = 2 # kappaleiden lukumäärä
x0 = [[0, 0], [1, 0]]
v0 = [[0, 0], [5, 0]]
t = 0
t_max = 10

kx = np.zeros(4, lkm)
# k1,1 k1,2 ... k1,n 
# k2,1 k2,2 ... k2,n
# k3,1 k3,2 ... k3,n
# k3,1 k3,2 ... k4,n
kv = np.zeros(4, lkm)
# k1,1 k1,2 ... k1,n
# k2,1 k2,2 ... k2,n
# k3,1 k3,2 ... k3,n
# k3,1 k3,2 ... k4,n

while(t<t_max):
    for i in range(lkm):
        for j in range(lkm):
            if (i != j):
                tmp = 

#initialize the particles’ velocity and position
#while (elapsed simulation time < end time) {
#        for (each k1, k2, k3, k4) {
#            for (each particle) {
#                for (each particle) {
#                    calculate the gravitational acceleration between the two particles
#                    store the value in the appropriate k
#                    }
#                }
#            }
#        for (each particle) {
#            use the k constants to update the position and velocity
#            }
#        for (each particle) {
#            for (each particle) {
#                if these particles have collided, combine them
#                }
#            }
#        }
