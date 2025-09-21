# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered
purpleTriangle = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(3, 50), colour=(128,0,255), position=(-100,0)) 
yellowHex= stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(6, 25), colour=(225,225,0), position=(100,0)) 
lineTri=stimuli.Line((-100,int(43.3/2)),(-100,int(43.3/2)+50),3)
lineHex=stimuli.Line((100,int(43.3/2)),(100,int(43.3/2)+50),3)
textTri=stimuli.TextLine("triangle",(-100,int(43.3/2)+70),text_colour=(255,255,255))
textHex=stimuli.TextLine("hexagon",(100,int(43.3/2)+70),text_colour=(255,255,255))

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross
purpleTriangle.present(clear=True, update=False)
yellowHex.present(clear=False, update=False)
lineTri.present(clear=False,update=False)
lineHex.present(clear=False,update=False)
textTri.present(clear=False,update=False)
textHex.present(clear=False,update=True)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()