from expyriment import design, control, stimuli, misc
from typing import Tuple

exp = design.Experiment(name="Launching",background_colour=misc.constants.C_GREY)

control.initialize(exp)

width, height= exp.screen.size

def sizes(aspectRatio: Tuple[int, int],rectSF,circleSF):
    rectWidth=aspectRatio[0]*rectSF
    rectHeight=aspectRatio[1]*rectSF
    radius=aspectRatio[0]*circleSF
    rectangle=stimuli.Rectangle((rectWidth,rectHeight), colour=misc.constants.C_GREY,line_width=0, position=(0,0))
    circle1=stimuli.Circle(int(radius), colour=misc.constants.C_BLACK,line_width=0, position=(rectWidth/2,rectHeight/2))
    circle2=stimuli.Circle(int(radius), colour=misc.constants.C_BLACK,line_width=0, position=(-rectWidth/2,rectHeight/2))
    circle3=stimuli.Circle(int(radius), colour=misc.constants.C_WHITE,line_width=0, position=(-rectWidth/2,-rectHeight/2))
    circle4=stimuli.Circle(int(radius), colour=misc.constants.C_WHITE,line_width=0, position=(rectWidth/2,-rectHeight/2))

    circle1.present(clear=True, update=False)
    circle2.present(clear=False, update=False)
    circle3.present(clear=False, update=False)
    circle4.present(clear=False, update=False)
    rectangle.present(clear=False, update=True)

sizes((4,3),300,75)

exp.keyboard.wait()
control.end()