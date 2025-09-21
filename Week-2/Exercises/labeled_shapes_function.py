# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
posIni=0

def createPoli(side,length,label,color,pos):
    poligon = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(side, length), colour=(color), position=(pos)) 
    textpoli=stimuli.TextLine(label,(pos[0],pos[1]+length+70),text_colour=(255,255,255))
    lineHex=stimuli.Line((pos[0],pos[1]+length),(pos[0],pos[1]+length+50),3)
    poligon.present(clear=True,update=False)
    textpoli.present(clear=False,update=False)
    lineHex.present(clear=False,update=True)

control.start(subject_id=1)

createPoli(6,50,"hexagon",(255,255,0),(0,0))


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()