# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered
squareRed = stimuli.Rectangle((50,50),colour="Red",position=(-100,0))
squareGreen = stimuli.Rectangle((50,50),colour="Green",position=(100,0))


# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross
squareRed.present(clear=True, update=False)
squareGreen.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()