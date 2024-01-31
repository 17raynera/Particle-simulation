import pygame
import pygame_gui
import math

#https://pygame-gui.readthedocs.io/en/latest/
#https://gamedevacademy.org/pygame-gui-tutorial-complete-guide/

test_user_parameters = {
    "PARTICLE_RADIUS" : 25,
    "NO_OF_PARTICLES" : 100,
    "PARTICLE_FRICTION" : 0,
    "PARTICLE_ELASTICITY": 1,
    "X_PARTICLE_VELOCITY_MEAN" : 0,
    "X_PARTICLE_VELOCITY_ST_DEV" : 200,
    "Y_PARTICLE_VELOCITY_MEAN" : 0,
    "Y_PARTICLE_VELOCITY_ST_DEV" : 200,
    "PARTICLE_VELOCITY_CORRELATION" : 0,
    "EDGE_FRICTION" : 0,
    "X_GRAVITY" : 0,
    "Y_GRAVITY" : 0,
    "PARTICLE_VELOCITY_ANTI_CORRELATION" : math.sqrt(1 - 0 * 0)  #must have the square of PARTICLE_VELOCITY_CORRELATION
}
test_benchmark_many_particles = {
    "PARTICLE_RADIUS" : 2,
    "NO_OF_PARTICLES" : 10000,
    "PARTICLE_FRICTION" : 0,
    "PARTICLE_ELASTICITY": 1,
    "X_PARTICLE_VELOCITY_MEAN" : 0,
    "X_PARTICLE_VELOCITY_ST_DEV" : 0,
    "Y_PARTICLE_VELOCITY_MEAN" : 0,
    "Y_PARTICLE_VELOCITY_ST_DEV" : 0,
    "PARTICLE_VELOCITY_CORRELATION" : 0,
    "EDGE_FRICTION" : 0,
    "X_GRAVITY" : 90,
    "Y_GRAVITY" : 90,
    "PARTICLE_VELOCITY_ANTI_CORRELATION" : math.sqrt(1 - 0 * 0)  #must have the square of PARTICLE_VELOCITY_CORRELATION
}
test_few_particles = {
    "PARTICLE_RADIUS" : 25,
    "NO_OF_PARTICLES" : 10,
    "PARTICLE_FRICTION" : 0,
    "PARTICLE_ELASTICITY": 1,
    "X_PARTICLE_VELOCITY_MEAN" : 0,
    "X_PARTICLE_VELOCITY_ST_DEV" : 200,
    "Y_PARTICLE_VELOCITY_MEAN" : 0,
    "Y_PARTICLE_VELOCITY_ST_DEV" : 200,
    "PARTICLE_VELOCITY_CORRELATION" : 0,
    "EDGE_FRICTION" : 0,
    "X_GRAVITY" : 0,
    "Y_GRAVITY" : 0,
    "PARTICLE_VELOCITY_ANTI_CORRELATION" : math.sqrt(1 - 0 * 0)  #must have the square of PARTICLE_VELOCITY_CORRELATION
}
test_benchmark_many_particles_no_grav = {
    "PARTICLE_RADIUS" : 2,
    "NO_OF_PARTICLES" : 10000,
    "PARTICLE_FRICTION" : 0,
    "PARTICLE_ELASTICITY": 1,
    "X_PARTICLE_VELOCITY_MEAN" : 0,
    "X_PARTICLE_VELOCITY_ST_DEV" : 200,
    "Y_PARTICLE_VELOCITY_MEAN" : 0,
    "Y_PARTICLE_VELOCITY_ST_DEV" : 200,
    "PARTICLE_VELOCITY_CORRELATION" : 0,
    "EDGE_FRICTION" : 0,
    "X_GRAVITY" : 0,
    "Y_GRAVITY" : 0,
    "PARTICLE_VELOCITY_ANTI_CORRELATION" : math.sqrt(1 - 0 * 0)  #must have the square of PARTICLE_VELOCITY_CORRELATION
}
test_simulated_ideal_gas = {
    "PARTICLE_RADIUS" : 1,
    "NO_OF_PARTICLES" : 100,
    "PARTICLE_FRICTION" : 0,
    "PARTICLE_ELASTICITY": 1,
    "X_PARTICLE_VELOCITY_MEAN" : 0,
    "X_PARTICLE_VELOCITY_ST_DEV" : 200,
    "Y_PARTICLE_VELOCITY_MEAN" : 0,
    "Y_PARTICLE_VELOCITY_ST_DEV" : 200,
    "PARTICLE_VELOCITY_CORRELATION" : 0,
    "EDGE_FRICTION" : 0,
    "X_GRAVITY" : 0,
    "Y_GRAVITY" : 0,
    "PARTICLE_VELOCITY_ANTI_CORRELATION" : math.sqrt(1 - 0 * 0)  #must have the square of PARTICLE_VELOCITY_CORRELATION
}
test_gravity_energy_conservation = {
    "PARTICLE_RADIUS" : 25,
    "NO_OF_PARTICLES" : 1,
    "PARTICLE_FRICTION" : 0,
    "PARTICLE_ELASTICITY": 1,
    "X_PARTICLE_VELOCITY_MEAN" : 0,
    "X_PARTICLE_VELOCITY_ST_DEV" : 0,
    "Y_PARTICLE_VELOCITY_MEAN" : 0,
    "Y_PARTICLE_VELOCITY_ST_DEV" : 0,
    "PARTICLE_VELOCITY_CORRELATION" : 0,
    "EDGE_FRICTION" : 0,
    "X_GRAVITY" : 0,
    "Y_GRAVITY" : 90,
    "PARTICLE_VELOCITY_ANTI_CORRELATION" : math.sqrt(1 - 0 * 0)  #must have the square of PARTICLE_VELOCITY_CORRELATION
}
test_histogram = {
    "PARTICLE_RADIUS" : 5,
    "NO_OF_PARTICLES" : 900,
    "PARTICLE_FRICTION" : 0,
    "PARTICLE_ELASTICITY": 1,
    "X_PARTICLE_VELOCITY_MEAN" : 500,
    "X_PARTICLE_VELOCITY_ST_DEV" : 100,
    "Y_PARTICLE_VELOCITY_MEAN" : 0,
    "Y_PARTICLE_VELOCITY_ST_DEV" : 100,
    "PARTICLE_VELOCITY_CORRELATION" : 0,
    "EDGE_FRICTION" : 0,
    "X_GRAVITY" : 0,
    "Y_GRAVITY" : 900,
    "PARTICLE_VELOCITY_ANTI_CORRELATION" : math.sqrt(1 - 0 * 0)  #must have the square of PARTICLE_VELOCITY_CORRELATION
}

#Horizontal and vertical gravity round the wrong way

left_edge = 100
left_edge_ui=300
right_edge = 450
right_edge_ui=710
upper_edge = 70
lower_edge = 300
increment = 30
width1 = 200
width2 = 260
width3 = 50

display_width = 800
display_height = 600

button_distance_from_left = 490
button_distance_from_top = 310
button_width = 200
button_height = 100

def populate_gui(parameters, entrylines):
    entrylines[0].set_text(str(parameters["PARTICLE_RADIUS"]))
    entrylines[1].set_text(str(parameters["NO_OF_PARTICLES"]))
    entrylines[2].set_text(str(parameters["PARTICLE_FRICTION"]*100))
    entrylines[3].set_text(str(parameters["PARTICLE_ELASTICITY"]*100))

    entrylines[4].set_text(str(parameters["X_PARTICLE_VELOCITY_MEAN"]))
    entrylines[5].set_text(str(parameters["X_PARTICLE_VELOCITY_ST_DEV"]))
    entrylines[6].set_text(str(parameters["Y_PARTICLE_VELOCITY_MEAN"]))
    entrylines[7].set_text(str(parameters["Y_PARTICLE_VELOCITY_ST_DEV"]))
    entrylines[8].set_text(str(parameters["PARTICLE_VELOCITY_CORRELATION"]*100))

    entrylines[9].set_text(str(parameters["EDGE_FRICTION"]*100))
    entrylines[10].set_text(str(parameters["X_GRAVITY"]))
    entrylines[11].set_text(str(parameters["Y_GRAVITY"]))
    print(parameters)

def place_text(manager):
    pygame_gui.elements.UITextBox(html_text="Particle properties:",
                                  relative_rect=pygame.Rect(left_edge, upper_edge, width1, increment),
                                  manager=manager)
    pygame_gui.elements.UITextBox(html_text="Radius:",
                                  relative_rect=pygame.Rect(left_edge, upper_edge + increment, width1, increment),
                                  manager=manager)
    pygame_gui.elements.UITextBox(html_text="Count:",
                                  relative_rect=pygame.Rect(left_edge, upper_edge + 2 * increment, width1,
                                                            increment), manager=manager)
    pygame_gui.elements.UITextBox(html_text="Friction (%):",
                                  relative_rect=pygame.Rect(left_edge, upper_edge + 3 * increment, width1,
                                                            increment), manager=manager)
    pygame_gui.elements.UITextBox(html_text="Elasticity (%):",
                                  relative_rect=pygame.Rect(left_edge, upper_edge + 4 * increment, width1,
                                                            increment), manager=manager)

    pygame_gui.elements.UITextBox(html_text="Particle initial conditions:",
                                  relative_rect=pygame.Rect(right_edge, upper_edge, width2, increment),
                                  manager=manager)
    pygame_gui.elements.UITextBox(html_text="Horizontal mean velocity:",
                                  relative_rect=pygame.Rect(right_edge, upper_edge + increment, width2, increment),
                                  manager=manager)
    pygame_gui.elements.UITextBox(html_text="Horizontal velocity st dev:",
                                  relative_rect=pygame.Rect(right_edge, upper_edge + 2 * increment, width2,
                                                            increment), manager=manager)
    pygame_gui.elements.UITextBox(html_text="Vertical mean velocity:",
                                  relative_rect=pygame.Rect(right_edge, upper_edge + 3 * increment, width2,
                                                            increment), manager=manager)
    pygame_gui.elements.UITextBox(html_text="Vertical velocity st dev:",
                                  relative_rect=pygame.Rect(right_edge, upper_edge + 4 * increment, width2,
                                                            increment), manager=manager)
    pygame_gui.elements.UITextBox(html_text="Correlation (%):",
                                  relative_rect=pygame.Rect(right_edge, upper_edge + 5 * increment, width2,
                                                            increment), manager=manager)

    pygame_gui.elements.UITextBox(html_text="Container properties:",
                                  relative_rect=pygame.Rect(left_edge, lower_edge, width1, increment),
                                  manager=manager)
    pygame_gui.elements.UITextBox(html_text="Edge friction (%):",
                                  relative_rect=pygame.Rect(left_edge, lower_edge + increment, width1, increment),
                                  manager=manager)
    pygame_gui.elements.UITextBox(html_text="Horizontal gravity:",
                                  relative_rect=pygame.Rect(left_edge, lower_edge + 2 * increment, width1,
                                                            increment), manager=manager)
    pygame_gui.elements.UITextBox(html_text="Vertical gravity:",
                                  relative_rect=pygame.Rect(left_edge, lower_edge + 3 * increment, width1,
                                                            increment), manager=manager)

def place_entrylines(manager):
    entrylines = []
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((left_edge_ui, upper_edge + increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((left_edge_ui, upper_edge + 2 * increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((left_edge_ui, upper_edge + 3 * increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((left_edge_ui, upper_edge + 4 * increment), (width3, increment)), manager))

    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((right_edge_ui, upper_edge + increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((right_edge_ui, upper_edge + 2 * increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((right_edge_ui, upper_edge + 3 * increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((right_edge_ui, upper_edge + 4 * increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((right_edge_ui, upper_edge + 5 * increment), (width3, increment)), manager))

    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((left_edge_ui, lower_edge + increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((left_edge_ui, lower_edge + 2 * increment), (width3, increment)), manager))
    entrylines.append(pygame_gui.elements.UITextEntryLine(
        pygame.Rect((left_edge_ui, lower_edge + 3 * increment), (width3, increment)), manager))
    for i, el in enumerate(entrylines):
        if i in [4, 5, 6, 7, 8, 10, 11]:
            el.set_allowed_characters(
                ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-'])  # want -ve numbers too
        else:
            el.set_allowed_characters('numbers')
    return entrylines

def select_scenario(dropdown_selector):
    if dropdown_selector.current_state.selected_option_button.text == 'test_benchmark_many_particles':
        parameters = test_benchmark_many_particles
    elif dropdown_selector.current_state.selected_option_button.text == 'test_few_particles':
        parameters = test_few_particles
    elif dropdown_selector.current_state.selected_option_button.text == 'test_benchmark_many_particles_no_grav':
        parameters = test_benchmark_many_particles_no_grav
    elif dropdown_selector.current_state.selected_option_button.text == 'test_simulated_ideal_gas':
        parameters = test_simulated_ideal_gas
    elif dropdown_selector.current_state.selected_option_button.text == 'test_gravity_energy_conservation':
        parameters = test_gravity_energy_conservation
    elif dropdown_selector.current_state.selected_option_button.text == 'test_histogram':
        parameters = test_histogram
    return parameters

def get_parameters(entrylines):
    corr = int(entrylines[8].get_text())/100
    parameters = {
        "PARTICLE_RADIUS": int(entrylines[0].get_text()),
        "NO_OF_PARTICLES": int(entrylines[1].get_text()),
        "PARTICLE_FRICTION": int(entrylines[2].get_text())/100,
        "PARTICLE_ELASTICITY": int(entrylines[3].get_text())/100,
        "X_PARTICLE_VELOCITY_MEAN": int(entrylines[4].get_text()),
        "X_PARTICLE_VELOCITY_ST_DEV": int(entrylines[5].get_text()),
        "Y_PARTICLE_VELOCITY_MEAN": int(entrylines[6].get_text()),
        "Y_PARTICLE_VELOCITY_ST_DEV": int(entrylines[7].get_text()),
        "PARTICLE_VELOCITY_CORRELATION": corr,
        "EDGE_FRICTION": int(entrylines[9].get_text())/100,
        "X_GRAVITY": int(entrylines[10].get_text()),
        "Y_GRAVITY": int(entrylines[11].get_text()),
        #"PARTICLE_VELOCITY_ANTI_CORRELATION": math.sqrt(1 - corr * corr)
        # must have the square of PARTICLE_VELOCITY_CORRELATION
    }
    return parameters

def check_user_input(parameters):
    input_sanitized = True
    if parameters["PARTICLE_RADIUS"] < 1 or parameters["PARTICLE_RADIUS"] > 475:
        input_sanitized = False
        print("Radius must be between 1 and 475")
    elif parameters["NO_OF_PARTICLES"] <1 or parameters["NO_OF_PARTICLES"] > 20000:
        input_sanitized = False
        print("Count must be betweeen 1 and 20,000")
    elif parameters ["PARTICLE_FRICTION"] < 0 or parameters ["PARTICLE_FRICTION"] >1:
        input_sanitized = False
        print("Friction (%) must be between 0 and 100")
    elif parameters["PARTICLE_ELASTICITY"] < 0 or parameters["PARTICLE_ELASTICITY"] > 1:
        input_sanitized = False
        print("Elasticity (%) must be between 0 and 100")
    elif parameters["X_PARTICLE_VELOCITY_MEAN"] < -1000 or parameters["X_PARTICLE_VELOCITY_MEAN"] > 1000:
        input_sanitized = False
        print("Horizontal mean velocity must be between -1000 and 1000")
    elif parameters["X_PARTICLE_VELOCITY_ST_DEV"] < -1000 or parameters["X_PARTICLE_VELOCITY_ST_DEV"] > 1000:
        input_sanitized = False
        print("Horizontal velocity st dev must be between -1000 and 1000")
    elif parameters["Y_PARTICLE_VELOCITY_MEAN"] < -1000 or parameters["Y_PARTICLE_VELOCITY_MEAN"] > 1000:
        input_sanitized = False
        print("Vertical mean velocity must be between -1000 and 1000")
    elif parameters["Y_PARTICLE_VELOCITY_ST_DEV"] < -1000 or parameters["Y_PARTICLE_VELOCITY_ST_DEV"] > 1000:
        input_sanitized = False
        print("Vertical velocity st dev must be between -1000 and 1000")
    elif parameters["PARTICLE_VELOCITY_CORRELATION"] < -1 or parameters["PARTICLE_VELOCITY_CORRELATION"] > 1:
        input_sanitized = False
        print("Correlation (%) must be between -100 and 100")
    elif parameters["EDGE_FRICTION"] < 0 or parameters["EDGE_FRICTION"] > 1:
        input_sanitized = False
        print("Edge friction (%) must be between 0 and 100")
    elif parameters["X_GRAVITY"] < -10000 or parameters["X_GRAVITY"] > 10000:
        input_sanitized = False
        print("Vertical gravity must be between -10,000 and 10,000")
    elif parameters["Y_GRAVITY"] < -10000 or parameters["Y_GRAVITY"] > 10000:
        input_sanitized = False
        print("Horizontal gravity must be between -10,000 and 10,000")

    return input_sanitized

def get_user_input():

    pygame.init()

    pygame.display.set_caption('Scenario Parameters')
    window_surface = pygame.display.set_mode((display_width, display_height))

    background = pygame.Surface((display_width, display_height))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((display_width, display_height), "gui.json")

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_distance_from_left, button_distance_from_top), (button_width, button_height)),text='Start',manager=manager)

    place_text(manager)
    entrylines = place_entrylines(manager)
    dropdown_selector = pygame_gui.elements.UIDropDownMenu(['test_benchmark_many_particles', 'test_few_particles', 'test_benchmark_many_particles_no_grav', 'test_simulated_ideal_gas', 'test_gravity_energy_conservation', 'test_histogram'], 'test_simulated_ideal_gas', pygame.Rect((0, 0), (350, 30)), manager)
    populate_gui(test_simulated_ideal_gas, entrylines)

    clock = pygame.time.Clock()
    is_running = True

    gui_x_pressed = False
    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                gui_x_pressed = True

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    parameters = get_parameters(entrylines)
                    input_sanitized = check_user_input(parameters)
                    if input_sanitized == True:
                        is_running = False

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                parameters = select_scenario(dropdown_selector)
                populate_gui(parameters, entrylines)



            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


    parameters = get_parameters(entrylines)

    return parameters, gui_x_pressed
