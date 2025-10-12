from expyriment import design, control, stimuli
from expyriment.misc.constants import (C_WHITE, C_BLACK,K_DOWN, K_UP, K_LEFT, K_RIGHT, K_1, K_2, K_SPACE)


exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)
exp.add_data_variable_names(["Eye","Radius","Coordinates"])
inst=stimuli.TextScreen("Instructions","A circle and a fixation cross will appear in your screen. \n " \
"Please cover the eye that is on the same side of the cross. \n" \
"Move the circle using the left and right arrows on your keyboard but keep fixating on the cross. \n" \
"You will now you have found your blindspot when you are no longer able to see the circle. \n" \
"You can also make the circle smaller by pressing 1 or bigger by pressing 2. \n" \
"Press space to start")

# ---------- Helpers ----------
def make_circle(r, pos=(0, 0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10, colour=C_BLACK)
    c.preload()
    return c

def keyboardResp(keys):
    key, rt = exp.keyboard.wait(keys)
    return key

def run_trial(side):
    if side=="right":
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    elif side=="left":
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[-300, 0])

    fixation.preload()
    while True:
        inst.present()
        exp.keyboard.wait(K_SPACE)
        break

    radius = 75
    circle = make_circle(radius, pos=(0, 0)) 
    keys = [K_DOWN, K_UP, K_LEFT, K_RIGHT, K_1, K_2, K_SPACE]

    while True:
        fixation.present(clear=True, update=False)
        circle.present(clear=False, update=True)

        key = keyboardResp(keys)
   
        if key == K_LEFT:
            circle.move((-20, 0))
        elif key == K_RIGHT:
            circle.move((20, 0))
        elif key == K_1:
            radius -=10
            pos = circle.position
            circle = make_circle(radius, pos)   
        elif key == K_2:
            radius += 10
            pos = circle.position
            circle = make_circle(radius, pos)
        exp.data.add([side, radius, circle.position])
        if key == K_SPACE:
            break
        
        exp.clock.wait(20)  


control.start(subject_id=1)
run_trial("right")
control.end()