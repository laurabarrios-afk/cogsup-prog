from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_WHITE, C_BLUE, C_RED, C_YELLOW

exp = design.Experiment(name="ternus")
control.initialize(exp)
width,height=exp.screen.size
canvas=stimuli.Canvas(size=(width,height))

posX1=[(-width/4)*3,-width/4,width/4] #Establishes positions for the first 3 circles and tags
posX2=[-width/4,width/4,(width/4)*3] #Changes the position of the first circle and tag
colors1=[C_YELLOW,C_BLUE,C_RED] #Establishes colors for the first 3 tags
colors2=[C_BLUE,C_RED,C_YELLOW] #"Moves" the first tag to the right 

def run_trial(rad,use_tags,isi):
    circles1 = [stimuli.Circle(radius=rad, position=(pos,0), colour=C_WHITE) for pos in posX1] #Creates the first 3 circles
    circles2 = [stimuli.Circle(radius=rad, position=(pos,0), colour=C_WHITE) for pos in posX2] #Moves the first circle to the right
    tags1 = [stimuli.Circle(radius=20, position=(pos,0), colour=color) for pos,color in zip(posX1,colors1)] #Changes the position of the first circle and tag
    tags2 = [stimuli.Circle(radius=20, position=(pos,0), colour=color) for pos,color in zip(posX2,colors2)] #Moves thefirst tag to the right 
    while True:
        if use_tags: #If use_tags=True, stims becomes a list of circles+tags, with tags last so that the can be drawed on top of the circles
            present_for(circles1+tags1,12) #Displays all the items of the list and waits for 200 ms
            exp.clock.wait(isi*16.67) #Waits the given ISI
            present_for(circles2+tags2,12) #Displays all the items with the new positions 
        else: #Displays only the big circles
            present_for(circles1,12) 
            exp.clock.wait(isi*16.67)
            present_for(circles2,12)
        if exp.keyboard.check(K_SPACE): #Allows to exit the loop
            break
        
def present_for(stims,frames):
    t0 = exp.clock.time #Takes the time before drawing the stimuli
    for i, stim in enumerate(stims):
        stim.present(clear=(i==0), update=(i==len(stims)-1))
    t1=exp.clock.time
    delay=t1-t0
    if frames*16.67>delay:
        exp.clock.wait(frames*16.67-delay)
        
run_trial(rad=100, isi=3, use_tags=False)
run_trial(rad=100, isi=30, use_tags=False)
run_trial(rad=100, isi=3, use_tags=True)

control.end()