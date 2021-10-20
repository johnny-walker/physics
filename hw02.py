from vpython import *

size = 0.2 #ball radius (m)
distance = 0.4 #distance between two adjacent pivots (m)
mass = 1 #ball mass (kg)
N = 2 #how many balls are lifted at first
dt, k , g= 0.001, 150000, vector(0,-9.8,0)

length = 2+(-mass*g.y)/k #the original length of the rope 
L=2 #the length of the rope after the ball stretches 
t=0
(total_Ek , total_U , average_Ek , average_U) = (0,0,0,0)

def af_col_v(m1, m2, v1, v2, x1, x2): # function after collision velocity
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)

scene = canvas(title = 'Vpython HW02 - Newton cradle', width = 600, height =800, center=vec(0, -1.0, 0), background=vec(0.5,0.5,0) , align = 'left') # open window
msg = text(text = 'Newton cradle with '+str(N)+' ball(s) lifted' , pos=vec(-1.5,0.5,0),color=color.blue,height=0.15)
#ceiling = box(pos=vec(0,0,0) , length = 3 , height = 0.05 , width = 0.5 , color=color.black)
oscillation1 = graph(title = 'blue line - Ek_average , red line - U_average',width=500 , align='right')
oscillation2 = graph(title = 'blue line - Ek_sum versus time,red line : U_sum versus time',width=500 , align='right')
Ek_avg = gcurve(graph = oscillation1, color=color.blue, width=4)
U_avg = gcurve(graph = oscillation1, width=4, color=color.red)
Ek_sum = gcurve(graph = oscillation2, color=color.blue, width=4)
U_sum = gcurve(graph = oscillation2, width=4, color=color.red)


balls =[]

springs = []
for i in range(N):
    ball_reference = sphere (pos = vec(0.4*(i-2),0,0), radius = 0.02, color=color.white)
    balls.append(sphere(pos = vec(-1*(sqrt(4-pow(1.95,2))+0.4*(2-i)), -1.95 , 0), radius = size, color=color.white))
    springs.append(cylinder(pos = vec(0.4*(i-2) , 0 , 0), radius=0.005 , color=color.white))
    balls[i].v = vec(0,0,0)
    springs[i].axis = balls[i].pos - springs[i].pos
for i in range(N,5):
    ball_reference = sphere (pos = vec(0.4*(i-2),0,0), radius = 0.02, color=color.white)
    balls.append(sphere(pos = vec((0.4*(i-2)), -2.0 , 0), radius = size, color=color.white))
    springs.append(cylinder(pos = vec(0.4*(i-2) , 0 , 0), radius = 0.005, color=color.white))
    balls[i].v = vec(0,0,0)
    springs[i].axis = balls[i].pos - springs[i].pos

while True:
    rate(500)
    t=t+dt
    for i in range(5) :
        spring_force = -k*(mag(springs[i].axis) - length)*springs[i].axis.norm()
        balls[i].a = g+(spring_force/mass)
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        springs[i].axis = balls[i].pos - springs[i].pos
        balls[i].Ek = 0.5*mass*dot(balls[i].v,balls[i].v)
        balls[i].U = mass*(-g.y)*(2-( balls[i].pos.y * -1))
        total_Ek += balls[i].Ek
        total_U += balls[i].U
        average_Ek += balls[i].Ek/5
        average_U += balls[i].U/5
        #print(balls[i].Ek , balls[i].U)
    for i in range(4):
        if mag(balls[i].pos - balls[i+1].pos) <= size*2 and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0 :
            (balls[i].v, balls[i+1].v) = af_col_v (mass, mass, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)
            print(balls[i].pos, balls[i+1].pos)
            print(balls[i].v, balls[i+1].v)
    Ek_avg.plot(pos=(t , average_Ek))
    U_avg.plot(pos=(t , average_U))
    #Ek_sum.plot(pos=(t , total_Ek/t))
    #U_sum.plot(pos=(t , total_U/t))
    (average_Ek,average_U)=(0,0)

    
