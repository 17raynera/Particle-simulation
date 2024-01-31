import pygame
import pymunk
import pymunk.pygame_util
import sys
import random
import math
import fast_histogram
import gui
import chart
random.seed(1)  # This makes every random number generation the same for each run,
                # making it consistent and simplifying debugging

#For optimisation: http://www.pymunk.org/en/latest/overview.html#performance

# Application constants
PYMUNK_DYNAMIC = 0  #Pymunk gives dynamic, static, and kinematic bodies different numbers
                    #to differentiate them. The number for dynamic bodies is 0

SCREEN_Y = 1000
BOX_X = 1000
BOX_THICKNESS = 50
PARTICLE_MASS = 1
HISTOGRAM_X = 600
HISTOGRAM_Y = 500
SCREEN_X = BOX_X + HISTOGRAM_X + BOX_THICKNESS * 5

# Parameters constants
# Note that:
# safe_distance_from_edge<SCREEN_X - safe_distance_from_edge
# safe_distance_from_edge<SCREEN_Y - safe_distance_from_edge
# PARTICLE_FRICTION >= 0
# PARTICLE_VELOCITY_CORRELATION <= 1, >= -1



def add_static_box(space,parameters):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    half_screen_x = 0.5 * BOX_X
    half_screen_y = 0.5 * SCREEN_Y
    body.position = (half_screen_x, half_screen_y)
    l1 = pymunk.Segment(body, (-half_screen_x, half_screen_y), (half_screen_x, half_screen_y), BOX_THICKNESS)
    l2 = pymunk.Segment(body, (half_screen_x, half_screen_y), (half_screen_x, -half_screen_y), BOX_THICKNESS)
    l3 = pymunk.Segment(body, (half_screen_x, -half_screen_y), (-half_screen_x, -half_screen_y), BOX_THICKNESS)
    l4 = pymunk.Segment(body, (-half_screen_x, -half_screen_y), (-half_screen_x, half_screen_y), BOX_THICKNESS)
    l1.friction = parameters["EDGE_FRICTION"]
    l2.friction = parameters["EDGE_FRICTION"]
    l3.friction = parameters["EDGE_FRICTION"]
    l4.friction = parameters["EDGE_FRICTION"]
    l1.elasticity = parameters["PARTICLE_ELASTICITY"]
    l2.elasticity = parameters["PARTICLE_ELASTICITY"]
    l3.elasticity = parameters["PARTICLE_ELASTICITY"]
    l4.elasticity = parameters["PARTICLE_ELASTICITY"]
    space.add(body, l1, l2, l3, l4)

def add_particle(space,parameters):
    mass = PARTICLE_MASS
    radius = parameters["PARTICLE_RADIUS"]
    body = pymunk.Body()
    safe_distance_from_edge = int(0.5*BOX_THICKNESS) + parameters["PARTICLE_RADIUS"]
    x = random.randint(safe_distance_from_edge, BOX_X - safe_distance_from_edge)
    y = random.randint(safe_distance_from_edge, SCREEN_Y - safe_distance_from_edge)
    body.position = x, y
    z = random.normalvariate(0, 1)
    w = random.normalvariate(0, 1)
    x_velocity = parameters["X_PARTICLE_VELOCITY_MEAN"] + parameters["X_PARTICLE_VELOCITY_ST_DEV"] * z
    y_velocity = parameters["Y_PARTICLE_VELOCITY_MEAN"] + parameters["Y_PARTICLE_VELOCITY_ST_DEV"] * (parameters["PARTICLE_VELOCITY_CORRELATION"] * z + parameters["PARTICLE_VELOCITY_ANTI_CORRELATION"] * w)
    body.velocity = x_velocity, y_velocity
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.friction = parameters["PARTICLE_FRICTION"]
    shape.elasticity = parameters["PARTICLE_ELASTICITY"]
    space.add(body, shape)


def setup_space(screen, space,parameters):
    space.gravity = (parameters["X_GRAVITY"], parameters["Y_GRAVITY"])
    for x in range(parameters["NO_OF_PARTICLES"]):
        add_particle(space,parameters)

    draw_options = pymunk.pygame_util.DrawOptions(screen)
    #print_options = pymunk.SpaceDebugDrawOptions()  # For easy printing
    add_static_box(space,parameters)
    return draw_options


def calc_ke(space):
    kinetic_energy = []
    for x in space.bodies:
        if x.body_type == PYMUNK_DYNAMIC:  # only use Ke of dynamic objects
            kinetic_energy.append(x.kinetic_energy*0.5)
    return kinetic_energy

def particle_collector(space, parameters):
    half_screen_x = 0.5 * BOX_X
    half_screen_y = 0.5 * SCREEN_Y
    for b in space.bodies:
        if b.position.x > half_screen_x*2 or b.position.x < 0 or b.position.y > half_screen_y*2 or b.position.y < 0:
            v = b.velocity
            space.remove(b)
            mass = PARTICLE_MASS
            body = pymunk.Body()
            body.position = half_screen_x, half_screen_y
            body.velocity = v
            shape = pymunk.Circle(body, parameters["PARTICLE_RADIUS"])
            shape.mass = mass
            shape.friction = parameters["PARTICLE_FRICTION"]
            shape.elasticity = parameters["PARTICLE_ELASTICITY"]
            space.add(body, shape)

#https://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
round_to_n = lambda x, n: x if x == 0 else round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

def plot_histograms(screen,clock,kinetic_energy, initial_max_ke, num_of_bins):
    max_ke = max(max(kinetic_energy), initial_max_ke)
    min_ke = min(kinetic_energy)
    tot_ke = sum(kinetic_energy)
    avg_ke= tot_ke/len(kinetic_energy)

    vel_max_x = round_to_n(math.sqrt(-2*avg_ke/PARTICLE_MASS*math.log(1-.999)),1)#math.sqrt(2*initial_max_ke/PARTICLE_MASS)
    ke_max_x = round_to_n(0.5*PARTICLE_MASS*vel_max_x*vel_max_x,1)
    if avg_ke ==0:
        vel_max_y = None
        ke_max_y = None
    else:
        vel_max_y = round_to_n(2*math.exp(-1/2)*math.sqrt(PARTICLE_MASS/avg_ke), 1) #double max value of probability density function
        ke_max_y = round_to_n(2*0.5*PARTICLE_MASS*vel_max_y*vel_max_y, 1)

    bin_width= (ke_max_x + 1) / num_of_bins
    bins =list(i* bin_width for i in range(num_of_bins))
    #bins_str = list(str(round(i*bin_width)) for i in range(num_of_bins))
    KE_histogram = fast_histogram.histogram1d(kinetic_energy, num_of_bins, (0, ke_max_x + 1))
    #print("bin_width=" + str(bin_width)+ ", bins=" + str(bins) + "\n vals=" + str(histogram.tolist()))
    #Histogram of particle energies

    chart.histogram(screen,(BOX_X+2*BOX_THICKNESS,0,HISTOGRAM_X,HISTOGRAM_Y),bins,KE_histogram.tolist(), title= 'Kinetic Energy Histogram',max_y=ke_max_y)

    #Histogram of particle velocities
    velocity = list(math.sqrt(k / 0.5 * PARTICLE_MASS) for k in kinetic_energy)
    bin_width_vel = (vel_max_x + 1) / num_of_bins
    velocity_bins = list(i*bin_width_vel for i in range(num_of_bins))
    velocity_histogram = fast_histogram.histogram1d(velocity, num_of_bins, (0, vel_max_x + 1))

    def vel_probability_density_function(s):
        alpha = PARTICLE_MASS/(avg_ke+0.00000000001)
        return alpha*s*math.exp(-alpha*s*s/2)
    chart.histogram(screen,(BOX_X+2*BOX_THICKNESS,HISTOGRAM_Y,HISTOGRAM_X,HISTOGRAM_Y),velocity_bins,velocity_histogram.tolist(), title= 'Velocity Histogram & Theoretical Distribution',probability_density_function = vel_probability_density_function, max_y= vel_max_y)


    pygame.display.set_caption("Particle Simulation: FPS=" + str(round((clock.get_fps()), 1)) + ", KE min/max/total=" + str(round(min_ke)) + " / " + str(round(max_ke)) + " / " + str(round(tot_ke)))


def main(parameters):

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    clock = pygame.time.Clock()

    # This is the "Space" object in pymunk which contains the simulation
    space = pymunk.Space()
    draw_options = setup_space(screen,space,parameters)

    initial_max_ke = max(calc_ke(space))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        screen.fill("white")
        space.debug_draw(draw_options)
        space.step(1/50.0)
        clock.tick(50)

        kinetic_energy = calc_ke(space)
        particle_collector(space, parameters)

        plot_histograms(screen,clock,kinetic_energy, initial_max_ke, 30)
        pygame.display.update()

if __name__ == '__main__':
    parameters, gui_x_pressed = gui.get_user_input()
    parameters.update({'PARTICLE_VELOCITY_ANTI_CORRELATION': math.sqrt(1 - parameters ["PARTICLE_VELOCITY_CORRELATION"] * parameters ["PARTICLE_VELOCITY_CORRELATION"]) })

    if gui_x_pressed == False:
        sys.exit(main(parameters))



