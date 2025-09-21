from expyriment import design, control, stimuli

exp = design.Experiment(name="Launching")
control.initialize(exp)

# Squares are created
squareRed = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0))   
squareGreen = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0))  

control.start(subject_id=1)

#Red square movement, from the left of the screen to the center where the green square is
for x in range(-1400, -50, 5):   #Threshold for the impression of causality: 25 pixels gap
    squareRed.position = (x, 0)
    exp.screen.clear() #Clears the screen every time the square moves so that it doesn't look like the square stretches
    squareGreen.present(clear=False, update=False)
    squareRed.present(clear=False, update=True) #Updates when both squares are in the buffer

#Green square movement, from the center to the right of the screen
for x in range(0, 1400, 5): 
    squareGreen.position = (x, 0)
    exp.screen.clear()
    squareRed.present(clear=False, update=False)
    squareGreen.present(clear=False, update=True)


exp.keyboard.wait()
control.end()