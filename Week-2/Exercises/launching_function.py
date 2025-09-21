from expyriment import design, control, stimuli

exp = design.Experiment(name="Launching")
control.initialize(exp)

# Squares are created
squareRed = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0))   
squareGreen = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0))  

control.start(subject_id=1)

def launching_function(temp,spat,speed):
    #Red square movement, from the left of the screen to the center where the green square is
    for x in range(-1400, int(-spat/2), 5):   # Changes position from left to right in steps of 5 pixels
        #Takes half ot the spatial gap to the left
        squareRed.position = (x, 0)
        exp.screen.clear() #Clears the screen every time the square moves so that it doesn't look like the square stretches
        squareGreen.present(clear=False, update=False)
        squareRed.present(clear=False, update=True) #Updates when both squares are in the buffer

    exp.clock.wait(temp)

    #Green square movement, from the center to the right of the screen
    for x in range(int(spat/2), 1400, speed*5): #Takes half of the spatial gap to the right
        #Multiplies the speed of the red square
        squareGreen.position = (x, 0)
        exp.screen.clear()
        squareRed.present(clear=False, update=False)
        squareGreen.present(clear=False, update=True)

launching_function(250,500,3)

exp.keyboard.wait()
control.end()